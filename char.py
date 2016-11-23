#!/usr/bin/python3.4
# -*-coding:utf-8 -*


def char(x):
    x = chr(x)
    return x


def charlisting():
    y = 0
    x = chr(y)
    while x:
        try:
            x = chr(y)
            print("char {0} = '{1}'".format(y, x))
            y += 1
        except UnicodeEncodeError:
            print("not more character")

if __name__ == "__main__":
    charlisting()
