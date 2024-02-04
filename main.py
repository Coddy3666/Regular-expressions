from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# Разносим ФИО по столбцам:
contacts_list_finished = list()
for row in contacts_list:
    new_row = ' '.join(row[:3]).split(' ')
    res = [new_row[0], new_row[1], new_row[2], row[3], row[4], row[5], row[6]]
    contacts_list_finished.append(res)


# Номер телефона по образцу:
pattern_num1 = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[-\s]+(\d+)[-\s]+(\d+)"
new_pattern_num1 = r"+7(\2)\3-\4-\5"

pattern_num2 = r"(\+7)(\d{3})(\d{3})(\d{2})(\d{2})"
new_pattern_num2 = r"+7(\2)\3-\4-\5"

pattern_num3 = r"8{1}\s*(\d+)\W?(\d+)\W?(\d{2})(\d{2})"
new_pattern_num3 = r"+7(\1)\2-\3-\4"

pattern_add_num = r"(\()?(доб\.)\s*(\d+)(\))?"
new_pattern_add_num = r"доб.\3"

new_contacts_list = list()
for rows in contacts_list_finished:
    new_row = ','.join(rows)
    format_row_num1 = re.sub(pattern_num1, new_pattern_num1, new_row)
    format_row_num2 = re.sub(pattern_num2, new_pattern_num2, format_row_num1)
    format_row_num3 = re.sub(pattern_num3, new_pattern_num3, format_row_num2)
    format_row_num_add = re.sub(pattern_add_num, new_pattern_add_num, format_row_num1)
    new_contacts_list.append(format_row_num_add)


# Объединение повторяющихся имён:
for row in contacts_list_finished:
    lastname1 = row[0]
    firstname1 = row[1]
    for row2 in contacts_list_finished:
        lastname2 = row2[0]
        firstname2 = row2[1]
        if lastname1 == lastname2 and firstname1 == firstname2:
            if row[2] == '':
                row[2] = row2[2]
            if row[3] == '':
                row[3] = row2[3]
            if row[4] == '':
                row[4] = row2[4]
            if row[5] == '':
                row[5] = row2[5]
            if row[6] == '':
                row[6] = row2[6]

result = list()
for row in contacts_list_finished:
    if row not in result:
        result.append(row)
pprint(result)

# Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)
