#!/usr/bin/env python3
"""
generate_context_words.py
This generates random words that will be used for context.
These words will only be nouns and verbs.
"""
__author__ = "Ernest McCarter"

import json
import random

TOTAL_WORD_COUNT = 500 # number of unique words to be selected
WORD_DICTIONARY = "../data/English-Words-Definitions\
-and-Parts-of-Speech/wordDictionary.txt"
OUTPUT_FILE = "../data/csurgen/context_words.json"

# generate_seed_context_words(path)
# generates list of random nouns and verbs
def generate_seed_context_words(path):
    # read n random words from dictionary
    words = []
    with open(path, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    # remove any non nouns and non verbs
    for line in lines:
        split_line = line.strip().split("|")
        if split_line[1] != "noun" and split_line[1] != "verb":
            continue
        words.append(split_line[0])

    # randomize list order
    random.shuffle(words)

    # get n words
    words = words[:TOTAL_WORD_COUNT]

    return words



# main()
# Generates random words
# Stores in json file
def main():
    random_context_words = generate_seed_context_words(WORD_DICTIONARY)
    random_context_words_json = json.dumps(
        {"words": random_context_words}
    )

    # store item
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(random_context_words_json)

if __name__ == "__main__":
    main()
