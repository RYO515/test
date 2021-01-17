# モジュール「chap4func」
# import chap4func
# chap4func.create_mail('山本', 40000)

import chap4func

data = [
{'name':'山本', 'bill':40000, 'crg':True},
{'name':'吉田', 'bill':25000, 'crg':False}
]

for rec in data:
    bill = rec['bill']
    if rec['crg']:
        bill = chap4func.add_charge(bill)

    chap4func.create_mail(rec['name'],bill)