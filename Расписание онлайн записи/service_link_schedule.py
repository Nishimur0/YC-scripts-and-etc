from datetime import datetime
from datetime import date
from datetime import timedelta
import re
dateFormatter = "%Y-%m-%d"
format_time = re.compile(r"^((0?[0-9])|(1[0-9])|(2[0-4]))(:)([0-5][05])$") #задал формат времени допустимый для ввода
format_date = re.compile(r"^[0-9]{4}(-)[0-9]{2}(-)[0-9]{2}$") #задал формат даты допустимый для воода

print("Используй запрос SQL: ")
print("select concat(salon_id,', ', service_id,', ', id) from salons_services_link where service_id in() and deleted = 0 ")
num_rows = int(input("Сколько строк вернул запрос? ")) #Решил сделать через цикл for, для большего контроля человеком
print("результаты запроса ")
list_of_services = [input().split(',') for i in range(num_rows)] #Добавляю результаты запроса в список


#Дни недели добавляемые в исключения.
print('Введи дни недели, которых не должно быть через запятую (0 = понедельник, 6 = воскресение)')
weekdays = re.split(', | ,| , | |  ', input())

#Забиваю даты начала и поиска сеансов.
# (Надо будет это переделать тоже с строгим форматом через re и убрать лишние преобразования)
start = datetime.strptime(str(input('Дата начала (включительно) в формате гггг-мм-дд: ')), dateFormatter)
end = datetime.strptime(str(input('Дата окончания(не включительно)в формате гггг-мм-дд: ')), dateFormatter)

#Забиваю ввод времени начала поиска сеансов и преобразовываю в минуты
while True:
    time_start = input('Введи время начала поиска сеансов в 24 часовом формате\nКратный 5 минутам\nНапример 13:30: ')
    if format_time.match(time_start):
        hours_st, minutes_st = [int(x) for x in time_start.split(':')]
        minutes_start = (((int(hours_st) * int(60)) + int(minutes_st))*int(60))
        break
    print('Неправильный формат времени. \nПопробуй ввести время в формате чч:мм\nкратно 5 минутам')

#Забиваю ввод времени окончания поиска сеансов и преобразовываю в минуты
while True:
    time_finish = input('Введи время окончания поиска сеансов в 24 часовом формате\nКратный 5 минутам\nНапример 13:30: ')
    if format_time.match(time_finish):
        hours_fin, minutes_fin = [int(x) for x in time_finish.split(':')]
        minutes_finish = (((int(hours_fin) * int(60)) + int(minutes_fin))*int(60))
        break
    print('Неправильный формат времени. \nПопробуй ввести время в формате чч:мм\nкратно 5 минутам')

#Добавляем конкретные даты, которые необходимо исключить. (Надо переформатировать в месяц и день только.)
exceptions = []
print('Введи даты исключения в формате гггг-мм-дд \n  Если исключения все введены, введи Y или y \n')
while True :
    temp = str(input())
    if temp.lower() not in ('y','н'):
        exceptions.append(str(datetime.strptime(temp, '%Y-%m-%d')))
    else:
        break

list_of_dates = []
for x in range(0, (end - start).days):
    day = str((start + timedelta(days=x)).strftime('%Y-%m-%d'))
    if str(datetime.strptime(day, '%Y-%m-%d')) not in exceptions and str(datetime.strptime(day, '%Y-%m-%d').weekday()) not in weekdays:
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
    print(F"update salons_services_link set schedule_template = 3, date_from = '{start.strftime('%Y-%m-%d')}', "
          F" date_to = '{end.strftime('%Y-%m-%d')}', seance_search_start = {minutes_start}, "
          F"seance_search_finish = {minutes_finish} "
          F" where id in \n(", end='', file=updates)
    print(*salon_service_links, sep=',\n', end = '', file = updates)
    print(");", file = updates)
