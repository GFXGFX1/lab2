import csv

pub = []
q = []
with open('books-en.csv') as books:
    rd = csv.reader(books)
    for i in rd:
        # print(''.join(i).split(';'))
        q.append(''.join(i).split(';'))
q.remove(q[0])
q.sort(key=lambda x: int(x[-2]), reverse=True)

for i in q:
    if i[4] not in pub:
        pub.append(i[4])

print(pub)
for i in range(20):
    print(q[i][1], q[i][-2])
books.close()
