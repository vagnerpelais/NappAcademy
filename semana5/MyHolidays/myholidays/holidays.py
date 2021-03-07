from datetime import date
from datetime import datetime
from dateutil.parser import parse


class MyCalendar:

    def __init__(self, *args):
        self.datas = []
        self.check_holiday()

        for item in args:
            if isinstance(item, date):
                self.datas.append(item)
            elif type(item) == str:
                if len(str(item).split('/')) > 2:
                    if int(str(item).split('/')[1]) > 12 or len(str(item).split('/')[0]) > 2:
                        continue
                    self.datas.append(parse(item).date())
                else:
                    pass

        # self.datas = [parse(str(item)) for item in args if type(item) not in types and len(str(item).split('/')) > 2]

    def check_holiday(self, *args):
        check_day = []
        for data in args:
            print(data)
            if len(str(data).split('/')[0]) > 2:
                check_day.append('invalido')
                continue
            if isinstance(data, date):
                check_day.append(data)
            elif type(data) == str:
                if int(str(data).split('/')[1]) > 12 or len(str(data)) <= 5:
                    check_day.append('invalido')
                else:
                    check_day.append(parse(data))
            else:
                pass

        for day in check_day:
            print(day)
            if day == 'invalido':
                return False
            if day.weekday() == 6 or day.weekday() == 5:
                return True
            else:
                return False


    def add_holiday(self, *args):
        for item in args:
            if type(item) == str:
                if int(str(item).split('/')[1]) > 12 or len(str(item).split('/')[0]) >= 3:
                    continue
            if parse(str(item)).date() in self.datas:
                pass
            elif isinstance(item, date):
                self.datas.append(item)
            elif type(item) == str:
                self.datas.append(parse(item))


if __name__ == '__main__':
    dt1 = '15/15/2021'
    dt2 = '120/3/2021'
    dt3 = '15/03/2021'
    dt4 = '15/05'
    dt5 = '24/24/2021'
    objeto = MyCalendar(dt1, dt2)
    assert objeto.check_holiday(dt1) is False
    assert objeto.check_holiday(dt2) is False
    assert objeto.check_holiday(dt3) is False
    assert objeto.check_holiday(dt4) is False
    assert objeto.check_holiday(dt5) is False
