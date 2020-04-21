'''

import gensim
import os

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()


sentences = MySentences('/some/directory')  # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences)


word1='物流系统'
word2='信息系统'
from gensim.models import word2vec

sentences = word2vec.Text8Corpus('idf.txt')

model = word2vec.Word2Vec(sentences)



with open('dic.txt','r+',encoding='UTF-8') as foo:
    for line in foo.readlines():
        if word1 in line:
            continue
    else:
        foo.write(word1)
        foo.write(' ')

with open('dic.txt','r+',encoding='UTF-8') as foo:
    for line in foo.readlines():
        if word2 in line:
            continue
    else:
        foo.write(word2)
        foo.write(' ')

sim=model.similarity(word1,word2)
print(sim)
'''

import numpy as np
from gensim.models import word2vec

'''
# 加载语料
sentences = word2vec.Text8Corpus('dic.txt')

# 训练模型
model = word2vec.Word2Vec(sentences,min_count = 1)
word="物资信息"

try:
    v1=np.array(model[word])

except:
    print("Error")
    fo = open("dic.txt", "a", encoding='utf-8')
    fo.write(word)
    fo.write("\n")
    fo.close()

finally:
    sentences = word2vec.Text8Corpus('dic.txt')
    v1 = np.array(model[word])
print(v1)
'''

def get_word2vec(word):
    sentences = word2vec.Text8Corpus('dic.txt')
    model = word2vec.Word2Vec(sentences, min_count=1)
    try:
        v1 = np.array(model[word])

    except:
        fo = open("dict.txt", "a", encoding='utf-8')
        fo.write(word)
        fo.write("\n")
        fo.close()

    finally:
        sentences = word2vec.Text8Corpus('dict.txt')
        model = word2vec.Word2Vec(sentences, min_count=1)
        v1 = np.array(model[word])
    return v1

print(get_word2vec("信息系统"))