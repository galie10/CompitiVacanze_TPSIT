from string import ascii_lowercase
def is_pangram(sentence):
    cr_frase = set(sentence.lower())
    cr_pangram = set(ascii_lowercase)
    if cr_pangram - cr_frase == set([]):
        return True
    return False