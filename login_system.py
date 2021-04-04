# Program will ask user to create a username and password
# and will store information in a text file

# this will create a new file if file is not already created
f = open('login_system','a')
f.close()

# function will ask user to enter a username, check if it is not already used, and
# return username if it is valid
def create_username():
    # will store created usernames in a list
    f = open('login_system', 'r')
    existing_usernames = []
    info = f.readline()
    while info != '':
        full_info = info.split(' ')
        existing_usernames.append(full_info[0])
        info = f.readline()
    f.close()
    # will test user input with existing usernames list
    is_valid = False
    while is_valid == False:
        username = input('Enter a username: ').strip()
        if username in existing_usernames:
            print('Username is taken. Please try another one.')
        else:
            is_valid = True
    
    print('Username is accepted')
    return username

# function will ask user to enter a password, check if it fits the requirements, and
# return password if it is valid
def create_password():
    print("""Password Requirements:
            - 6 to 18 characters long
            - at least one UPPERCASE letter
            - at least one number
            - at least one special character (!, #, $, &)""")
    valid_special_chars = (33,35,36,38)
    is_valid = False
    while is_valid == False:
        password = input('Enter a password: ').strip()
        correct_length = False
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special_char = False
    
        if  6 <= len(password) <= 18:
            correct_length = True
    
        for char in password:
            if char.isupper():
                has_uppercase = True
            if char.islower():
                has_lowercase = True
            if char.isdigit():
                has_digit = True
            if ord(char) in valid_special_chars:
                has_special_char = True
            if char == ' ':
                has_special_char = False
                break
    
        if correct_length and has_uppercase and has_lowercase and \
            has_digit and has_special_char:
            is_valid = True
            return password
        
        print('Invalid password. Please enter a password that ' +
                'fits the requirements.')

def reenter_password(password):
    password2 = input('Confirm password: ')
    if password == password2:
        return True
    else:
        print('Passwords do not match. Please retry.')
        return False

# function will prompt user to enter their details to sign up
def sign_up():
    print('Enter a username and password to sign up')
    username = create_username()
    do_passwords_match = False
    while not do_passwords_match:
        password = create_password()
        do_passwords_match = reenter_password(password)
    print('Password is accepted')
    f = open('login_system', 'a')
    f.write(username + ' ' + password + '\n')
    f.close()
    print('\nYour username and password have been added')

# function will receive user option and return True/False based on input
def get_option():
    answer = input().strip().lower()
    if answer.startswith('y'):
        return True
    elif answer.startswith('n'):
        return False

# function will try to find account and provide feedback with user's inputs
def find_account():
    while True:
        f = open('login_system', 'r')
        info = f.readline()
        account_found = False
        username = input('Enter your username: ').strip()
        password = input('Enter your password: ').strip()
        # loop will test each line to find a username & password match
        while info != '':
            full_info = info.split(' ')
            if username == full_info[0] and password == full_info[1].strip('\n'):
                print('Found your account. Welcome!')
                account_found = True
                break
            info = f.readline()
        if account_found == True:
            break
        # if account_found is false after testing each line,
        # program will prompt user to try again or restart program to sign up
        else:
            print('Username not found or password is incorrect.' +
                  'Press enter to try again or type "new" to sign up.')
            f.close()
            if input().strip().lower() == 'new':
                print("Restart program to sign up.")
                break

# main function runs program
def main():
    print('Do you have an account? (yes or no)')
    if get_option():
        find_account() 
    else:
        print('Would you like to sign up? (yes or no)')
        if get_option():
            sign_up()
            print('Welcome!')
        else:
            print('Have a nice day!')
            
# call to main
main()
