# Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

numbers = int(input('Введите трехзначное число: '))
second = numbers//10;
secomd2 = second%10;

print(f"Сумма введенных чисел равен {numbers%10 + numbers//100 + secomd2}")
