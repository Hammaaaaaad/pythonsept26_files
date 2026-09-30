emails = [
    "alice.johnson@example.com",
    "bob.smith@gmail.com",
    "charlie99@yahoo.com",
    "david.wilson@outlook.com",
    "emma.brown@company.org",
    "frank.miller@mail.com",
    "grace.davis@example.net",
    "henry.taylor@proton.me",
    "isabella.moore@gmail.com",
    "jack.anderson@yahoo.co.uk",
    "karen.thomas@example.com",
    "liam.jackson@outlook.com",
    "mia.white@gmail.com",
    "noah.harris@example.org",
    "olivia.martin@mail.com",
    "paul.thompson@yahoo.com",
    "quinn.garcia@example.net",
    "rachel.martinez@gmail.com",
    "sam.robinson@company.com",
    "tina.clark@proton.me",

    # Invalid emails
    "invalid-email",
    "@example.com",
    "user@",
    "user@@example.com",
    "user example@gmail.com",
    "user.example.com",
    "user@.com",
    "user@example",
    "user@example..com",
    ".user@example.com",
    "user.@example.com",
    "user@-example.com",
    "user@example-.com",
    "user#example.com",
    "user@ example.com",
    "user@exam_ple.com",
    "user..name@example.com",
    "user@example,com",
    "user@example.com.",
    "user@",
    "example.com"
]
valid_emails = []
invalid_emails= []


for email in emails:
    valid = True
    if email == "":
        valid = False
    if not ('.' in email and '@' in email):
        valid = False
    if email.count('@')>1:
        valid = False
    if not email.endswith(('.com','.net','.org')):
        valid =False
    if not email[0].isalnum() and email[-1].isalnum():
        valid = False
    if valid:
        valid_emails.append(email)
    else:
        invalid_emails.append(email)

print("Valid emails:", len(valid_emails))
print("Invalid emails:", len(invalid_emails))

print (invalid_emails)