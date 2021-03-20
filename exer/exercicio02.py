from massa_dados import list_spend_money


def spend_by_gender(gender):
     for item in list_spend_money:
             if item[-2] == gender.upper():
                     print(item)


def sum_by_gender(gender):
     sum = 0
     for item in list_spend_money:
             if item[-2] == gender.upper():
                     if item[-1] == '':
                             sum += 0
                     else:
                             sum += float(item[-1])
     return round(sum, 2)


if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total ĂŠ: ')
    print(sum_by_gender(gender))
