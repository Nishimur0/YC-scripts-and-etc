lines = []
print('Введи запрос')
print('включая in для update\'ов')
main_line = input()

print('Введи строки для разбивки')
print('Каждая строка с новой строки\n(для in ( ) запятые не обязательны)\nзначения (полностью в скобках)'
      '\nКогда все строки введены, введи y')
while True:
    temp = input().rstrip(',;')
    if temp.lower() in ('y', 'н'):
        break
    lines.append(temp)


def del_or_upd_query(x):
    with open('queries.sql', 'a') as f:
        counter = 0
        for i in range(0, len(x)):
            if counter == 0 or i == 0:
                print(main_line, file=f)
                print(f'(\n{x[i]}', file=f)
                counter += 1
            elif counter == 5000 and counter != len(x) - 1:
                print(f'{x[i]}\n);', file=f)
                print(main_line, file=f)
                print('(', file=f)
                counter = 1
            elif counter == len(x) - 1:
                print(f'{x[i]}\n);', file=f)
                counter = 0
            elif i == len(x)-1:
                print(f'{x[i]}\n);', file=f)
            else:
                print(f'{x[i]},', file=f)
                counter += 1



def insert_query(x):
    with open('queries.sql', 'a') as f:
        counter = 0
        for i in range(0, len(x)):
            if counter == 0 or i == 0:
                print(main_line, file=f)
                print(f'VALUES\n{x[i]},', file=f)
                counter += 1
            elif counter == 5000 and counter != len(x) - 1:
                print(f'{x[i]}\n;', file=f)
                print(f'{main_line}\nVALUES', file=f)

                counter = 1
            elif counter == len(x) - 1:
                print(f'{x[i]};', file=f)
                counter = 0
            elif i == len(x)-1:
                print(f'{x[i]};', file=f)
            else:
                print(f'{x[i]},', file=f)
                counter += 1


queries = {1: del_or_upd_query, 2: insert_query}

print('Укажи тип запроса:')
print('1 = delete или update')
print('2 = insert')
type_of_query = int(input())

if type_of_query in (1, 2):
    queries[type_of_query](lines)