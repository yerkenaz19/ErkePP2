import re
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))
emails = ["user@example.com", "invalid-email@", "test.email@kbtu.kz", "hello@123", "user.name@domain.org"]

for e in emails:
    print(f"{e} -> {is_valid_email(e)}")
