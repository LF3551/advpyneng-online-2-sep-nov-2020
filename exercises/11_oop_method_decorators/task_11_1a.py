# -*- coding: utf-8 -*-
'''
Задание 11.1a

Скопировать класс IPv4Network из задания 11.1.
Добавить метод from_tuple, который позволяет создать экземпляр класса IPv4Network
из кортежа вида ('10.1.1.0', 29).

Пример создания экземпляра класса:

In [3]: net2 = IPv4Network.from_tuple(('10.1.1.0', 29))

In [4]: net2
Out[4]: IPv4Network(10.1.1.0/29)

'''
