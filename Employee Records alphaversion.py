#used dictionary to define mulitiple employees
Employee = {}


#created Admin menu with all options - created by Sylwia Jablonska
def main_menu():
    print('#'*40)
    print('1) Add Record\n2) Modify\n3) List\n4) Search\n5) Delete\n6) Exit\n7) Switch User')
    print('#'*40)


#created User menu with limited options - created by Sylwia Jablonska
def user_menu():
    print('#'*40)
    print('1) Add Record\n2) List\n3) Exit\n4) Switch User')
    print('#'*40)


#created by Alexandre De Menezes
#adding record is possible with id (new structure within Employee dictionary) - each value from list is same as in Employee records function
def add_record(id, fname, sname, date, position, department, salary, contNumber, email):  
    Employee[id] = {
        'First': fname,
        'Surname': sname,
        'Started': date,
        'Position': position,
        'Department': department,
        'Salary': salary,
        'Contact': contNumber,
        'Email': email, 

    }
    print('>>>> Employee {} created successfully.'.format(id))
    save()

#differences from add_record - elif statement and conditions. Created by Alexnadre De Menezes
def modify(id, fname, sname, date, position, department, salary, contNumber, email):  
    Employee[id] = {
        'First': fname,
        'Surname': sname,
        'Started': date,
        'Position': position,
        'Department': department,
        'Salary': salary,
        'Contact': contNumber,
        'Email': email, 

    }
    print('>>>> Employee {} modified  successfully.'.format(id))
    save()

#displaying all availible definded ID dictonary within Employee dictionary - created by Marcel Piotrowski
def list():
    print('--------------------------------------------')  
    if Employee:
        for id in Employee:
           search(id)
    else:
        print('>>>> Dont have any Employees yet.')

#created by Alexandre De Menezes
def employee_details(): 
       fname = input('Please enter the First Name: ')
       sname = input('Please enter the Surname: ')
       date  = input('Please enter the Started Date: ')
       position = input('Please enter the Position: ')
       department = input('Please enter the Department: ')
       salary = input('Please enter the Salary: ')
       contNumber = input('Please enter the Contact Number: ')
       email = input('Please enter the Email Address: ')
       return fname, sname, date, position, department, salary, contNumber, email


#created by Alexandre De Menezes
def delete(id):
    try:
        Employee.pop(id)
        print('--------------------------------------------')
        print('>>>> Employee {} deleted successfully'.format(id))
        print('--------------------------------------------')
        save()
    except :
        print('>>>> Employee does not exist')


#created by Marcel Piotrowski
def search(id):
    try:
        print('Employee ID:', id)
        print('First Name:', Employee[id]['First'])
        print('Surname:', Employee[id]['Surname'])
        print('Started Date:', Employee[id]['Started'])
        print('Position:', Employee[id]['Position'])
        print('Department:', Employee[id]['Department'])
        print('Salary:', Employee[id]['Salary'])
        print('Contact Number:', Employee[id]['Contact'])
        print('Email Address:', Employee[id]['Email'])

        print('--------------------------------------------')
    except:
        print('>>>> Employee does not exist.')



#created by Alexandre De Menezes
def save(): 
        try:
            with open('database.csv', 'w') as file:
                for id in Employee:
                    fname = Employee[id]['First']
                    sname = Employee[id]['Surname']
                    date = Employee[id]['Started']
                    position = Employee[id]['Position']
                    department = Employee[id]['Department']
                    salary =  Employee[id]['Salary']
                    contNumber = Employee[id]['Contact']
                    email = Employee[id]['Email']
                    file.write("{},{},{},{},{},{},{},{},{}\n".format(id, fname, sname, date,
                                                                  position, department, salary, contNumber, email))#makes each variable have bracket
        except :
            print('>>>> An error occurred')
            
#created by Marcel Piotrowski
def load(): 
    try:
        with open('database.csv', 'r') as file:
            lines = file.readlines() #returns a list containing each line in the file as a list item. 
            for line in lines:
                detail = line.strip().split(',') #string gets a list based in the delimiter that you specified

                id = detail[0]
                fname = detail[1]
                sname = detail[2]
                date = detail[3]
                position = detail[4]
                department = detail[5]
                salary = detail[6]
                contNumber = detail[7]
                email = detail[8]
                

                Employee[id] = {
                    'First': fname,
                    'Surname': sname,
                    'Started': date,
                    'Position': position,
                    'Department': department,
                    'Salary': salary,
                    'Contact': contNumber,
                    'Email': email,
                }
    except :
        pass

#passwords for both accounts 
user = 'user' 
password = 'user'

superUser = 'admin'
superPass = 'root'

loop = 0


#created by all
while True: 
    load()
    print('#'*40)
    print('>>>>> Welcome to Employee data base. \nCreated by AMS Developers. <<<<<<<')
    print('#' * 40)
    checkUser = input('Please enter with your user to sign in: ')
    checkpass = input('Please enter with your password: ')
    if checkUser == user and checkpass == password:
        while True:
            user_menu()
            try:
                menu = input(str('Please enter your option: '))
                menu = menu.capitalize()
            except:
                print('Please enter a correct option.')
                continue
            if menu == '1' or menu == 'Add record':
                id = input('Please enter the Unique ID number: ')
                try:
                    Employee[id]
                    print('This Id number is already in use, please try again.')
                except KeyError: #user ID is unique thanks to KeyError function
                    fname, sname, date, position, department, salary, contNumber, email = employee_details()
                    add_record(id, fname, sname, date, position, department, salary, contNumber, email)

            elif menu == '2' or menu == 'List':
                list()
            elif menu == '3' or menu == 'Exit':
                print('-' * 30)
                print('Closing the program.')
                print('-' * 30)
                raise SystemExit

            elif menu == '4' or menu == 'Switch User':
                print('-' * 30)
                print('Sign out.')
                print('-' * 30)
                break

            else:
                print('Please enter a correct option.')
    elif checkUser == superUser and checkpass == superPass:
        while True:
            main_menu()
            try:
                menu = input(str('Please enter your option: '))
                menu = menu.capitalize()
            except:
                print('Please enter a correct option.')
                continue
            if menu == '1' or menu == 'Add record':
                id = input('Please enter the Unique Id number: ')
                try:
                    Employee[id]
                    print('This Id number is already in use, please try again.')
                except KeyError:
                    fname, sname, date, position, department, salary, contNumber, email = employee_details()
                    add_record(id, fname, sname, date, position, department, salary, contNumber, email)

            elif menu == '2' or menu == 'Modify':
                id = input('Please enter the Employee id to modify : ')
                try:
                    Employee[id]
                    print('Modifying  Employee ')
                    fname, sname, date, position, department, salary, contNumber, email = employee_details()
                    modify(id, fname, sname, date, position, department, salary, contNumber, email)

                except:
                    print('This Id number does not exist, please try again.')

            elif menu == '3' or menu == 'List':
                list()
            elif menu == '4' or menu == 'Search':
                id = input('Please enter the Unique Id number: ')
                search(id)
            elif menu == '5' or menu == 'Delete':
                id = input('Please enter the Unique Id number: ')
                delete(id)

            elif menu == '6' or menu == 'Exit':
                print('-' * 30)
                print('Closing the program.')
                print('-' * 30)
                raise SystemExit
            elif menu == '7' or menu == 'Switch User':
                print('-' * 30)
                print('Sign out.')
                print('-' * 30)
                break
            else:
                print('Please enter a correct option.')
    else:
        loop = loop + 1
        print('-' * 30)
        print('User or password incorrect, please, try again.')
        print('-' * 30)
        if loop == 3:
            print('>>>>>>>> Sorry, you have tried too many times! Please try in a while!')
            break



