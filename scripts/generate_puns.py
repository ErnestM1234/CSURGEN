import os
import argparse

COMMAND="""python generate_pun.py data/bookcorpus/edit/bin/data \\
	--path models/bookcorpus/edit/delete/checkpoint_best.pt \\
	--beam 20 --nbest 1 --unkpen 100 \\
	--system rule --task edit \\
	--retriever-model models/bookcorpus/retriever.pkl --doc-file data/bookcorpus/raw/books1/epubtxt/zone-defense.epub.txt \\
	--lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \\
	--skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \\
	--num-candidates 10000 --num-templates 10000 \\
	--num-topic-word 100 --type-consistency-threshold 0.3 \\
	--pun-words data/semeval/hetero/dev.json \\
	--outdir results/semeval/hetero/dev/rule \\
	--scorer random \\
	--max-num-examples 100"""


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--doc-file', nargs='+', help='training corpus')
    print(COMMAND)


if __name__ == "__main__":
    main()


# cat results/semeval/hetero/dev/rule/results.json