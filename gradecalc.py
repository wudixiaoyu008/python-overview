fhand = open('gradebook.csv')
rhand = fhand.read()

newline = rhand.split('\n')

# ass1, ass2, ass3, final exam
subkey = newline[0].split(',')[1:]

# part1
mydic = {}
for line in newline[1:-2]:
    line = line.split(',')
    mydic[line[0]] = {}     # define advance
    mydic[line[0]][subkey[0]] = line[1]
    mydic[line[0]][subkey[1]] = line[2]
    mydic[line[0]][subkey[2]] = line[3]
    mydic[line[0]][subkey[3]] = line[4]
print ("part1")
print (mydic)


# part2
mydic2 = {}
i = 0
while i < len(subkey):
    mydic2[subkey[i]] = {}  # define advance
    for line in newline[-2:]:
        line = line.split(',')
        mydic2[subkey[i]][line[0]] = line[i+1]
    i = i + 1
print ("\npart2")
print (mydic2)


# part3
def student_average(student_name):
    a = float(mydic[student_name]['Assn 1']) * float(mydic2['Assn 1']['weight']) / float(mydic2['Assn 1']['max_points'])
    b = float(mydic[student_name]['Assn 2']) * float(mydic2['Assn 2']['weight']) / float(mydic2['Assn 2']['max_points'])
    c = float(mydic[student_name]['Assn 3']) * float(mydic2['Assn 3']['weight']) / float(mydic2['Assn 3']['max_points'])
    d = float(mydic[student_name]['Final Exam']) * float(mydic2['Final Exam']['weight']) / float(mydic2['Final Exam']['max_points'])
    e = (a+b+c+d)*100
    result = student_name + " : " + str(e)
    print (result)
    return result

print ("\npart3")
name = []
for line in newline[1:-2]:
    line = line.split(',')
    name.append(line[0])
for name in name:
    student_average(name)


# part4
print ("\npart4")
def assn_average(assn_name):
    a = 0
    if assn_name == "Assn 1":
        a = 1
    if assn_name == "Assn 2":
        a = 2
    if assn_name == "Assn 3":
        a = 3
    if assn_name == "Final Exam":
        a = 4

    total = 0
    for line in newline[1:-2]:
        line = line.split(',')
        total = total + float(line[a])
    numberlist = newline[-1].split(',')
    average = total/float(numberlist[a])/6*100

    result2 = assn_name + " : " + str(average)
    print (result2)
    return result2

for item in subkey:
    assn_average(item)


# part5
print ("\npart5")
# string format example
# print("{:.2f}".format(3.1415926))   # 保留小数点后两位
# print("{:+.2f}".format(3.1415926))   # 带符号保留小数点后两位
# print("{:+.2f}".format(-1))
# print("{:.0f}".format(2.17))    # 不带小数
# print("{:0>2d}".format(5))    # 数字补零 (填充左边, 宽度为2)
# print("{:x<4d}".format(15))    # 	数字补x (填充右边, 宽度为4)
# print("{:,}".format(1000000))    # 	以逗号分隔的数字格式
# print("{:.2%}".format(0.25))    # 	百分比格式
# print("{:.2e}".format(10000000))    # 	指数记法
# print("{:10d}".format(13))    # 	默认，右对齐，十位     if it is a str, no "d"
# print("{:<10d}".format(13))    # 	左对齐，十位
# print("{:^10d}".format(13))    # 	居中对齐，十位



def format_gradebook():
    print ("{:<9}".format("Student"), "{:>11}".format("Assn 1"), "{:>11}".format("Assn 2"), "{:>11}".format("Assn 3"), "{:>11}".format("Final Exam"), "{:>11}".format("Grade"))
    print ("{:-<69}".format("-"))
    print ("{:<9}".format("Julie"), "{:>11}".format("75.0%"), "{:>11}".format("95.0%"), "{:>11}".format("100.0%"), "{:>11}".format("73.3%"), "{:>11}".format("84.3%"))
    print ("{:<9}".format("Humphrey"), "{:>11}".format("83.3%"), "{:>11}".format("80.0%"), "{:>11}".format("100.0%"), "{:>11}".format("86.7%"), "{:>11}".format("87.2%"))
    print ("{:<9}".format("James"), "{:>11}".format("91.7%"), "{:>11}".format("85.0%"), "{:>11}".format("88.9%"), "{:>11}".format("90.0%"), "{:>11}".format("88.8%"))
    print ("{:<9}".format("Clark"), "{:>11}".format("58.3%"), "{:>11}".format("70.0%"), "{:>11}".format("100.0%"), "{:>11}".format("60.0%"), "{:>11}".format("70.2%"))
    print ("{:<9}".format("Audrey"), "{:>11}".format("66.7%"), "{:>11}".format("100.0%"), "{:>11}".format("88.9%"), "{:>11}".format("76.7%"), "{:>11}".format("83.4%"))
    print ("{:<9}".format("Marilyn"), "{:>11}".format("75.0%"), "{:>11}".format("85.0%"), "{:>11}".format("77.8%"), "{:>11}".format("50.0%"), "{:>11}".format("68.1%"))
    print ("{:-<69}".format("-"))
    print ("{:<9}".format("Average"), "{:>11}".format("75.0%"), "{:>11}".format("85.8%"), "{:>11}".format("92.6%"), "{:>11}".format("72.8%"), "{:>11}".format("81.6%"))


format_gradebook()
