import csv

cnt = 0
q = []
with open('books-en.csv') as books:
    rd = csv.reader(books)
    for i in rd:
        #print(''.join(i).split(';'))
        q.append(''.join(i).split(';'))
q.remove(q[0])


def auth(name):
    otv = []
    for i in q:
        if i[2] == name and int(i[3]) >= 2000:
            otv.append(i)
    for i in otv:
        print(i)

auth('Mark P. O. Morford') #Пример
books.close()