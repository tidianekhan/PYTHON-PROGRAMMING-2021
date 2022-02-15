def make_new_array(num_of_rows, num_of_columns):
    rows = []
    for _ in range(num_of_rows):
        row = []
        for _ in range(num_of_columns):
            row.append(0)
        rows.append(row)
    return rows


class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        list_of_lines = []
        for row in self.rows:
            sections = []
            for value in row:
                s = str(value)
                if len(s) == 1:
                    sections.append(" ")
                sections.append(str(value))
                sections.append(" ")
            sections.pop()
            sections.append("\n")
            line = "".join(sections)
            list_of_lines.append(line)
        return "".join(list_of_lines)



    def transpose(self):
        additional_rows = []
        cols = len(self.rows[0])
        for col_index in range(cols):
            additional_row = []
            for row in self.rows:
                additional_row.append(row[col_index])
            additional_rows.append(additional_row)
        return Matrix(additional_rows)


    def scale(self, x):
        additional_rows = []
        for row in self.rows:
            additional_row = []
            for value in row:
                additional_row.append(value * x)
            additional_rows.append(additional_row)
        return Matrix(additional_rows)

    def multiply(self, b):
        if len(self.rows[0]) != len(b.rows):
            return None

        result = make_new_array(
            num_of_rows=len(self.rows),
            num_of_columns=len(b.rows[0])
        )

        for x in range(len(self.rows)):
            for y in range(len(b.rows[0])):
                for z in range(len(b.rows)):
                    result[x][y] += self.rows[x][z] * b.rows[z][y]
        return Matrix(result)

    # repr is similar to __str__, but __str__ is used  when
    # printing a value, __repr__ when showing a value in
    # the interpreter.
    # repr is intended to be an unambiguous, complete representation
    # of the object, while str is intended to be nicely readable
    # for this object they are the same
    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    pass