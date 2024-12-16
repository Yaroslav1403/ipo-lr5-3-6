#Открываем файл, чтобы его прочитать
with open('text.txt', 'r', encoding = 'utf-8') as file:
    #Читаем содержимое файла
    text = file.read()
#Разобъём текст на слова, используя знаки препинания и пробелы  
words = text.split()
#Приводим слова к нижнему регистру и удаляем дубликаты с помощью множества
unique_words = set(word.lower().strip(',.?!";:[]()') for word in words)
#Открываем новый файл, куда будут записываться уникальные слова и числа 
with open('output.txt', 'w', encoding = 'utf-8') as output:
    #Записываем уникальные слова в файл
    for word in sorted(unique_words):
        #Отделяем каждое слово двумя пробелами и записываем в файл
        output.write(word + '  ')
#Выводим результат
print("Уникальные слова записаны в output.txt")
