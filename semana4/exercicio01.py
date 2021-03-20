from datetime import datetime


def lyfedays(date):
    life = datetime.today() - date
    return f'Você nasceu em {date.year} e tem {life.days} dias de vida'


if __name__ == '__main__':
    today = datetime(1998, 3, 7)
    print(lyfedays(today))
