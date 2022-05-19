from random import randrange

def get_jokes(n):
    joke_list = []
    for i in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))], adjectives[randrange(len(adjectives))]])
        joke_list.append(joke)
    print(joke_list)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(5)