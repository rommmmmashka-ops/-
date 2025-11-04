import time
from decorator.decorator import log_time


@log_time
def square(number):
    time.sleep(2)
    result = number * number
    return result


def main():
    print(square(1, 2, 4, 15, 20.5))

if __name__=="__main__":
    main()