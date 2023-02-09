values = []
feature_id = int(input('Фича ID: '))
param_group = int(input('стартовое значение param_group: '))
name = str(input('Имя param_group: '))
inp = ''
print('Введи список филиалов. Каждый с новой строки: ')
while inp != 'y' and inp != 'Y' and inp != 'Н' and inp != 'н':
    inp = input()
    if inp != 'y' and inp != 'Y' and inp != 'Н' and inp != 'н':
        values.append(int(inp))
    else:
        break
with open('new feature.sql', 'w') as new:
    print('insert into version_control_feature_params (id, version_control_feature_id, param_group, name, value) \nvalues', file = new)
    for i in range(len(values)):

        if i == len(values)-1:
            print(
                F"(null, {feature_id}, {param_group}, '{name}', {values[i]});", file=new)
        else:
            print(
                F"(null, {feature_id}, {param_group}, '{name}', {values[i]}),", file=new)
        param_group += 1