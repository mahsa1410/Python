#input: a dictionary and then a Sentence => output: Translated sentence
dictionary = dict()
number = int(input())
for i in range (number):
    new_word = input().lower().split()
    dictionary[new_word[0]] = new_word[1]

sentence = (input().lower().split())
translated_sentence = ''
for i in sentence:
    translated_sentence =translated_sentence+ ' ' + dictionary.get( i , i )
print (translated_sentence)