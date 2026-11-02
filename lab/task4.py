answer_list = {}
valute = []
# Открываем файл. Указываем кодировку windows-1251, чтобы русский текст не сломался
with open('currency.xml') as currency:
    for text in currency:  # Получаем из xml строки, которые можно прочитать
        valute = text.split('ID')  # Список строк
# for i in valute:
# print(i.split('>'))
# индекс 8 - название<.. индекс 4 - Charcode<...
for line in valute:
    if '<Name>' in line and '<CharCode>' in line:  # Некоторые строки полупустые, поэтому нужна проверка
        linesplit = line.split('>')
        Charcd = ''.join(linesplit[4].split('<')[0])
        namev = ''.join(linesplit[8].split('<')[0])
        answer_list[namev] = Charcd

print(answer_list)
