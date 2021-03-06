import getpass


def check_passwd(min_length=8, check_username=True):
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    print(username, password)
    if len(password) < min_length:
        print("Пароль слишком короткий")
        return False
    elif check_username and username in password:
        print("Пароль содержит имя пользователя")
        return False
    else:
        print(f"Пароль для пользователя {username} прошел все проверки")
        return True
