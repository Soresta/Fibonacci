# Fibonacci:
# 1 1 2 3 5 8 13 .... diye devam eden fibonacci sersisinin ilk 50 sayısını ekrana yazdırın program.
# The program that prints the first 50 numbers of the fibonacci series.

totalResult = 0
num1 = 1
num2 = num1
liste = [1]
totalResult = num1

for i in range(1, 50):
    liste.append(totalResult)
    totalResult = num1 + num2
    num1 = num2
    num2 = totalResult
    i += 1

print(liste)
