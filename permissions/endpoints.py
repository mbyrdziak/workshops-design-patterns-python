from permissions.state import add_permission


def login(username, password):
    if username == "administrator":
        add_permission("admin")
    else:
        add_permission("user")
    print("Logging in")


def get_user_secrets():
    print("Accessing logged in user endpoint")


def get_admin_secrets():
    print("Accessing logged in admin endpoint")
