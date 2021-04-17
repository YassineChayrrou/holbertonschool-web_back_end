#!/usr/bin/env python3


from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

user = auth.register_user(email, password)

print(user.reset_token)


auth.get_reset_password_token(email)

print(user.reset_token)

fake_email = 'fake@fake.com'
try:
    auth.get_reset_password_token(fake_email)
except ValueError:
    print("email does not exist")
