import random


def get_jokes(n, uniq=False):

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if uniq:
        n = min(n, len(nouns), len(adverbs), len(adjectives))

    jokes = []
    for i in range(n):
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        jokes.append(joke)

        if uniq:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
    return jokes


print(get_jokes(7))
print(get_jokes(7, False))
print(get_jokes(7, True))
