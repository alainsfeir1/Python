from PasswordCheckerClass import passwordChecker
def main():
    print("Welcome to Password Validation")
    print('''Create a password with :
    1. Minimum length of transaction password: 6
    2. Maximum length of transaction password: 12
    3. At least 1 letter between [a-z]
    4. At least 1 letter between [A-Z]
    5. At least 1 character from [$#@]
    ''')
    while True:
        password=input("Type in password:")
        Pass=passwordChecker(str(password))
        Pass.passwordConverter()
        Pass.passSize()
        Pass.letterChecker()
        Pass.specialChararacterChecker()
        Pass.Validity()
main()
        
