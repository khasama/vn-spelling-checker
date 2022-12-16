from symspellpy import SymSpell, Verbosity

# while True:
#     sym_spell = SymSpell()
#     sym_spell.load_dictionary('dictionaries/dictionary.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
#     sym_spell.load_bigram_dictionary('dictionaries/dictionary_bigram.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
#     print("Enter text: ")
#     text = input()
#     suggestions = sym_spell.lookup(text, Verbosity.CLOSEST)
#     for suggestion in suggestions:
#         print(suggestion)

def get_correct_text(text):
    sym_spell = SymSpell()
    sym_spell.load_dictionary('dictionaries/dictionary.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
    sym_spell.load_bigram_dictionary('dictionaries/dictionary_bigram.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
    suggestions = sym_spell.lookup(text, Verbosity.CLOSEST)
    for suggestion in suggestions:
        print(suggestion)