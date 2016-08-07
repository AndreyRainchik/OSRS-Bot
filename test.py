__author__ = 'Admin'
kelly = [4, 9, 11, 15, 16, 18, 19, 22, 24, 25, 26, 29, 32, 33, 35, 38, 39, 40, 48, 49, 51, 52, 55, 58, 67, 68, 70, 73, 74, 77, 78, 79, 82, 85, 87, 90, 91, 92, 93, 94, 95, 98, 99, 100, 101]
andrey = [2, 4, 9, 11, 14, 15, 16, 19, 20, 22, 23, 24, 25, 31, 33, 35, 36, 38, 39, 40, 46, 48, 49, 50, 51, 55, 58, 60, 65, 67, 70, 74, 75, 77, 78, 79, 80, 81, 82, 83, 85, 86, 90, 91, 92, 93, 94, 95, 98, 99, 100, 101]
same = []
andreyDiff = []
kellyDiff = []
for i in range(0,len(andrey)):
    if andrey[i] in kelly:
        same += [andrey[i]]
    else:
        andreyDiff += [andrey[i]]
for j in range(0,len(kelly)):
    if kelly[j] in same:
        x = 3
    else:
        kellyDiff += [kelly[j]]
print same
print andreyDiff
print kellyDiff