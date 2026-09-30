# email must not be empty
# email must contain '.' and '@'
# email must contain exactly one '@' symbol
# email must end with '.com', '.net', or '.org'
# email must not be longer than 50 characters
# email must start and end with digits or letter

email = input("Enter email: ").lower().strip()
password = input("Enter password: ").strip()
valid = True

if email == "" or password == "":
    print("Email and password must not be empty!")
    valid = False

if not ('.' in email and '@' in email):
    print("Email must contain '.' and '@' symbol!")
    valid = False

if email.count('@')>1:
    print("Email must not have more than one '@' sign!")
    valid = False

if not email.endswith(('.com','.net','.org')):
    print("Email must end with '.com', '.net', or '.org'!")
    valid = False

if len(email)>50:
    print("Email must not exceed 50 characters!")
    valid = False

if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must begin and end with a digit or letter!")
    valid = False

if valid:
    print(email,"is a valid email.")






password = input("Enter your password: ").strip()
valid = True

# password must be atleast 8 characters
if len(password)<8:
    print("Password must be at least 8 characters.")
    valid = False

# password must include at least one uppercase
if not any(a.isupper() for a in password):
    print("Password must contain at least one uppercase.")
    valid = False

# password must contain at least one lowercase
if not any(A.islower() for A in password):
    print("Password must contain at least one lowercase.")
    valid = False

# password must not be same as email
if password == email:
    print("Password must not be same as email.")
    valid = False

# password must not contain any spaces
if " " in password:
    print("Password must not contain any spaces.")
    valid = False

# password must start with a letter or number
if not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or number")
    valid = False

if valid:
    print(password,"is a valid password.")