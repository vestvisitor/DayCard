import pandas as pd
import random
from collections import namedtuple

prompts = pd.read_csv("/home/michael/PycharmProjects/DayCard/backend/dataset.csv")
quotes = pd.read_json("/home/michael/PycharmProjects/DayCard/backend/quotes.jsonl", lines=True)

get_random_row = lambda i1, i2: random.randint(i1, i2)

Quote = namedtuple('Quote', ['text', 'author'])


def get_prompt() -> str:
    row = get_random_row(0, 1039791)
    prompt = prompts['Prompt'][row]

    return prompt


def get_quote():
    row = get_random_row(0, 2508)
    quote = quotes['quote'][row]
    author = quotes['author'][row]

    return Quote(text=quote, author=author)


if __name__ == '__main__':
    pass
