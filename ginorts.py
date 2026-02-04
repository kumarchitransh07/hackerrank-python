s = input()

lower = []
upper = []
odd = []
even = []

for ch in s:
    if ch.islower():
        lower.append(ch)
    elif ch.isupper():
        upper.append(ch)
    elif ch.isdigit():
        if int(ch) % 2 == 0:
            even.append(ch)
        else:
            odd.append(ch)

result = (
    ''.join(sorted(lower)) +
    ''.join(sorted(upper)) +
    ''.join(sorted(odd)) +
    ''.join(sorted(even))
)

print(result)
