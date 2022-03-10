#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_laboratories(**kwargs):
    """ Максимальный вес груза, прибывшего в порт.

    На вход поступает название судна и общий вес груза

    Функция выводит название судна, которое прибыло с грузом наибольшего веса

    """
    if kwargs:
        max_weight = max(kwargs.values())
        for vessel, weight in kwargs.items():
            if weight == max_weight:
                print(
                    f"Наибольший вес груза - ({weight} тонн) "
                    f" у судна: {vessel}"
                )
    else:
        return None


if __name__ == "__main__":
    min_laboratories(Arkadiy=90, Chayka=4, Napoleon=1, London=7)
    min_laboratories(Starflight=16, Vansk=5, Alekstour=45)
    min_laboratories(Flavour=13)
