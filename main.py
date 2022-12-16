from keras.preprocessing.text import Tokenizer
from symspellpy import SymSpell, Verbosity
import json

def get_wrong_text(text):
    single_characters = []

    with open("vietnam74K.txt", 'r', encoding='utf-8') as f:
        data = f.read().split("\n")
        for i in data:
            arr_character = i.split(" ")
            if len(arr_character) == 1:
                character = arr_character[0].lower()
                single_characters.append(character)

    tokenizer = Tokenizer(oov_token="<OOV>")
    tokenizer.fit_on_texts(single_characters)
    # word_index = tokenizer.word_index
    # jsonObject = json.loads(word_index)
    # for c in word_index:
    #     f = open("dictionary.txt", "a", encoding='utf-8')
    #     line = f'{c} {word_index[c]}\n'
    #     f.write(line)
    #     f.close()
    arr_text = text.split(' ')
    wrong_text = []
    for i in arr_text:
        sequences = tokenizer.texts_to_sequences([i])
        if sequences[0][0] == 1:
            # print(i)
            wrong_text.append(i)
    
    return wrong_text

def get_correct_text(text):
    sym_spell = SymSpell()
    sym_spell.load_dictionary('dictionaries/dictionary.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
    sym_spell.load_bigram_dictionary('dictionaries/dictionary_bigram.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
    suggestions = sym_spell.lookup(text, Verbosity.CLOSEST)
    arr_suggest = []
    i = 0
    for suggestion in suggestions:
        if i == 5: break
        suggest = str(suggestion).split(',')
        arr_suggest.append(suggest[0])
        i += 1
    
    return arr_suggest

# get_wrong_text('Khoảg cáh chỉh sửa laf số tao tasc trn mỗi ký tự trng chũi bn đầu đểe đưa ra mootj chỗi ưngs cử vin')
# get_correct_text('Khoảg')
