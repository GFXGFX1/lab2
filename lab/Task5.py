import csv

pub = []
q = []
with open('books-en.csv') as books:
    rd = csv.reader(books)
    for i in rd:
        # print(''.join(i).split(';'))
        q.append(''.join(i).split(';'))
q.remove(q[0])

for i in q:
    if i[4] not in pub:
        pub.append(i[4])

print(pub)
books.close()
