function allLetter(inputtxt)
{
    var letters = /^[A-Za-z]+$/;
    if(inputtxt.value.match(letters))
        {
        return true;
        }
    else
        {
        alert("message");
        return false;
        }
}

// function validateForm(x, y, z) 
// {
//     var letters = /^[A-Za-z]+$/;
//     var rollnum = /^\d{2}[A-Z][A-Z][A-Z][A-Z]\d{2}$/;
//     var marks = /^[0-1]\d{2}$/;
//     let student_mark = document.getElementById('marks').value;
//     if(x.value.match(letters))
//     {
//             if (y.value.match(rollnum))
//         {
//                 if (z.value.match(marks))
//                 {
//                     /*if (student_mark > 100)
//                     {
//                         alert("Marks is > 100");
//                         return false;
//                     }
//                     else
//                     {
//                         return true;
//                     }*/
//                     return true;
//                 }
//                 else
//                 {
//                     alert("Marks Format is not right");
//                     return false;
//                 }	
//         }
//         else
//         {
//             alert("Roll number should be in NumberCODENumber Format");
//             return false;
//         }
//     }
//     else
//     {
//             alert("Name should be character");
//             return false;
//     }
// }

function validatename() {
    var name = document.myForm.name.value;
    document.write(name);

    if (name==null || name==""){  
        alert("Name can't be blank");  
        return false; 
    }
    else if(! s.matches("[a-zA-Z]+")){
        System.out.println("Name only contains letters");
    }
    else{
        alert("Name only contains the letters");
    }
}

function validaterollno(rollno){

}
function validate 