import sys
import re


groups = sys.stdin.read().split("=\n")
for group in groups:
        group = group.splitlines()
        class_name = group[0]
        print("Report for group " + str(class_name))
        del group[0]
        for x in range(len(group)):
            item = str(group[x])
            item = re.split('_+', item)
            grades = item[1].split(" ")
            list_of_grades = []

            for x in grades:
                list_of_grades.append(float(x))
                average = (sum(list_of_grades) / len(list_of_grades))
                average = round(average * 2) / 2
                if average == 5.5:
                    average = 6.0

            names = item[0]
            grade_line = str(names) + " has a final grade of " + str(average) + "\n"
            print(grade_line, end="")

        print("End of report\n")

