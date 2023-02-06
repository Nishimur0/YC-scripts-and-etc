from datetime import datetime
from datetime import timedelta
dateFormatter = "%Y-%m-%d"

print("Используй запрос SQL: ")
print("select concat(salon_id,', ', service_id,', ', id) from salons_services_link where service_id in() and deleted = 0 ")
num_rows = int(input("Сколько строк вернул запрос? "))
print("результаты запроса ")
list_of_services = [input().split(',') for i in range(num_rows)]

start = datetime.strptime(str(input('Дата начала (включительно): ')), dateFormatter)
end = datetime.strptime(str(input('Дата окончания(не включительно): ')), dateFormatter)

list_of_dates = []
exceptions = []
temp = ''

print('Введи даты исключения в формате г-м-д \n  Если исключения все введены, введи Y или y \n')
while temp != 'Y' or temp != 'y' and temp != 'н' and temp != 'Н' :
    temp = str(input())
    if temp != 'Y' and temp != 'y' and temp != 'н' and temp != 'Н' :
        exceptions.append(str(datetime.strptime(temp, '%Y-%m-%d')))
    else:
        break

for x in range(0, (end - start).days):
    day = str((start + timedelta(days=x)).strftime('%Y-%m-%d'))
    if str(datetime.strptime(day, '%Y-%m-%d')) not in exceptions:
        list_of_dates.append((start + timedelta(days=x)).strftime('%Y-%m-%d'))
    else:
        continue

data = len(list_of_dates)

with open('service_schedule.sql', 'w') as f:
    print("insert into services_link_schedule (id, salon_id, service_id, salon_service_id, date)", file=f)
    print("values", file=f)
    for i in range(len(list_of_services)):
        for j in range(len(list_of_dates)):
            if (i == num_rows-1) and (j == data-1):
                print('(null, ',list_of_services[i][0],', ', list_of_services[i][1],', ', list_of_services[i][2], ', ',"'",list_of_dates[j],"'",');', sep='', file=f)
            else:
                print('(null, ',list_of_services[i][0],', ', list_of_services[i][1],', ', list_of_services[i][2], ', ',"'",list_of_dates[j],"'",'),', sep='', file=f)
salon_service_links = []
for i in range (len(list_of_services)):
    salon_service_links.append(list_of_services[i][2])
with open('update services.sql', 'w') as updates:
    print(F"update salons_services_link set schedule_template = 3, date_from = '{start.strftime('%Y-%m-%d')}', date_to = '{end.strftime('%Y-%m-%d')}' where id in \n(", end='', file=updates)
    print(*salon_service_links, sep=',\n', end = '', file = updates)
    print(");", file = updates)

