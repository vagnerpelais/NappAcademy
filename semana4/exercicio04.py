from datetime import datetime


def defeatday(data):
    shameday = datetime.today() - data
    return f'Faz {shameday.days} dias que passamos vergonha na copa'


if __name__ == '__main__':
    defeat = datetime(year=2014, month=7, day=8)
    print(defeatday(defeat))
