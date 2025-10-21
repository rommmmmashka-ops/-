import math
import sys
import numpy
import time
import random
import pandas
import PIL
import matplotlib
import openpyxl
import os


def try_math():
    try:
        print(math.sqrt(64), math.log(64, 2))
    except Exception as e:
        print(e)


def try_sys():
    try:
        version = sys.version
        platform = sys.platform
        print(version, platform)
    except Exception as e:
        print(e)


def try_numpy():
    try:
        array = [1, 4, 9, 16, 25, 26]
        print(numpy.sqrt(array))
    except Exception as e:
        print(e)


def try_time():
    try:
        start = time.perf_counter()
        time.sleep(2)
        end = time.perf_counter()
        print(end - start)
    except Exception as e:
        print(e)


def try_random():
    try:
        array = random.sample(range(100), 10)
        print(array)
    except Exception as e:
        print(e)


def main():
    try_math()
    try_sys()
    try_numpy()
    try_time()
    try_random()


if __name__=="__main__":
    main()