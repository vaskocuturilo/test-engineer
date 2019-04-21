users = [
    {"name": "invalid_user", "login": "admin", "password": "admin"}]


def get_user(name):
    try:
        return (user for user in users if user["name"] == name).next()
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)
