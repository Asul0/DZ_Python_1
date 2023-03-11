# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#*Пример:*

#385916 -> yes
#123456 -> no


num = int(input('Введите 6и значный билет: '))
first_three_nums = num//1000
first_num = first_three_nums//100
second = first_three_nums//10;
secomd_num = second%10;
three_num = first_three_nums%10

first3 = first_num +secomd_num +three_num

last_three_nums = num%1000
first_num2 = last_three_nums//100
second2 = last_three_nums//10;
secomd_num2 = second2%10;
three_num2 = last_three_nums%10

last3 = first_num2+secomd_num2 +three_num2

if first3 == last3:
   print('Ура, вы победитель!!!')
else :
   print('Повезет, в след раз)')  




