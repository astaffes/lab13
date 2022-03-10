#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mid_geom(*args):
    if args:
        multiplication = 1
        values = [float(arg) for arg in args]
        n = len(values)
        for elem in values:
            multiplication *= elem
        return multiplication ** (1 / n)
    else:
        return None


if __name__ == "__main__":
    arguments = [float(i) for i in input("Введите аргументы: ").split()]
    print(f"Среднее геометрическое: {mid_geom(*arguments)}")
