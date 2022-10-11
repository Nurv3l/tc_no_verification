from operator import le
import re


tc_no = []
real_tc_no = []
firstTwoDigits = input("Enter the first two digits:")
lastTwoDigits = input("Enter the last two digits:")
for i in range(1000000, 9999999, 1):
    result = str(firstTwoDigits) + str(i) + str(lastTwoDigits)
    tc_no.append(result)
for k in range(0, 1000000, 1):
    if k < 10:
        k = str(k)
        tc_no.append(str(firstTwoDigits) + k.zfill(7) + str(lastTwoDigits))
    elif 10 <= k < 100:
        k = str(k)
        tc_no.append(str(firstTwoDigits) + k.zfill(7) + str(lastTwoDigits))
    elif 100 <= k < 1000:
        k = str(k)
        tc_no.append(str(firstTwoDigits) + k.zfill(7) + str(lastTwoDigits))
    elif 1000 <= k < 10000:
        k = str(k)
        tc_no.append(str(firstTwoDigits) + k.zfill(7) + str(lastTwoDigits))
    elif 10000 <= k < 100000:
        k = str(k)
        tc_no.append(str(firstTwoDigits) + k.zfill(7) + str(lastTwoDigits))
    elif 100000 <= k < 1000000:
        k = str(k)
        tc_no.append(str(firstTwoDigits) + k.zfill(7) + str(lastTwoDigits))
for j in tc_no:
    sumDigits = (int(j[0]) + int(j[2]) + int(j[4]) + int(j[6]) + int(j[8])) * 7
    sumDigits2 = int(j[1]) + int(j[3]) + int(j[5]) + int(j[7])
    result = sumDigits - sumDigits2
    result2 = int(result % 10)
    if result2 != int(j[9]):
        pass
    elif result2 == int(j[9]):
        if (int(j[0]) + int(j[1]) + int(j[2]) + int(j[3]) + int(j[4]) + int(j[5]) + int(j[6]) + int(j[7]) + int(j[8]) + int(j[9])) % 10 == int(j[10]):
            real_tc_no.append(j)
for j in real_tc_no:
    with open('/Users/nbursali/Desktop/rresult.txt', 'a') as the_file:
        the_file.write(j + '\n')
print(len(real_tc_no))