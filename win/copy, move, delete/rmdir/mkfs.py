import os

os.makedirs(os.path.join('fs', 'temp'))
os.makedirs(os.path.join('fs', 'backups'))

from random import randint
from random_words import RandomWords
rw = RandomWords()
words = rw.random_words(count=10)

for w in words:
    filename = os.path.join(fs, 'backups', w + '.txt')
    with open(filename, 'w') as f:
        f.write('x' * randint(5, 10000))

