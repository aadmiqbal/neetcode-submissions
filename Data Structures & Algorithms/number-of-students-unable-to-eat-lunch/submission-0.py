class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circle sandwich = 0
        # square sandwich = 1

        #students stand in a queue
        # sandwiches are in a stack

        #if student likes sandwich at top of the stack, pop stack and dequeue
        # else dequeue and enqueue them

        #return number of students that dont get their sandwich
        # a full pass of the students without getting rid of one from the queue means we are done
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
