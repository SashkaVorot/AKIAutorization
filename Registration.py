def users_coincidence(login, password):
    file = open('users.txt', 'r')

    file = file.read()

    spc1 = 0
    spc2 = 0
    men = []
    men_login = []
    men_pass = []

    for i in range(len(file)):
        if file[i] == '\n':

            spc2 = i
            men.append(file[spc1:spc2])
            spc1 = spc2

    for i in range(len(men)):
        men[i] = men[i].replace('\n', '')

        indexI = men[i].find(' I ')

        men_login.append(men[i][:indexI])
        men_pass.append(men[i][indexI + 3:])

        if login == men_login[i] and  password == men_pass[i]: return True

    return False
        

def users_in_base(login):
    file = open('users.txt', 'r')

    file = file.read()

    spc1 = 0
    spc2 = 0
    men = []
    men_login = []

    for i in range(len(file)):
        if file[i] == '\n':

            spc2 = i
            men.append(file[spc1:spc2])
            spc1 = spc2

    for i in range(len(men)):
        men[i] = men[i].replace('\n', '')

        indexI = men[i].find(' I ')

        men_login.append(men[i][:indexI])

    for i in men_login:
        if i == login:
            print('Such user already exists')
            return True

    return False

def fuck():
    answer = ''
    
    while answer != '0' and answer != '1' and answer != '2':
        answer = input('Enter 0 to exit\nEnter 1 to register again\nEnter 2 to enter login and password\n')

    if answer == '0': print('Goodbye')
    elif answer == '1': registration()
    elif answer == '2': log_in()

def registration():
    login = input('Login: ')
    password = input('Password: ')

    if users_in_base(login):
        return fuck()
    file_write = open('users.txt', 'a')

    file_write.write(login + ' I ' + password + '\n')
    file_write.close()

    print('Success')
    
def log_in():
    login = input('Login: ')
    password = input('Password: ')
    
    if users_coincidence(login, password) == False:
        print('Wrong login or password')
        fuck()
    else:print('Hello ' + login)
    
answer = ''

while answer != '0' and answer != '1' and answer != '2':
    answer = input('Enter 0 to exit\nEnter 1 to register\nEnter 2 to log in\n')

if answer == '0': print('Goodbye')
elif answer == '1': registration()
elif answer == '2': log_in()
    
