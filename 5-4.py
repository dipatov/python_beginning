d = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

fw = open('file4_res.txt', 'w')
fr = open('file4.txt', 'r')

res = fr.read()
for word_from, word_to in d.items():
    res = res.replace(word_from, word_to)

fw.write(res)

fw.close()
fr.close()
