from datetime import datetime

from django.urls import get_mod_func
class GoFood:

    menu = {'pizza': 150, 'burger':100, 'coke':50, 'brownies': 60}
    delivery_charges = {'Peak hour': 30, 'Special Days': 50, 'Night Charges': 20, 'default_charge': 20}
    get_month = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    peakhour = [11, 12, 13, 14, 18, 19]
    sepcialday = {'Jan':None, 'Feb':None, 'Mar':None, 'Apr':None, 'May':None, 'Jun':None, 'Jul':None, 'Aug':None, 'Sep':None, 
                'Oct':None, 'Nov':[4], 'Dec':[9, 25]}
    night_hours = [21, 22, 23, 0, 1, 2, 3]


    def applying_delivery_charges(self, conditions):


        timepoint = datetime.now()
        date_and_time = str(timepoint).split()

        month = date_and_time[0][6:8]
        day   = date_and_time[0][8:]
        hour  = date_and_time[1][:2]

        is_peakHour   = int(hour) in self.peakhour
        if is_peakHour:
            delivery_bill += self.delivery_charges['Peak hour']

        is_sepcialDay = day in self.sepcialday[self.get_month[int(month)]]
        if is_sepcialDay:
            delivery_bill += self.delivery_charges['Special Day']

        is_night      = int(hour) in self.night_hours
        if is_night:
            delivery_bill += self.delivery_charges['Night Charges']

        is_normal = True in (is_peakHour, is_sepcialDay, is_night)
        if is_normal:
            delivery_bill += self.delivery_charges['default_charge']



        # delivery_bill = 0
        # for condition, response in conditions:
        #     if response.lower() == 'yes':
        #         delivery_bill += self.delivery_charges[condition]
        
        # delivery_bill += self.delivery_charges['default']

        return delivery_bill



    def order(self, items, conditions):
        bill_value = 0

        for item in items:
            bill_value += self.menu[item.lower()]
        
        bill_value += self.applying_delivery_charges(conditions)

        return bill_value

