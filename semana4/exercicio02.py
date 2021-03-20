from datetime import datetime, timedelta


def twoweek():
    data = datetime.today() + timedelta(days=17)
    return f'O dia será {data.day} do {data.month} de {data.year}'


if __name__ == '__main__':
    print(twoweek())
