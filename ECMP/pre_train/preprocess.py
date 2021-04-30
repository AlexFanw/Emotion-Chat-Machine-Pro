import jieba
import numpy as np


def loadWordEmbedding(filename):
    vocab_embed = {}

    fr = open(filename, 'r', encoding="utf-8")

    line = fr.readline().strip()

    word_dim = int(line.split(' ')[1])
    print('word number:', int(line.split(' ')[0]), '\tword dimension:', int(line.split(' ')[1]))

    vocab_embed["unk"] = [1]*word_dim

    for line in fr:
        row = line.strip().split(' ')
        vocab_embed[row[0]] = [float(x) for x in row[1:]]
        print(row[0])
    fr.close()

    return vocab_embed


# 搜索word的向量值
def searchWordEmbeddiing(vocab_embed, word):
    if word not in vocab_embed:
        return vocab_embed["unk"]
    else:
        return vocab_embed[word]


def cosine_similarity(x, y):
    x = np.array(x)
    y = np.array(y)
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom


if __name__ == "__main__":
    vocab_embed = loadWordEmbedding("sgns.weibo.bigram-char")
    testline = "我爱中国"
    s = jieba.lcut("我爱中国")
    print(' '.join(s))
    for i in s:
        print(searchWordEmbeddiing(vocab_embed, i))
    print(searchWordEmbeddiing(vocab_embed, "范唯"))
    print(searchWordEmbeddiing(vocab_embed, "法国"))
    print(cosine_similarity(searchWordEmbeddiing(vocab_embed, "范唯"), searchWordEmbeddiing(vocab_embed, "法国")))
    print(cosine_similarity(searchWordEmbeddiing(vocab_embed, "布偶猫"), searchWordEmbeddiing(vocab_embed, "橘猫")))
