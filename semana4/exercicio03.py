from datetime import datetime


def idade(birth):
    today = datetime.today()
    if birth >= today:
        years = today.year - birth.year
        return f'Você nasceu em {birth.year} e tem {years} anos de idade'
    else:
        years = today.year - birth.year
        years -= 1
        return f'Você nasceu em {birth.year} e tem {years} anos de idade'


if __name__ == '__main__':
    birthdate = datetime(1998, 3, 7)
    print(idade(birthdate))
