attempts = 0


def cyber_attempts(user, trusted, port):
    global attempts
    attempts += 1
    if (attempts > 5 and user != trusted) or (port in (22, 3389) and attempts >= 3):
        return True
    return False


user = input("enter user")
trusted = input("enter trusted user")
port = int(input("enter port value"))
print(cyber_attempts(user, trusted, port))
