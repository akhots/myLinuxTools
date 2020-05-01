#!/usr/bin/env python3
import os

ip_lst = []

while True:
    elem = input(':')
    if elem == '':
        break
    ip_lst.append(elem)

res_lst = []
for ip in ip_lst:
    res = os.popen('ping ' + ip + ' -c 1').read()
    if res == '':
        res_lst.append((ip, 'error'))
    else:
        res_lst.append((ip, res.split()[-2][1:]))

print('ip - loss')
for res in res_lst:
    print(res[0] + ' - ' + res[1])


input()

