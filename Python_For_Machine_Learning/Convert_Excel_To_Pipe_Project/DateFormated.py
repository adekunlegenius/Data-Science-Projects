from datetime import *


class DateFormated:

    def __init__(self, date_string):
        self.date_string = date_string
        self.date_Obj = date.fromisoformat(date_string)

    def get_month_number(self):
        return self.date_Obj.month

    def get_year_number(self):
        return self.date_Obj.year

    def get_day_number(self):
        return self.date_Obj.day

    def get_month_first_three_char(self):
        month_number = self.get_month_number()
        if month_number == 1:
            return 'Jan'
        elif month_number == 2:
            return 'Feb'
        elif month_number == 3:
            return 'Mar'
        elif month_number == 4:
            return 'Apr'
        elif month_number == 5:
            return 'May'
        elif month_number == 6:
            return 'Jun'
        elif month_number == 7:
            return 'Jul'
        elif month_number == 8:
            return 'Aug'
        elif month_number == 9:
            return 'Sep'
        elif month_number == 10:
            return 'Oct'
        elif month_number == 11:
            return 'Nov'
        else:
            return 'Dec'

    def get_month_last_day(self):
        month_number = self.get_month_number()
        if month_number == 1:
            return 31
        elif month_number == 2:
            return 29
        elif month_number == 3:
            return 31
        elif month_number == 4:
            return 30
        elif month_number == 5:
            return 31
        elif month_number == 6:
            return 30
        elif month_number == 7:
            return 31
        elif month_number == 8:
            return 31
        elif month_number == 9:
            return 30
        elif month_number == 10:
            return 31
        elif month_number == 11:
            return 30
        else:
            return 31

    def get_date_string_with_last_day(self, sep=''):
        last_day_date_string= ""
        last_day_date_string = str(self.get_year_number()) + sep + self.get_month_first_three_char() + sep + str(self.get_month_last_day())
        return last_day_date_string

    