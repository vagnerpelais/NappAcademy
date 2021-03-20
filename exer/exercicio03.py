from massa_dados import list_spend_money


def spend_by_subname(name):
     for item in list_spend_money:
             if name in item[0]:
                     print(item)


def sum_by_subname(name):
     sum = 0
     for item in list_spend_money:
             if name in item[0]:
                     if item[-1] == '':
                             sum += 0
                     else:
                             sum += float(item[-1])
     return round(sum, 2)


if __name__ == "__main__":
    name = 'Brown'
    spend_by_subname(name)
    print('A soma total Ã©: ')
    print(sum_by_subname(name))
