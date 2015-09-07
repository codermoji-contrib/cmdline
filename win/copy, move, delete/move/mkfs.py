import os
from random import choice, randint
from random_words import RandomWords

rw = RandomWords()

words = rw.random_words(count=10)

def makefile(name, ext='.txt', size=None):
    fullname = os.path.join('fs', name + ext)
    if not size:
        size = randint(5,10000)
    with open(fullname, 'w') as f:
        f.write('x' * size)

for word in words + ['secrets']:
    makefile(word)

os.makedirs(os.path.join(fs, 'secretsfolder'))
