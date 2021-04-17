#!/usr/bin/env python3


from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)
session_id = auth.create_session(email)
print(f"user {email} session ID: {session_id}")

user = auth.get_user_from_session_id(session_id)

if user is None:
    print(f"No User Found for session={session_id}")
else:
    user_id = user.id
    print(f"User {user.email} Found for session={session_id}")
    print(f"User {user.email} has id={user_id}")

print("\n-------------------------------------------\n")

auth.destroy_session(user_id)
print(f"User {user.email} has id={user_id} and SessionID={user.session_id}")
