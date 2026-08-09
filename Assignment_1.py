print("hello world")

print("Samarth Gulati")
print("Samarth Gulati")
print("Samarth Gulati")

x = 2
y = 10
z = x + y
print(x, '+', y, '=', z)

ch1 = 'a'
ch2 = 'hello'
ch3 = ch1 + ch2
print(ch1, '+', ch2, '=', ch3)

num = 20
ch = 'world'
ans = str(num) + ch
print(num, '+', ch, '=', ans)

for i in range(0, 10):
    print(i)

j = 0
while j < 10:
    j += 1
    print(j)

for i in range(1, 11):
    print(5, 'X', i, '=', 5 * i)

x = 10
y = 20
z = 30
three_num = x + y + z
print(x, '+', y, '+', z, '=', three_num)

x = 'He'
y = 'llo'
z = ' World'
three_str = x + y + z
print(x, '+', y, '+', z, '=', three_str)

for i in range(1, 11):
    print(7, 'X', i, '=', 7 * i)

for i in range(1, 11):
    print(9, 'X', i, '=', 9 * i)

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, 'X', i, '=', n * i)

n = input("Enter a number: ")
sum = 0
for i in range(0, int(n)):
    sum += (i + 1)
print(sum)

a = input("Enter a number: ")
b = input("Enter another number: ")

if a > b:
    print(a, ">", b)
elif a < b:
    print(a, "<", b)
else:
    print(a, "=", b)

n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

a = input("Enter a string: ")
b = input("Enter another string: ")

if a == b:
    print("a==b")
elif a > b:
    print("a > b")
else:
    print("a < b")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a number: "))

print(max(a, b, c))