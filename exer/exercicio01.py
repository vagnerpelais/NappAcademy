from massa_dados import list_spend_money


def spend_by_login(login):
     for item in list_spend_money:
             if item[1] == login:
                     print(item)


def sum_by_login(login):
     sum = 0
     for item in list_spend_money:
             if item[1] == login:
                     if item[-1] == '':
                             sum += 0
                     else:
                             sum += float(item[-1])
     return round(sum, 2)


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login)
    print('A soma total ĂŠ: ')
    print(sum_by_login(login))
