textfile = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text18-9.txt', 'r', encoding='utf-8')


lineslist = textfile.readlines()
count = 0
lengthlist = len(lineslist)
linefound = False
for i in lineslist:
    if i == "Умремте же под Москвой," + "\n":
        print("true")
        count += 1
        linefound = True
    else:
        count += 1
if (count == lengthlist) and (linefound == False):
    print("error")
else:
    print(f'Номер строки: {count}')