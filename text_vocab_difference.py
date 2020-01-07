#encoding:utf-8
import nltk 
from nltk import *
from nltk.corpus import gutenberg

def unusual_words(text):
    #lower() 方法只对ASCII编码，即‘A-Z’有效，对于其它语言中把大写转换为小写的情况无效
    text_vocab=set(w.lower() for w in text if w.isalpha())
    english_vocab=set(w.lower() for w in nltk.corpus.words.words()) 
    unusual=text_vocab.difference(english_vocab)    #求差集
    return sorted(unusual)


print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
print(unusual_words(nltk.corpus.nps_chat.words()))
