class Student:
    def __init__(self, name, student_nr, points_per_assignment, exam_grade):
        self.name = name
        self.student_nr = student_nr
        self.points_per_assignment = points_per_assignment
        self.exam_grade = exam_grade

    def course_points(self):
        # What the points in each assignment are worth via the course overview page
        multipliers = [1, 2, 2, 2, 3, 3]
        total = 0
        # Multiply each assignment grade by a multiplier in each list.
        for points_per_assignment, multipliers in zip(self.points_per_assignment, multipliers):
            total += points_per_assignment * multipliers
        return total

    def grade(self):
        # According to the course overview for every extra point 0.02 is added to the grade.
        difference = self.course_points() - 95
        final_grade = self.exam_grade + difference * 0.02
        final_grade = round(final_grade * 2) / 2
        # According to the course overview, if the grade is 5.5 then the final grade is rounded up to 6.0
        if final_grade == 5.5:
            final_grade = 6.0
        # Another condition is that it is less than 5.5 then it is "Niet Voldaan"
        if self.exam_grade < 5.5:
            final_grade = "NVD"
        # Another condition is that the course_points are less than 95 then it is "Niet Voldaan"
        if self.course_points() < 95:
            final_grade = "NVD"
        return final_grade


    def result(self):
        x = self.grade()
        if x == "NVD":
            x = "NVD"
        else:
            # String Formatting
            x = "%.1f" % x
        result = ("%s (%d) has scored %s on X_401096" % (self.name, self.student_nr, x))
        return result

    def passes(self):
        x = self.grade()
        if x == "NVD":
            return False
        else:
            return True

    def scores_higher_than(self, b):
        x = self.grade()
        y = b.grade()
        if y == "NVD":
            return True
        elif y < x:
            return True
        elif x == "NVD":
            return False
        else:
            return False



if __name__ == "__main__":
    # put test code here
    mary = Student("Mary", 15789613, [10, 9, 8, 10, 9, 10], 9)
    alice = Student("Alice", 1235233, [10, 9, 9, 9, 8, 7], 7)
    bob = Student("Bob", 1235232, [10, 9, 7, 9, 8, 9], 5)
    charlie = Student("Charlie", 13655232, [10, 7, 6, 7, 9, 6], 5.5)
    anne = Student("Anne", 12655232, [10, 9, 5, 10, 5, 5], 8)


class Class(Student):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def pass_rate(self):
        total_passing_students = 0
        class_size = len(self.students)
        for student in self.students:
            if student.passes():
                total_passing_students += 1
        pass_rate = total_passing_students/class_size
        return pass_rate


