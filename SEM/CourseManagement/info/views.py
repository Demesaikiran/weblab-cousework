from typing import ContextManager
from django.core.files import storage
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Dept, Class, Student, Attendance, Course, Teacher, Assign, AttendanceTotal, \
    DAYS_OF_WEEK, AttendanceClass, StudentCourse, Marks, MarksClass, AbstractUser, User, AssignTime, time_slots
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#----------------------------------------------------------------#
from tablib import Dataset
from django.contrib import messages
from django.http import HttpResponse
# from .resources import UserResource
#----------------------------------------------------------------#
# from .decorators import *

from django.core.files.storage import default_storage
import os
import re
import glob
import pandas as pd
import openpyxl 
import xlrd
'''
admin:demesaikiran
joshi:jntuhces
saikiran:project123
AJNTUCES adminjntuces : project123
'''
@admin_only
def user_upload(request):
    print("Hello")
    #return render(request, 'info/temporary.html')
    #return render(request, 'info/a_homepage.html')
    if request.method == "POST":
        user_resource = UserResource()
        #return render(request, 'info/a_homepage.html')
        dataset = Dataset()
        
        if request.POST.get('myfile') == '':
            messages.info(request, "Upload some file")
            return render(request, "info/a_adminUpload.html")
        else:
            new_user = request.FILES['myfile']

        

        if not new_user.name.endswith('xlsx'):
            messages.info(request, 'WrongFormat')
            #return render(request, 'upload.html')
            return render(request, 'info/a_adminUpload.html')

        imported_data = dataset.load(new_user.read(), format = 'xlsx')
        for data in imported_data:
            try:
                User.objects.get(username = data[0])
                continue
            except User.DoesNotExist:
                value = User.objects.create_user(data[0],  data[1],  data[2])
                #We need to set the type of user here 
                #You can add a user to a group teacher or student by 
                answer = request.POST.get('group', False )# This value is that name we keep for storing dropdown values
                group = Group.objects.get(name = answer)
                value.groups.add(group)
                value.save()
            
            

    return render(request, 'info/a_adminUpload.html')

def a_tsDBUploading(request):
    if request.method == "POST":
        user_resource = UserResource()
        dataset = Dataset()
        #new_user = request.FILES['myfile']

        if request.POST.get('myfile') == '':
            messages.info(request, "Upload some file")
            return render(request, "info/a_adminUpload.html")
        else:
            new_user = request.FILES['myfile']

        if not new_user.name.endswith('xlsx'):
            messages.info(request, 'WrongFormat')
            return render(request, 'info/a_teacherStudentUpload.html')

        imported_data = dataset.load(new_user.read(), format = 'xlsx')

        usertype = request.POST.get('usertype', False )
        if usertype == 'Teacher':

            for data in imported_data:
                try:
                    Teacher.objects.get(id = data[0])
                    continue
                except Teacher.DoesNotExist:
                    try:
                        value = Teacher(id = data[0], name = data[3],Gender = data[4], DOB= data[5], email = data[6], phone_number = data[7])
                        index = int((Dept.objects.get(name = data[2])).id)
                        value.dept_id = index

                    except Dept.DoesNotExist:
                        pass

                    try:
                        userindex = int((User.objects.get(username = data[1])).id)
                        value.user_id = userindex
                        value.save()

                    except User.DoesNotExist:
                        cUser = User.objects.create_user(data[1], data[6], data[0])
                        group = Group.objects.get(name = usertype)
                        cUser.groups.add(group)
                        cUser.save()
                        userindex = int((User.objects.get(username = data[1])).id)
                        value.user_id = userindex
                        value.save()

        elif usertype == 'Student':
            for data in imported_data:
                print(data)
                try:
                    Student.objects.get(HTNo = data[1])
                    continue
                except Student.DoesNotExist:
                    value = Student(HTNo = data[1], name = data[2], father_name = data[3], college_code = data[4], 
                    branch_code = data[5], Gender = data[6], phone_number = data[7], reservation = data[8],
                    DOB = data[9], address = data[10], phone_number2 = data[11], moles = data[12], email = data[13], scribe = data[14], 
                    religion = data[15], ph_status = data[16], adm_category = data[17], adhar_number = data[18])

                    #dept_index = Dept.objects.get(name = )<In case of dept_id>
                    
                    if data[4]== None:
                        value.college_code = (value.HTNo)[2:4]
                    #17ss1a0514
                    if data[5] == None:
                        value.branch_code = (value.HTNo)[6:8]
                        

                    class_index = Class.objects.get(dept_id = (value.HTNo)[6:8], section = (value.HTNo)[5], sem = 1).id

                    value.class_id_id = class_index

                    try:
                        userindex = int((User.objects.get(username = data[0])).id)
                        value.user_id = userindex
                        value.save()
                    except User.DoesNotExist:
                        cUser = User.objects.create_user(data[0], data[13], data[1])
                        group = Group.objects.get(name = usertype.lower())
                        cUser.groups.add(group)
                        cUser.save()
                        userindex = int((User.objects.get(username = data[0])).id)
                        value.user_id = userindex
                        value.save()
                    


    return render(request, 'info/a_teacherStudentUpload.html')

@admin_only
def a_studentMarks(request):

    if request.method == "POST":
        rollno = request.POST['hallticket']
        fl = os.listdir('media/')

        #filelist = [f for f in glob.glob("media/"+"*.xlsx", recursive = True)] #AnotherMethod
        #Selecting files of required rollNo
        filelist=[]
        for t in fl:
            if t[:2] == rollno[:2]:
                filelist.append(t)
        print(filelist)
        #Regular expression Based Selection (Try)
        #temp = filelist.join(' ')
        #filelist2 = re.findall(r"(+")



        dataset = Dataset()
        
        data = {}
        name = Student.objects.get(HTNo = rollno)
        fathername = (Student.objects.get(HTNo = rollno)).father_name

        subjects = []
        cgpa = 0
        tcredits = 0
        tfail = 0

        for selectedfile in filelist:
            file = default_storage.open(selectedfile)
            dept = rollno[6:8]
            branch = (Dept.objects.get(id = dept)).name
            df = pd.read_excel('media/'+selectedfile, sheet_name = branch)
            
            subjects = list(df.columns)
            print(subjects)
            subjects = subjects[3:-2:2]
            keyvalue = selectedfile[2] + selectedfile[3]
            data[keyvalue] = {}

            data[keyvalue]['Regulation'] = 'R16'

            for mdata in (df.values.tolist()):
                if mdata[1] != rollno:
                    continue
                else:
                    index = 3

                    for subject in subjects:
                        data[keyvalue][subject] = [mdata[index], mdata[index + 1]]
                        if(mdata[index] == 'F'):
                            tfail = tfail + 1
                        index = index + 2 # 5 cells for each subject to parse....**
                    data[keyvalue]['SGPA'] = mdata[index]
                    cgpa = cgpa + int(mdata[index])
                    data[keyvalue]['Credits'] = mdata[index+1]
                    tcredits = tcredits + int(mdata[index+1])
        cgpa = cgpa / len(filelist)
        context = {'data':data, 'rollno':rollno, 'name': name, 'fathername':fathername, 'subjects': subjects,
        'cgpa':cgpa, 'tcredits':tcredits, 'tfail':tfail}

        return render(request, 'info/a_studentMarks.html', context)



    return render(request, 'info/a_studentMarks.html')



@login_required
def index(request):
    if request.user.is_teacher:
        return render(request, 'info/t_homepage.html')
    if request.user.is_student:
        return render(request, 'info/homepage.html')

    if request.user.is_admin:
        return render(request, 'info/a_homepage.html')
    return render(request, 'info/logout.html')


############ Admin adding############################



@login_required
def a_userUploading(request):
    return render(request, 'info/temporary.html')

@admin_only
def userTypePage(request):
    return render(request, "info/a_usertypeUpload.html")

@admin_only
def a_tsUpload(request):
    return render(request, "info/a_teacherStudentUpload.html")
#+======================================================================================#
############ Teacher Views############################

@login_required
def t_clas(request, teacher_id, choice):
    teacher1 = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'info/t_clas.html', {'teacher1': teacher1, 'choice': choice})


@login_required()
def t_student(request, assign_id):
    ass = Assign.objects.get(id=assign_id)
    att_list = []
    for stud in ass.class_id.student_set.all():
        try:
            a = AttendanceTotal.objects.get(student=stud, course=ass.course)
        except AttendanceTotal.DoesNotExist:
            a = AttendanceTotal(student=stud, course=ass.course)
            a.save()
        att_list.append(a)
    return render(request, 'info/t_students.html', {'att_list': att_list})


@login_required()
def t_class_date(request, assign_id):
    now = timezone.now()
    ass = get_object_or_404(Assign, id=assign_id)
    att_list = ass.attendanceclass_set.filter(date__lte=now).order_by('-date')
    return render(request, 'info/t_class_date.html', {'att_list': att_list})


@login_required()
def cancel_class(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    assc.status = 2
    assc.save()
    return HttpResponseRedirect(reverse('t_class_date', args=(assc.assign_id,)))


@login_required()
def t_attendance(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    ass = assc.assign
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
        'assc': assc,
    }
    return render(request, 'info/t_attendance.html', context)


@login_required()
def edit_att(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    cr = assc.assign.course
    att_list = Attendance.objects.filter(attendanceclass=assc, course=cr)
    context = {
        'assc': assc,
        'att_list': att_list,
    }
    return render(request, 'info/t_edit_att.html', context)


@login_required()
def confirm(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    ass = assc.assign
    cr = ass.course
    cl = ass.class_id
    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.HTNo]
        if status == 'present':
            status = 'True'
        else:
            status = 'False'
        if assc.status == 1:
            try:
                a = Attendance.objects.get(course=cr, student=s, date=assc.date, attendanceclass=assc)
                a.status = status
                a.save()
            except Attendance.DoesNotExist:
                a = Attendance(course=cr, student=s, status=status, date=assc.date, attendanceclass=assc)
                a.save()
        else:
            a = Attendance(course=cr, student=s, status=status, date=assc.date, attendanceclass=assc)
            a.save()
            assc.status = 1
            assc.save()

    return HttpResponseRedirect(reverse('t_class_date', args=(ass.id,)))


@login_required()
def t_attendance_detail(request, stud_id, course_id):
    stud = get_object_or_404(Student, HTNo=stud_id)
    cr = get_object_or_404(Course, id=course_id)
    att_list = Attendance.objects.filter(course=cr, student=stud).order_by('date')
    return render(request, 'info/t_att_detail.html', {'att_list': att_list, 'cr': cr})


@login_required()
def change_att(request, att_id):
    a = get_object_or_404(Attendance, id=att_id)
    a.status = not a.status
    a.save()
    return HttpResponseRedirect(reverse('t_attendance_detail', args=(a.student.HTNo, a.course_id)))


@login_required()
def t_extra_class(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
    }
    return render(request, 'info/t_extra_class.html', context)


@login_required()
def e_confirm(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    cr = ass.course
    cl = ass.class_id
    assc = ass.attendanceclass_set.create(status=1, date=request.POST['date'])
    assc.save()

    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.HTNo]
        if status == 'present':
            status = 'True'
        else:
            status = 'False'
        date = request.POST['date']
        a = Attendance(course=cr, student=s, status=status, date=date, attendanceclass=assc)
        a.save()

    return HttpResponseRedirect(reverse('t_clas', args=(ass.teacher_id, 1)))


@login_required()
def t_report(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    sc_list = []
    for stud in ass.class_id.student_set.all():
        a = StudentCourse.objects.get(student=stud, course=ass.course)
        sc_list.append(a)
    return render(request, 'info/t_report.html', {'sc_list': sc_list})





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@login_required()
def timetable(request, class_id):
    asst = AssignTime.objects.filter(assign__class_id=class_id)
    matrix = [['' for i in range(12)] for j in range(6)]

    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(12):
            if j == 0:
                matrix[i][0] = d[0]
                continue
            if j == 4 or j == 8:
                continue
            try:
                a = asst.get(period=time_slots[t][0], day=d[0])
                matrix[i][j] = a.assign.course_id
            except AssignTime.DoesNotExist:
                pass
            t += 1

    context = {'matrix': matrix}
    return render(request, 'info/timetable.html', context)


@allowed_users(allowed_roles=['Teacher'])
@login_required()
def t_timetable(request, teacher_id):
    asst = AssignTime.objects.filter(assign__teacher_id=teacher_id)
    class_matrix = [[True for i in range(12)] for j in range(6)]
    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(12):
            if j == 0:
                class_matrix[i][0] = d[0]
                continue
            if j == 4 or j == 8:
                continue
            try:
                a = asst.get(period=time_slots[t][0], day=d[0])
                class_matrix[i][j] = a
            except AssignTime.DoesNotExist:
                pass
            t += 1

    context = {
        'class_matrix': class_matrix,
    }
    return render(request, 'info/t_timetable.html', context)


@login_required()
def free_teachers(request, asst_id):
    asst = get_object_or_404(AssignTime, id=asst_id)
    ft_list = []
    t_list = Teacher.objects.filter(assign__class_id__id=asst.assign.class_id_id)
    for t in t_list:
        at_list = AssignTime.objects.filter(assign__teacher=t)
        if not any([True if at.period == asst.period and at.day == asst.day else False for at in at_list]):
            ft_list.append(t)

    return render(request, 'info/free_teachers.html', {'ft_list': ft_list})




@login_required()
def marks_list(request, stud_id):
    stud = Student.objects.get(HTNo=stud_id, )
    ass_list = Assign.objects.filter(class_id_id=stud.class_id)
    sc_list = []
    for ass in ass_list:
        try:
            sc = StudentCourse.objects.get(student=stud, course=ass.course)
        except StudentCourse.DoesNotExist:
            sc = StudentCourse(student=stud, course=ass.course)
            sc.save()
            sc.marks_set.create(type='I', name='Mid test 1')
            sc.marks_set.create(type='I', name='Mid test 2')
            sc.marks_set.create(type='S', name='Semester End Exam')
        sc_list.append(sc)

    return render(request, 'info/marks_list.html', {'sc_list': sc_list})


#==================================================================================#
# Teacher Alots marks here...
@allowed_users(allowed_roles=['Teacher'])
@login_required()
def t_marks_list(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    m_list = MarksClass.objects.filter(assign=ass)
    print(m_list[2].name,'888888888888888888888888888888888888888888888888888888888')
    return render(request, 'info/t_marks_list.html', {'m_list': m_list})


@login_required()
def t_marks_entry(request, marks_c_id):
    mc = get_object_or_404(MarksClass, id=marks_c_id)
    ass = mc.assign
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
        'mc': mc,
    }
    return render(request, 'info/t_marks_entry.html', context)


@login_required()
def marks_confirm(request, marks_c_id):
    mc = get_object_or_404(MarksClass, id=marks_c_id)
    print(mc)
    ass = mc.assign
    print("ass value",ass)
    cr = ass.course
    cl = ass.class_id
    print(cr,cl,".......")
    for s in cl.student_set.all():
        print(s,"S value")
        #mark = request.POST[s.HTNo]
        mark = Student.objects.get(name = s).pk

        print(mark)
        try:
            sc = StudentCourse.objects.get(course=cr, student=s)
            print(sc,"SC Value...")
            print(mc.name)
            m = sc.marks_set.get(name=mc.name)
            m.marks1 = mark
            print(m)
            m.save()
        except StudentCourse.DoesNotExist:
            sc = None
    mc.status = True
    mc.save()

    return HttpResponseRedirect(reverse('t_marks_list', args=(ass.id,)))


