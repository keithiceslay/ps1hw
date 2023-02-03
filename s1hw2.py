# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print ('Введите X, Y и Z')
x = input()
y = input()
z = input()
is_true = not (x and y and z) == (not x and not y and not z)
print(is_true)