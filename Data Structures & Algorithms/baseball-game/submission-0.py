class Solution:
    def calPoints(self, operations: List[str]) -> int:
        optypes = ["+","D","C"]
        record = []
        for i, op in enumerate(operations):
            if op in optypes:
                match op:
                    case "D":
                        record.append(int(record[len(record)-1])*2)
                    case "C":
                        record.pop()
                    case "+":
                        record.append(int(record[len(record)-1]) + int(record[len(record)-2]))
            else:
                try:
                    record.append(int(op))
                except Exception as e:
                    print(e)
        return sum(record)

        