import csv

cnt = 0
q = []
with open('books-en.csv') as books:
    rd = csv.reader(books)
    for i in rd:
        # print(''.join(i).split(';'))
        q.append(''.join(i).split(';'))
q.remove(q[0])


def nazv(qq):
    if len(q[qq][1]) > 30:
        return 1
    return 0


for i in range(len(q)):
    cnt += nazv(i)

print(cnt)
books.close()
