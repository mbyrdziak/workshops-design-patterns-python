import datetime

from invitation import *


def main():
    invitation = Invitation(
        "inviteId",
        datetime.datetime(2013, 7, 17),
        datetime.datetime(2014, 7, 17),
        "email",
        "new",
        "admin",
        datetime.datetime(2013, 7, 17),
        None,
        None,
        ["participant1@test.com", "participant2@test.com"]
    )

if __name__ == "__main__":
    main()
