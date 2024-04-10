word=input("введи слово")
#переменные для подсчета количетсва каждой глассной
quanity_a=0
quanity_e=0
quanity_i=0
quanity_o=0
quanity_u=0
#цикл который ,берет по букве из переменной word и првоеряет равна ли она рдной из гласных, в случае если равна прибавляет к счетчику этой глассной 1
for i in word:
    if i=='a':
        quanity_a+=1
    if i=='e':
        quanity_e+=1
    if i=='i':
        quanity_i+=1
    if i=='o':
        quanity_o+=1
    if i=='u':
        quanity_u+=1
#ввыводим количество каждой гласной
print("Количество a:", quanity_a)
print("Количество e:", quanity_e)
print("Количество i:", quanity_i)
print("Количество o:", quanity_o)
print("Количество u:", quanity_u)
#считаем сумму гласных
summ_glas=quanity_a+quanity_e+quanity_i+quanity_o+quanity_u
#считаем количество не гласных вычитая из длины слова сумму глассных и выводим данные по гласным и не гласным
summ_neglass=len(word)-summ_glas
print("Количество глассных:", summ_glas)
print("Количество неглассных:", summ_neglass)