"""
удаляет первые слова в строке
например порядковые номера
"""
g=open(r"D:\Projects\Python\Х\Очистка порядковых номеров\готовый.txt", "w")
with open(r"D:\Projects\Python\Х\Очистка порядковых номеров\исходник.txt", "r") as f:
    l=""
    for line in f:
        h=line[(line.find(' ')+1):len(line)]
        l=l+h
g.write(l)
f.close()
g.close()

