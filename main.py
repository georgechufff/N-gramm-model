import re

def tuple_to_string(my_tuple):
     str = ' '.join(my_tuple)
     str += ' '
     return str

def generate_ngrams(s, n):

     # Разбитие предложения на массив непустых токенов
     tokens = [token for token in s.split() if len(token) != 0]

     # Use the zip function to help us generate n-grams
     # Concatentate the tokens into ngrams and return
     bigram = zip(*[tokens[i:] for i in range(n)])
     return list(bigram)

def MLE(s, word1, combination):
     # превращение кортежа в строку
     str = tuple_to_string(combination)
     return s.count(str + word1) / s.count(word1)

def main():
     file = open('model.txt', 'r', encoding='utf-8')
     s = [line[:-2] for line in file.readlines()]
     s = ' '.join(s)
     s = s.lower()

     # Удаление всех знаков препинания и замен их на пробел.
     s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)

     print(s)

     # создание массива различных n-грамм (в данном случе кортежи из n слов)
     ngrams = []
     for i in range(1, 4):
          ngrams.extend(generate_ngrams(s, i))

     ngrams_dict = {}

     # создание самоого словаря на основе полученных n-грамм
     for i in ngrams:
          words_n_probabilities = [(word[0], MLE(s, word[0], i)) for word in \
               generate_ngrams(s, 1) if tuple_to_string(i) + word[0] in s]
          # если для данной n-граммы можно найти слово
          if len(words_n_probabilities) != 0:
               #то добавляем n-грамму в словарь
               ngrams_dict[i] = words_n_probabilities

     # вывод словаря
     for i in ngrams_dict.keys():
          print(i,':', ngrams_dict[i])
     file.close()


if __name__ == '__main__':
     main()