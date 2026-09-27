class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches.reverse()
        done = False
        prevLength = len(students)
        while not done:
            for student in (students):
                if student == sandwiches[-1]:
                    sandwiches.pop()
                    students = students[1:]
                    break
                else:
                    students = students[1:]
                    students.append(student)

            if len(students) == prevLength:
                done = True
            prevLength = len(students)

        return len(students)
