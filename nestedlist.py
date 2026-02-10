students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# extract scores
scores = []
for s in students:
    scores.append(s[1])

# get second lowest distinct score
unique_scores = sorted(set(scores))
second_lowest = unique_scores[1]

# get names with second lowest score
result = []
for s in students:
    if s[1] == second_lowest:
        result.append(s[0])

# print in alphabetical order
for name in sorted(result):
    print(name)
