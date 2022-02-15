import sys
import re

list_of_lists = []
for line in sys.stdin.readlines():
    stripped_line = line.strip()
    list_of_lists.append(stripped_line)

for t in range(len(list_of_lists)):
    if t % 2 == 0:
        item = list_of_lists[t]
        item = re.split('_+', item)
        grades = item[1].split(" ")
        list_of_grades = []

        for x in grades:
            list_of_grades.append(float(x))
            average = (sum(list_of_grades) / len(list_of_grades))
            average = round(average * 2) / 2
            if average == 5.5:
                average = '6-'

        names = item[0]
        grade_line = str(names) + " has an average of " + str(average) + "\n"
        print(grade_line, end="")

    if t % 2 != 0:
        elem = list_of_lists[t]
        elem = elem.split(';')
        similarity_score = elem[0].split("=")
        similar_names = elem[1]
        for x in similarity_score:
            index = similarity_score.index(x)
            x = int(x)
            similarity_score[index] = x

        for x in similarity_score:
            index = similarity_score.index(x)
            if x == 0:
                similarity_score[index] = '_'
            elif x < 20:
                similarity_score[index] = '-'
            elif x >= 20:
                similarity_score[index] = '^'
        str1 = ''.join(similarity_score)

        print(str1)



        similar_names = similar_names.split(",")
        for x in similar_names:
            if x == '':
                print("No matches found")
            else:
                print(x)

        print("\n")






































