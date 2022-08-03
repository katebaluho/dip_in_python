def is_acceptable_password(password):
    return len(password) > 6 and any(map(str.isdigit, password))

print(is_acceptable_password('fg'))












