#!/usr/bin/env python3
"""
parse_pun_pairs.py
This scripts parses the Semeval2017 Task 7 files to retrieve pun pairs.
Pun pairs are stored in json format.

output format:

"puns_pairs": [
    {
        "id": id,
        "pun_word": pun_word,
        "alter_word": alter_word,
    },
]
"""
__author__ = "Ernest McCarter"


import json

GOLD_PATHS = [
    "../data/semeval2017_task7/data/test/subtask3-heterographic-test.gold",
    "../data/semeval2017_task7/data/test/subtask3-homographic-test.gold",
]
OUTPUT_FILE = "../data/csurgen/pun_pairs.json"


# parse_gold_file(path)
# For the given path, extract the pun word, alternative word, and the
# unique identifier
def parse_gold_file(path):
    puns = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            split_line = line.strip().split()
            sent_id = '_'.join(split_line[0].split('_')[:2])
            pun_word = split_line[1].split('%')[0]
            alter_word = split_line[2].split('%')[0]
            puns.append(
                {
                    "id": sent_id,
                    "pun_word": pun_word,
                    "alter_word": alter_word,
                }
            )
    return puns


# parse_gold_files(paths)
# For each path in the given paths parse the pun pair
# and return it in a dictionary format.
def parse_gold_files(paths):
    puns_pairs = {
        "puns_pairs": []
    }
    for path in paths:
        puns_pairs["puns_pairs"].extend(parse_gold_file(path))
    return puns_pairs


# main()
# Parse all given pun files and extract pun pairs.
# Store these pun pairs in a json file.
def main():
    # get pun pairs from Semeval_2017 Task 7
    puns_pairs = parse_gold_files(GOLD_PATHS)
    json_puns_pairs = json.dumps(puns_pairs)

    # store items
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(json_puns_pairs)


if __name__ == "__main__":
    main()
