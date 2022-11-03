from keras.preprocessing.text import Tokenizer
import json


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
word_index = tokenizer.word_index
# jsonObject = json.loads(word_index)
# for c in word_index:
#     f = open("dictionary.txt", "a", encoding='utf-8')
#     line = f'{c} {word_index[c]}\n'
#     f.write(line)
#     f.close()
test = [
    "Khoảng cách chỉnh sửa là số thao tác trên mỗi ký tự trong chuỗi ban đầu để đưa ra một chuỗi ứng cử viên", 
    "Khoảg cáh chỉh sửa laf số tao tasc trn mỗi ký tự trng chũi bn đầu đểe đưa ra mootj chỗi ưngs cử vin"
    ]
sequences = tokenizer.texts_to_sequences(test)
print(sequences[0])
print(sequences[1])
