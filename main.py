# -*- coding: utf-8 -*-
# encoding: utf-8
'''
скриптик для замены  местами 4 байтов значения карты клиента
'''
from __future__ import absolute_import, division, print_function, unicode_literals

import csv

card_list = []
with open('Order_FCT_44320_Apa_Rura_Batches_3_FCT_51978не_прописанные.csv') as f:
    card_read_file = csv.reader(f)
    for card_number in card_read_file:
        card_list.append(card_number)
ferst_item = card_list[0]
card_list.pop(0)
new_list = []
for i in card_list:
    i = ''.encode('utf8').join(i)
    i = list(i)
    i.insert(11, i[17])
    i.insert(12, i[19])
    i.pop(20)
    i.pop(19)
    i.insert(13, i[17])
    i.insert(14, i[19])
    i.pop(20)
    i.pop(19)
    i.insert(15, i[17])
    i.insert(16, i[19])
    i.pop(20)
    i.pop(19)
    i = ''.join(i)
    new_list.append(i.split())
new_list.insert(0, ferst_item)
with open('Order_FCT_44320_Apa_Rura_Batches_3_FCT_51978.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(new_list)
