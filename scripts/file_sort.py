# -*-coding:utf-8 -*-
import os

import uniout

file_order = [
    u"四護一甲(A)",u"四護一甲(B)",
    u"四護一乙(A)",u"四護一乙(B)",
    u"四護一丙(A)",u"四護一丙(B)",
    u"四社一甲",u"四社一乙",
    u"四食一甲(A)",u"四食一甲(B)",
    u"四食一乙(A)",u"四食一乙(B)"
]

input_dir = "input"

files = [f.decode("big5") for f in os.listdir(input_dir)]
files.sort()
sorted_file = []

for f in file_order:
    temp = [o for o in files if f in o]
    for old_name in temp:
        sorted_file.append(old_name)
for index, old_name in enumerate(sorted_file):
    print(input_dir,"%02d.%s" % (index, old_name))
    os.rename(os.path.join(input_dir,old_name),
              os.path.join(input_dir,"%02d.%s" % (index, old_name)))