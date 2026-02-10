if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0
    indx = 0
    for key,value in student_marks.items():
        if key == query_name:
            for x in student_marks[query_name]:
                total += x
                indx = len(student_marks[query_name])
        else:
            continue
    val = total/indx
    print(f"{val:.2f}")
