#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def zero_sum(*args):
    if args:
        i = 0
        for index, arg in enumerate(args):
            if arg == 0:
                i = index
                break
        zer_s = sum(abs(arg) for index, arg in enumerate(args) if index > i)
        return zer_s
    else:
        return None


if __name__ == "__main__":
    arguments = [int(i) for i in input("Введите аргументы: ").split()]
    print("Сумма модулей аргументов после первого 0: "
          f"{zero_sum(*arguments)}"
    )
