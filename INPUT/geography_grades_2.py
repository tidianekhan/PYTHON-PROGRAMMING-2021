import sys
import re



print("Report for group 2b")

for line in sys.stdin.readlines():
    line = line.strip('\n')
    item = re.split('_+', line)
    grades = item[1].split(" ")
    list_of_grades = []


    for x in grades:
        list_of_grades.append(float(x))
        average = (sum(list_of_grades) / len(list_of_grades))
        average = round(average*2)/2
        if average == 5.5:
            average = 6.0

    names = item[0]
    grade_line = str(names) + " has a final grade of " + str(average) + "\n"
    print(grade_line, end="")

print("End of report")



