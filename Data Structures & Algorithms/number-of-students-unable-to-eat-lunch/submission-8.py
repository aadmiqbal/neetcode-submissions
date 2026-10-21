class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches.reverse()
        my_students = deque(students)
        while True:
            for i in range(len(my_students)):
                if my_students[0] == sandwiches[-1]:
                    my_students.popleft()
                    sandwiches.pop()
                    continue
                else:
                    my_students.append(my_students.popleft())

            if not sandwiches:
                break
            if sandwiches[-1] not in my_students:
                break
        return len(my_students)

