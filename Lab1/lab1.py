
# from google.colab import drive
# drive.mount('/content/drive')

import nltk
from nltk.tokenize import word_tokenize

from nltk import sent_tokenize

# !pip install pymorphy2

import pymorphy2

nltk.download('punkt')
print(word_tokenize("Типа текст."))

print(sent_tokenize("Типа текст. Не, серьёзно."))

m = pymorphy2.MorphAnalyzer()
w = m.parse("университетов")[0]
print(w.normal_form)

# root = '/content/drive/MyDrive/Lab_NLP/Lab1/'
filename = 'text.txt'

f = open(filename)

text = f.read()
print(text)

f.close()

all_word = word_tokenize(text)

all_sentence = sent_tokenize(text)
all_sentence

def is_adjective_or_noun(word):
  parsed_word = m.parse(word)[0]
  return 'NOUN' in parsed_word.tag or 'ADJF' in parsed_word.tag or 'ADJS' in parsed_word.tag

def check_gender_number_cases(word1, word2):
  word1_parsed = m.parse(word1)[0].tag
  word2_parsed = m.parse(word2)[0].tag

  word1_gender = word1_parsed.gender
  word2_gender = word2_parsed.gender

  word1_number = word1_parsed.number
  word2_number = word2_parsed.number

  word1_case = word1_parsed.case
  word2_case = word2_parsed.case

  return (word1_gender == word2_gender) and (word1_number == word2_number) and (word1_case == word2_case)

# ['Эта книга адресована всем, кто изучает русский язык.']
for sentence in all_sentence:
  print(f"Sentence: {sentence}")
  word_in_sentence = word_tokenize(sentence)

  lemmas = []
  for word in word_in_sentence:
    parsed_word = m.parse(word)[0]
    if is_adjective_or_noun(word):
        lemmas.append(parsed_word.normal_form)
  matching_pairs = []
  for i in range(len(lemmas) - 1):
    currentWord = lemmas[i]
    nextWord = lemmas[i + 1]
    if is_adjective_or_noun(currentWord) and is_adjective_or_noun(nextWord) and check_gender_number_cases(currentWord, nextWord):
      currentWord_norm = m.parse(currentWord)[0].normal_form
      nextWord_norm = m.parse(nextWord)[0].normal_form
      matching_pairs.append((currentWord_norm, nextWord_norm))

  for pair in matching_pairs:
    print(" ".join(pair))

  print()