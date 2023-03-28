#!/usr/bin/env python3
"""
This script requests synonyms for a given context word.
This is done using API Ninja's thesaurus API. Because this
program uses web requests, it will take longer to run corresponding
to number of contexts that need to be fulfilled.
"""
__author__ = "Ernest McCarter"

import json
import os
import requests
from dotenv import load_dotenv
load_dotenv()

CONTEXT_COUNT = 100 # number of desired contexts
CONTEXTS_WORDS = "../data/csurgen/context_words.json"
OUTPUT_FILE = "../data/csurgen/contexts.json"
API_KEY = os.environ.get('API_NINJA_KEY')


def get_synonyms(context_words):
    # TODO: send requests in parallel
    context_synonyms = []
    for i, word in enumerate(context_words):
        api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
        if response.status_code == 200:
            response_json = json.loads(response.text)
            synonyms = response_json["synonyms"]
            synonyms.append(word)
            synonyms = [
                synonym.replace("_", " ")
                for synonym in synonyms
            ]
            context_synonyms.append({
                "id": i,
                "word": word,
                "synonyms": synonyms
            })
        else:
            print("Error:" + str(response.status_code) + response.text)
            print(str(response))
    return context_synonyms

def get_context_words(path):
    with open(path, "r", encoding="utf-8-sig") as file:
        lines = file.readline()
    words = json.loads(lines)
    return words["words"]

def main():
    words = get_context_words(CONTEXTS_WORDS)
    contexts = get_synonyms(words[:CONTEXT_COUNT])
    contexts_json = json.dumps({
        "contexts": contexts
    })

    # store item
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(contexts_json)

if __name__ == "__main__":
    main()
