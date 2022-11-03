arrChar = []
arrIndex = []
# new_dictionary = []

def merge_dictionary():
    file_o = open("dictionary_1_2.txt", "r", encoding='utf-8')
    file_t = open("dictionary-3.txt", "r", encoding='utf-8')
    old_dictionary_o = file_o.read().split("\n")
    old_dictionary_t = file_t.read().split("\n")
    print(len(old_dictionary_o))

    for char in old_dictionary_o:
        arrChar.append(char.split()[0])
        arrIndex.append(char.split()[1])
        
    for i in old_dictionary_t:
        c = i.split()[0]
        index = i.split()[1]
        if c in arrChar:
            old_dictionary_o[arrChar.index(c)] = f'{c} {int(arrIndex[arrChar.index(c)])+int(index)}'
        else:
            old_dictionary_o.append(f"{c} {index}")

    print(len(old_dictionary_o))

    for t in old_dictionary_o:
        f = open("dictionary.txt", "a", encoding='utf-8')
        f.write(f'{t}\n')
        f.close()

def merge_bigram_dictionary():
    file_o = open("dictionary_bigram_1_2.txt", "r", encoding='utf-8')
    file_t = open("dictionary-bigram-3.txt", "r", encoding='utf-8')
    old_dictionary_o = file_o.read().split("\n")
    old_dictionary_t = file_t.read().split("\n")
    print(len(old_dictionary_o))
    # print(len(old_dictionary_t))

    for char in old_dictionary_o:
        # print(char)
        arrChar.append(f'{char.split()[0]} {char.split()[1]}')
        arrIndex.append(char.split()[2])
        
    for i in old_dictionary_t:
        c = f'{i.split()[0]} {i.split()[1]}'
        index = i.split()[2]
        if c in arrChar:
            old_dictionary_o[arrChar.index(c)] = f'{c} {int(arrIndex[arrChar.index(c)])+int(index)}'
        else:
            old_dictionary_o.append(f"{c} {index}")

    print(len(old_dictionary_o))
    for t in old_dictionary_o:
        f = open("dictionary_bigram.txt", "a", encoding='utf-8')
        f.write(f'{t}\n')
        f.close()

merge_bigram_dictionary()