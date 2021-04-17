#!/usr/bin/env python3


from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)
print("User registered!")


reset_token = auth.get_reset_password_token(email)
print(f"token is reset")


try:
    auth.update_password(reset_token, "new_pwd")
    print("password updated!")
except ValueError:
    print("Token is not verified, Try again")

fake_token = 'a8b15fa9-5f93-4a71-b7ff-00d2465efc20'
try:
    auth.update_password(fake_token, "new_pwd")
    print("password updated!")
except ValueError:
    print("Token is not verified, Try again")
