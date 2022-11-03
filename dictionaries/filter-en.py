from keras.preprocessing.text import Tokenizer

single_characters = []
tokenizer = Tokenizer(oov_token="<OOV>")
with open("../vietnam74K.txt", 'r', encoding='utf-8') as f:
    data = f.read().split("\n")
    for i in data:
        arr_character = i.split(" ")
        if len(arr_character) == 1:
            character = arr_character[0].lower()
            single_characters.append(character)

tokenizer.fit_on_texts(single_characters)
word_index = tokenizer.word_index
# print(word_index)

def filter_dictionary():
    with open("raw-dictionary-3.txt", 'r', encoding='utf-8') as f:
        data = f.read().split("\n")
        for i in data:
            arr_character = i.split(" ")
            text = [arr_character[0]]
            sequence = tokenizer.texts_to_sequences(text)[0]
            if not 1 in sequence:
                file = open("dictionary-3.txt", "a", encoding='utf-8')
                file.write(i + '\n')
                file.close()


def filter_bigram_dictionary():
    with open("raw-dictionary-bigram-3.txt", 'r', encoding='utf-8') as f:
        data = f.read().split("\n")
        for i in data:
            try:
                arr_character = i.split()
                char_one = arr_character[0].split('\'')[1]
                char_two = arr_character[1].split('\'')[1]
                index = arr_character[2]
                text = [f'{char_one} {char_two}']
                sequence = tokenizer.texts_to_sequences(text)[0]
                if not 1 in sequence:
                    file = open("dictionary-bigram-3.txt", "a", encoding='utf-8')
                    file.write(f'{char_one} {char_two} {index}\n')
                    file.close()
            except:
                print(f'Error {i}')
            
filter_bigram_dictionary()
# filter_dictionary()