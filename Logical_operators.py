#python challenges on logical operators

# 1 Check if a user's name is not empty and the age is greater than or equal to 18
user_name = input("enter user name ")
age = int(input("enter your age "))

if(user_name != "" and age>=18):
    print("user is valid")
else:
    ("user is not valid")

# 2 Check if the password is at least eight characters long and does not contain spaces

password = input("Entre your password")
if(len(password) <8 and " " in password):
    print("invalid password")
else:
    print("Valid password")

# 3 Check if a user's email is not empty contains '@' and ends '.com'

email = input("enter your email id")
if email != "" and '@' in email and email.endswith('.com'):
    print('Vaild email')
else:
    print('Invalid email')

# 4 Check if a username is a string is not None and is longer than characters
user_name2 = input("enter username")

if isinstance(user_name2, str) and user_name2 is not None and len(user_name2)>5 :
    print("Valid username")
else:
    print("invalid username")

# 5 Check if the user is either an admin or moderator and either they are not banned or they have verified their email

role = "admin"
banned = False
verified_email = True

if (role == "admin" or role == "moderator") and (not banned or verified_email):
    print("authorized")
else:
    print("unauthorized")

# membership operator --- in , not in 

#validate the domain is not on the banned list
domain_name = input("enter domain name")

banned_domain = ['spam.com', 'junk.com', 'fake,org']
if domain_name in banned_domain:
    print("Banned Domain")
else:
    print('Valid domain')