import re

def generate_ngrams(s, n):
     s = s.lower()

     # Удаление всех знаков препинания и замен их на пробел.
     s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)

     # Разбитие предложение на массив непустых токенов
     tokens = [token for token in s.split() if len(token) != 0]

     # Use the zip function to help us generate n-grams
     # Concatentate the tokens into ngrams and return
     bigram = zip(*[tokens[i:] for i in range(n)])
     return list(bigram)

if __name__ == '__main__':
     s = "Natural-language processing (NLP) is an area of computer science and artificial intelligence concerned with the interactions between computers and human (natural) languages."

     ngrams = []
     for i in range(2, len(s.split()) // 3):
          ngrams.extend(generate_ngrams(s, i))

     print(ngrams)
