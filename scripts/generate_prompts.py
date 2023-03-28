#!/usr/bin/env python3
"""
This script uses context sets and pun pairs to generate
GPT prompts for creating seeding sentences.

output:
{
    "id": id,
    "pun_pair": {
        "id": pun_pair_id,
        "pun_word": pun_word,
        "alt_word": alt_word,
    },
    "context": {
        "id": context_id,
        "context_word": context_word
        "synonyms": synonyms, 
    }
    "prompt1": prompt1,
    "prompt2": prompt2,
    "seed_sentence_count": seed_sentence_count
}
"""
__author__ = "Ernest McCarter"

import json
import random


CONTEXT_FILE = "../data/csurgen/contexts.json"
PUN_PAIR_FILE = "../data/csurgen/pun_pairs.json"
OUTPUT_FILE = "../data/csurgen/prompts.json"
SEED_SENTENCE_COUNT = 10
PROMPT_COUNT = 100
PROMPT_1 = """Generate {n} sets of 2 sentences each containing the word \
'{alternative_word}' and at least one of the following phrases: \
{context}."""
PROMPT_2 = """Generate {n} sets of 2 sentences each containing the word \
'{alternative_word}' towards the end and at least one of the following phrases: \
{context}."""


# # --- FILE READING/WRITING --- # #

def get_pun_pairs(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readline()
    pun_pairs = json.loads(lines)
    return pun_pairs["puns_pairs"]

def get_contexts(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readline()
    contexts = json.loads(lines)
    return contexts["contexts"]

def store_information(path, item):
    item_json = json.dumps(item)
    with open(path, "w", encoding="utf-8") as file:
        file.write(item_json)


# # --- PROMPT GENERATION --- # #

# format list of context words for prompt
def format_context_words(context_words):
    # add or to the final word
    context_words[-1] = "or " + context_words[-1]
    return ', '.join(context_words)

# generates a prompt string
def generate_prompt(
        prompt_template,
        alternative_word,
        formatted_context,
        seed_sentence_count
    ):
    return prompt_template.format(
        n=seed_sentence_count,
        alternative_word=alternative_word,
        context=formatted_context
    )

# generates a prompt object
def generate_prompt_object(
        id_num,
        pun_pair,
        context,
        seed_sentence_count
    ):

    formatted_context = format_context_words(context["synonyms"])
    prompt_object = {
        "id": id_num,
        "pun_pair": pun_pair,
        "context": context,
        "prompt1": generate_prompt(
                    PROMPT_1,
                    pun_pair["alter_word"],
                    formatted_context,
                    seed_sentence_count
                ),
        "prompt2": generate_prompt(
                    PROMPT_2,
                    pun_pair["alter_word"],
                    formatted_context,
                    seed_sentence_count
                ),
        "seed_sentence_count": seed_sentence_count,
    }
    return prompt_object

# generates a dictionary containing a list of prompts
def generate_prompts_objects(
        pun_pair_list,
        context_list,
        prompt_count,
        seed_sentence_count
    ):

    prompts_object = {"prompts": []}
    for i in range(prompt_count):
        # puns and contexts are chosen randomly
        pun_pair = random.choice(pun_pair_list)
        context = random.choice(context_list)
        prompt_obj = generate_prompt_object(
            id_num=i,
            pun_pair=pun_pair,
            context=context,
            seed_sentence_count=seed_sentence_count,
            )
        prompts_object["prompts"].append(prompt_obj)

    return prompts_object

# generates prompts
def main():
    # retrieve puns and context
    pun_pair_list = get_pun_pairs(PUN_PAIR_FILE)
    context_list = get_contexts(CONTEXT_FILE)

    # generate propmts
    prompts_object = generate_prompts_objects(
        pun_pair_list,
        context_list,
        PROMPT_COUNT,
        SEED_SENTENCE_COUNT
    )

    # store prompts
    store_information(OUTPUT_FILE, prompts_object)

if __name__ == "__main__":
    main()
