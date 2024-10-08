import os, secrets, sys, string, pyperclip

def exit_program():
    sys.exit()

def create_random_password():
    length = int(input("how many characters do you like"))
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password
def store_password(service, username, password):
    with open ("password.txt", "a") as x:
        x.write(f"service: {service}, username: {username}, password: {password}")
        print('password is succesfully saved')

def does_file_exist():
    if os.path.exists("password.txt"):
        return True
    else:
        return False

def does_master_exist():
    if os.path.exists('masterpasswd.txt'):
        return True
    else:
        return False

def read_password():
    with open("password.txt", "r") as xx:
        return xx.read()

def copy(copied):
    pyperclip.copy(copied)
    print("copied")
    
def create_master(master):
    with open("masterpasswd.txt", "w") as xxx:
        xxx.write(master)
        print("master password created")
        return master

def read_master():
    with open("masterpasswd.txt", "r") as xxxx:
        return xxxx.read()

def delete_all_passwords():
    os.remove("password.txt")

def delete_master():
    os.remove("masterpasswd.txt")

def main():
    if os.path.exists("masterpasswd.txt"):
        masterpassword = input("what is your master password? \n")
        if masterpassword == read_master():
            print("master password is correct, what do you want to do?")
            while True:
                choice = int(input("1. store a password \n 2. see stored password \n 3. delete all passwords \n 4. delete all data including master password \n 5. exit program \n"))
                if choice == 1:
                    username = input("enter your username \n")
                    service = input('enter a service \n')
                    choice2 = int(input('press 1 if you want to randomly generate a password \n'))
                    if choice2 == 1:
                        password = create_random_password()
                    else: 
                        password = input('what is your password \n')
                    store_password(service, username, password)
                
                elif choice == 2:
                    if does_file_exist():
                        print(read_password())
                        copy(read_password())
                        print('passwords copied')
                    else:
                        print('no passwords found')
                
                elif choice == 3:
                    if does_file_exist():
                        delete_all_passwords()
                        print('passwords succesfully deleted')
                    else:
                        print('no passwords found')
                elif choice == 4:
                    if does_file_exist() and does_master_exist():
                        delete_all_passwords()
                        delete_master()
                        print('passwords and master password succesfully deleted')
                    elif does_file_exist() == False and does_master_exist():
                        delete_master()
                        print('passwords deleted')
                    else:
                        print('no passwords found')
                elif choice == 5:
                    exit_program()

        else:
            print("you entered the wrong password")
            exit_program()
 
    else:
        choice3 = int(input('no master password found. would you like to sign up? press 1 or 0 \n'))
        if choice3 == 1:
            master = input('create a master password, 12 characters at least \n')
            if len(master) < 12:
                print("your master password may not be less than 12 characters")
                print('exiting')
                exit_program()
            else:
                create_master(master)
                print('master password succesfully created. restarting the program.')
                exit_program()
        else:
            print('exiting')
            exit_program()
        
if __name__ == '__main__':
    main()













        
