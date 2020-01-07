#encoding:utf-8
import nltk 

def plural(word):
    if word.endswith('y'): 
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']: 
        return word + 'es'
    elif word.endswith('an'): 
        return word[:-2] + 'en'
    else:
        return word + 's'

# w_1 = plural('man')
# w_2 = plural('candy')
# w_3 = plural('story')

# print(w_1)
# print(w_2)
# print(w_3)

