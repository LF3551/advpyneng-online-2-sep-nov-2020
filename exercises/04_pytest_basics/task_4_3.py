# -*- coding: utf-8 -*-
'''
Задание 4.3

Написать тест(ы), который проверяет есть ли маршрут 192.168.100.0/24 в таблице
маршрутизации (команда sh ip route) на маршрутизаторах, которые указаны в файле devices.yaml.

Для проверки надо подключиться к каждому маршрутизатору с помощью netmiko
и проверить маршрут командой sh ip route или разновидностью команды sh ip route.

Тест(ы) должен проходить, если маршрут есть.
Тест может быть один или несколько.

Тест(ы) написать в файле задания.
'''
