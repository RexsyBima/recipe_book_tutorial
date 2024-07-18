def greet(username: str):
    print(f"{username}")


# greet(
#    True
# )  # dynamic type typing -> variabel tidak perlu dideklarasikan tipedatanya apa


def numberpositive(number: int):
    if number >= 0:
        return True
    else:
        raise ValueError("number must be positive")


def checkemail(email: str):
    if "@" in email:
        return True
    else:
        raise ValueError("email must have @")


# x = -10
# y = numberpositive(x)
# print(y)
#

checkemail("jokoko")
