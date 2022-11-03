from symspellpy import SymSpell, Verbosity

# suggestions = sym_spell.lookup_compound(p, max_edit_distance=2, ignore_term_with_digits=True)

while True:
    sym_spell = SymSpell()
    # p = 'vin'
    sym_spell.load_dictionary('dictionaries/dictionary.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
    sym_spell.load_bigram_dictionary('dictionaries/dictionary_bigram.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
    print("Enter text: ")
    text = input()
    suggestions = sym_spell.lookup(text, Verbosity.CLOSEST, max_edit_distance=2)
    for suggestion in suggestions:
        print(suggestion)