import re
f = open("Day3\data.txt")
text = f.read()

found = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don\'t)\(\)', text)
res = 0
do = True
for item in found:
    if item[2] != "":
        do = True
    elif item[3] != "":
        do = False
    if do == True and item[0].isdigit():
        a, b = int(item[0]), int(item[1])
        res += a*b
print(res)