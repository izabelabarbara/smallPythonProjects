import stackClass as sc

s1 = sc.Stack()

for c in "Witam":
    s1.push(c)

reversed_string = ""

for i in range (s1.size):
    reversed_string += s1.pop()

print(reversed_string)
