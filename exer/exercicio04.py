from massa_dados import list_spend_money


def spend_by_login(login, limit=1000):
     for item in list_spend_money:
             if item[1] == login and item[-1] == '':
                     pass
             elif item[1] == login and float(item[-1]) <= limit:
                     print(item)
             else:
                     pass


def sum_by_login(login, limit=1000):
     sum = 0
     for item in list_spend_money:
             if item[1] == login and item[-1] == '':
                     pass
             elif item[1] == login and float(item[-1]) <= limit:
                     sum += float(item[-1])
             else:
                     pass
     return round(sum, 2)


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)
    print('A soma total atĂŠ 600: ')
    print(sum_by_login(login))
    print('A soma total atĂŠ 1200: ')
    print(sum_by_login(login, 1200))
