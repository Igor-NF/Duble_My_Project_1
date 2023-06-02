# x = 5
# i = 10
# print(x + i)
# print(id(1))
# print(1, 2, 3, sep="&")
# print(1, 2, 3, sep="@")
# print(1, 2, 3, sep="*****")
# Coment
# a = input('AGE: ')
# print(a)
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num1 += 3
# print("result:", num1 + num2)
# print("result:", num1 - num2)
# print("result:", num1 / num2)
# print("result:", num1 * num2)
# print("result:", num1 ** num2)
# print("result:", num1 // num2)
# print("result:", num1 % num2)

# s = 0; i = 1
# while i <= 1000 and s < 5:
#     s += 1/i
#     i += 1
# print(s)

# A = [ [1, 2, 3,], [4, 5, 6] ]
# n = 2; m = 3
# for i in range(n):
#     for j in range(m):
#         print(A[i][j], end='')
#     print()

# S = 0; M = 10; N = 5
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         S +=i * j
#         print(S, end = "")
# print("\n", S)

#                      Задание из урока.
# a = [-1, 0, 5, 3, 2]
# c = []
# for i in a:
#     b = i + 7.2
#     c.append(b)
# print(c)

# a = [-1, 0, 5, 3, 2]
# i = 0
# c = []
# while i < len(a):
#     b = a[i] + 7.2
#     i += 1
#     c.append(b)
# print(c)

# psw = "fr"
# in_psw = ""
# while psw != in_psw:
#     in_psw = input("Введите пароль: ")
# print("Вход разрешен: ")

# st = 'abrakadabra'
# print(st)
# print(st.count('a'))

# print(st.replace('ab', ''))

# sl = input("    Введите сллово: ")
# dl = len(sl)
# dl1 = dl // 2
# sll = sl[:dl1]
# slr1 = sl[::-1]
# slr = slr1[:dl1]
# if sll != slr:
#     print("    Это слово не полиндром!")
# else:
#     print("     Это слово полиндром! ")

# print(st.find("ra"))

# s = input('введите:')
# print(s.split(" "))


n = 11
a = list(range(n))
print(a)

for i in range(n//2):
    a[i],a[n-i-1] = a[n-i-1],a[i]
    print(n-i-1)
    print(i)
print(a)


x = [5, 2, 7, 6, 4, 8, 7, 9, 1]
y = len(x)
print(y)
for i in range(y-1):
    for j in range(i+1,y):
        if x[i] > x[j]:
            x[i],x[j] = x[j],x[i]
print(x)


lst = list(p)
print(lst)
print(lst.count("+7"))
print(lst[2].count("+7"))
print(p[2].count("+7"))


p = ("+792345678", "+792345478", "+792355678", "+592345678", "+392345678", "+7923456558")
print(p)
n = (len(p))
for i in range(n):
    a = p[i].count("+7")
    if a == True:
        print(p[i])
print('END')

h = ("Оценки: 5, 4, 3, 4, 2, 4, 5, 4")
r = h[8:].replace(", ", "")
print(r)


