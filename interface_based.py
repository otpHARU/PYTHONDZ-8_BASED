import crud_based as cr
import logger_based as lg

print('\nВас приветствует информационная система сотрудников компании DODO!')

def ls_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать всех сотрудников.')
        print('2. Найти сотрудника по фамилии.')
        print('3. Найти сотрудника по имени.')
        print('4. Найти сотрудника по номеру телефона.')
        print('5. Добавить нового сотрудника.')
        print('6. Обновить данные действующего сотрудника.')
        print('7. Удалить запись о сотруднике.')
        print('8. Закрыть программу.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            lg.logging.info('The user has selected item number 1')
            print(cr.retrive())

        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            search = input('Введите фамилию: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(surname=search))

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            search = input('Введите имя: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(name=search))

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            search = input('Введите номер  телефона: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(number=search))

        elif n == 5:
            lg.logging.info('The user has selected item number 5')
            name = input('Введите имя: ')
            lg.logging.info('User entered: {name}')
            surname = input('Введите фамилию: ')
            lg.logging.info('User entered: {surname}')
            number = input('Введите номер телефона: ')
            lg.logging.info('User entered: {number}')
            email = input('Введите электронную почту: ')
            lg.logging.info('User entered: {email}')
            cr.create(name, surname, number, email)
            print('Данные о сотруднике занесены в систему!')

        elif n == 6:
            lg.logging.info('The user has selected item number 6')
            print('1. Найти сотрудника по фамилии.')
            print('2. Найти сотрудника по имени.')
            print('3. Найти сотрудника по номеру телефона.')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                lg.logging.info('The user has selected item number 6.1')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(surname=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                print('Какую информацию требуется обновить?')
                print('1. Обновить фамилию.')
                print('2. Обновить имя.')
                print('3. Обновить номер телефона.')
                change = сhecking_the_number(input('Введите номер пункта: '))
                if change == 1:
                    lg.logging.info('The user has selected item number 6.1.1')
                    new_surname = input('Введите новую фамилию: ')
                    lg.logging.info('User entered: {new_surname}')
                    cr.update(id=user_id, new_surname=new_surname)
                    print('Данные о сотруднике успешно изменены!')
                elif change == 2:
                    lg.logging.info('The user has selected item number 6.1.2')
                    new_name = input('Введите новое имя: ')
                    lg.logging.info('User entered: {new_name}')
                    cr.update(id=user_id, new_name=new_name)
                    print('Данные о сотруднике успешно изменены!')
                elif change == 3:
                    lg.logging.info('The user has selected item number 6.1.3')
                    new_number = input('Введите новый номер телефона: ')
                    lg.logging.info('User entered: {new_number}')
                    cr.update(id=user_id, new_number=new_number)
                    print('Данные о сотруднике успешно изменены!')
                else:
                     lg.logging.info('User entered an invalid menu value')
                     print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

            elif change == 2:
                lg.logging.info('The user has selected item number 6.2')
                search = input('Введите имя: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(name=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                print('Какую информацию требуется обновить?')
                print('1. Обновить фамилию.')
                print('2. Обновить имя.')
                print('3. Обновить номер телефона.')
                change = сhecking_the_number(input('Введите номер пункта: '))
                if change == 1:
                    lg.logging.info('The user has selected item number 6.2.1')
                    new_surname = input('Введите новую фамилию: ')
                    lg.logging.info('User entered: {new_surname}')
                    cr.update(id=user_id, new_surname=new_surname)
                    print('Данные о сотруднике успешно изменены!')
                elif change == 2:
                    lg.logging.info('The user has selected item number 6.2.2')
                    new_name = input('Введите новое имя: ')
                    lg.logging.info('User entered: {new_name}')
                    cr.update(id=user_id, new_name=new_name)
                    print('Данные о сотруднике успешно изменены!')
                elif change == 3:
                    lg.logging.info('The user has selected item number 6.2.3')
                    new_number = input('Введите новый номер телефона: ')
                    lg.logging.info('User entered: {new_number}')
                    cr.update(id=user_id, new_number=new_number)
                    print('Данные о сотруднике успешно изменены!')
                else:
                     lg.logging.info('User entered an invalid menu value')
                     print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

            elif change == 3:
                lg.logging.info('The user has selected item number 6.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(number=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                print('Какую информацию требуется обновить?')
                print('1. Обновить фамилию.')
                print('2. Обновить имя.')
                print('3. Обновить номер телефона.')
                change = сhecking_the_number(input('Введите номер пункта: '))
                if change == 1:
                    lg.logging.info('The user has selected item number 6.3.1')
                    new_surname = input('Введите новую фамилию: ')
                    lg.logging.info('User entered: {new_surname}')
                    cr.update(id=user_id, new_surname=new_surname)
                    print('Данные о сотруднике успешно изменены!')
                elif change == 2:
                    lg.logging.info('The user has selected item number 6.3.2')
                    new_name = input('Введите новое имя: ')
                    lg.logging.info('User entered: {new_name}')
                    cr.update(id=user_id, new_name=new_name)
                    print('Данные о сотруднике успешно изменены!')
                elif change == 3:
                    lg.logging.info('The user has selected item number 6.3.3')
                    new_number = input('Введите новый номер телефона: ')
                    lg.logging.info('User entered: {new_number}')
                    cr.update(id=user_id, new_number=new_number)
                    print('Данные о сотруднике успешно изменены!')
                else:
                     lg.logging.info('User entered an invalid menu value')
                     print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 7:
            lg.logging.info('The user has selected item number 7')
            print('1. Найти сотрудника по по фамилии.')
            print('2. Найти сотрудника по по имени.')
            print('3. Найти сотрудника по номеру телефона.')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 7.1')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(surname=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 7.2')
                search = input('Введите имя: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(name=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('The user has selected item number 7.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(number=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
            lg.logging.info('End')
            print('Спасибо за проделанную работу!')
            break

        else:
            lg.logging.info('User entered an invalid menu value: {n}')
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('User entered an invalid menu value: {arg}')
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)