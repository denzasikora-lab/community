def shout(func):
    def wrapper():
        print(">>> старт функции")
        result = func()
        print(">>> конец функции")
        return result
    return wrapper


@shout
def hello():
    print("Hello, world!")


if __name__ == "__main__":
    hello()
