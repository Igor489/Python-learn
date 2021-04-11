source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

my_list = []
for element in source_list:
    if element.isdigit():
        my_list.extend(['"', f'{int(element):02}', '"'])
    elif (element[0] == '+' or element[0] == '-') and element[1:].isdigit():
        sign = element[0]
        my_list.extend(['"', sign + f'{int(element[1:]):02}', '"'])
    else:
        my_list.append(element)

result = ' '.join(my_list)
print(result)
