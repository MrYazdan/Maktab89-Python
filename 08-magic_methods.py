class Mark:
    def __init__(self, lesson_name, mark):
        self.lesson = lesson_name
        self.mark = mark

    # def __str__(self):
    #     return f"{self.lesson} : {self.mark}"

    def __repr__(self):
        return f"<Mark : [{self.lesson}:{self.mark}]>"


class UserMarks:
    def __init__(self, _marks):
        self.marks = _marks  # => list

    def add(self, mark):
        assert isinstance(mark, Mark), "Error !"
        self.marks.append(mark)

    def __add__(self, other):
        if isinstance(other, Mark):
            self.marks.append(other)
            return self
        else:
            assert isinstance(other, UserMarks)
            return self.marks + other.marks


marks = [
    Mark('math', 19),
    Mark('english', 10),
    Mark('programming', 20),
]

reza_marks = UserMarks(marks)
reza_marks.add(Mark('chemistry', 9))

reza_marks += Mark('physic', 4)  # -> reza_mark = reza_mark + Mark...

print(Mark('physic', 4))
print(reza_marks)

# ali_marks = UserMarks([Mark('math', 10), Mark('physic', 18)])
#
# all_marks = reza_marks + ali_marks
# print(all_marks)

# all_marks = reza_marks + ali_marks
