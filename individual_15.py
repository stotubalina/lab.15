#!/usr/bin/dev python3
# -*- coding: utf-8 -*-

def decorator_setup(start=0):
    def decorator_function(func):
        def wrapper(args):
            result = func(args)
            return result + start

        return wrapper

    return decorator_function


@decorator_setup(start=5)
def ind(data):
    dig = list(map(int, data.split()))
    return sum(dig)


def main():
    string = input("Введите число:\n")
    result = ind(string)
    print(result)


if __name__ == '__main__':
    main()
