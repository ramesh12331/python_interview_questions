def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


def greet():
    print("Hello")


greett = decorator(greet)

greett()