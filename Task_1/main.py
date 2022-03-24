from pprint import pprint
from data import *

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;


def people(list_of_libraries, request):
    result = ''
    for i in list_of_libraries:
        if request == i['number']:
            result =  i['name']
    if result == '':
        result = 'Нет такого номера документа'
    return result

def shelf(shelfs_id, request):
    result = ''
    for key, value in shelfs_id.items():
        if request in value:
            result = key
    if result == '':
        result = 'Нет такого номера документа'
    return result

def lists(list_of_libraries):
    print()
    for i in list_of_libraries:
        qwer = i.values()
        print(', '.join(qwer))

def adds(list_of_libraries, shelfs_id, document_type, document_number, document_owner, shelf_number):
    if shelf_number in shelfs_id.keys():
        dictonary = {"type": document_type, "number": document_number, "name": document_owner}
        list_of_libraries.append(dictonary)
        shelfs_id[shelf_number].append(document_number)
    else:
        print('Такой полки нет')
    return list_of_libraries, shelfs_id

def delete(list_of_libraries, shelfs_id, request):
    result = ''
    for key, value in shelfs_id.items():
        if request in value:
            result = key
            index = value.index(request)
            del (value[index])

    for index, i in enumerate(list_of_libraries):
        if request == i['number']:
            del (list_of_libraries[index])
    if result == '':
        print('Нет такого номера документа')
    return list_of_libraries, shelfs_id

def move(shelfs_id):
    request = input('Введите номер документа ')
    result = True
    for key, value in shelfs_id.items():
        if request in value:
            move_to = input('Введите номер полки куда хотите переместить ')
            result = False
            if move_to in shelfs_id.keys():
                shelfs_id[move_to].append(request)
                index = value.index(request)
                del (value[index])
                break
            else:
                print('Нет такой полки')
    if result == True:
        print('Нет такого номера документа')
    return shelfs_id

def add_shelf(shelfs_id):
    request = input('Введите номер полки ')
    shelfs_id.setdefault(request, [])

def main(list_of_libraries, shelfs_id):
    while True:
        what_to_do = input(
            '\np – спросит номер документа и выведет имя человека, кот. принадлежит; \ns – спросит номер документа и выведет номер полки, на кот. находится; \nl – выведет список всех документов \na - добавит новый документ в каталог \nВведите обозначение операции символом: \nd - delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. \nm - move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. \nas – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.  \nq - выход \nВведите операцию: ')
        if what_to_do == 'p':
            request = input('Введите номер документа ')
            print(people(list_of_libraries, request))

        elif what_to_do == 's':
            request = input('Введите номер документа ')
            shelf(shelfs_id, request)

        elif what_to_do == 'l':
            lists(list_of_libraries)

        elif what_to_do == 'a':
            document_type = input('Введите тип документа ')
            document_number = input('Введите номер документа ')
            document_owner = input('Введите имя, фамилию владельца ')
            shelf_number = input('Введите номер полки, на которой будет храниться документ ')
            adds(list_of_libraries, shelfs_id, document_type, document_number, document_owner, shelf_number)
            pprint(list_of_libraries)
            pprint(shelfs_id)

        elif what_to_do == 'd':
            request = input('Введите номер документа ')
            delete(list_of_libraries, shelfs_id, request)


        elif what_to_do == 'm':
            move(shelfs_id)

        elif what_to_do == 'as':
            add_shelf(shelfs_id)

        elif what_to_do == 'q':
            break

if __name__ == '__main__':
    main(documents, directories)
