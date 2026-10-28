import csv

cnt = 0
P = [2, 4, 8, 16, 20, 21, 24, 25, 29, 31, 34, 40]
q = []
with open('books-en.csv') as books:
    rd = csv.reader(books)
    for i in rd:
        # print(''.join(i).split(';'))
        q.append(''.join(i).split(';'))
q.remove(q[0])


def wrt(cnt, st):
    otv.write(f'{cnt}:  {st[2]}.  {st[1]} - {st[3]}\n')


with open('third.txt', mode='w') as otv:
    for i in P:
        cnt += 1
        wrt(cnt, q[i])

otv.close()
books.close()
