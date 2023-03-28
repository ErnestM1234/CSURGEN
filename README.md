# CSURGEN
Context Based Pun Generation Model





python -m pungen.wordvec.preprocess --data-dir data/bookcorpus/skipgram \
	--corpus sample_data/bookcorpus/raw/train.txt \
	--min-dist 5 --max-dist 10 --threshold 80 \
	--vocab data/bookcorpus/skipgram/dict.txt


python generate_pun.py data/bookcorpus/edit/bin/data \
	--path models/bookcorpus/edit/delete/checkpoint_best.pt \
	--beam 20 --nbest 1 --unkpen 100 \
	--system rule --task edit \
	--retriever-model models/bookcorpus/retriever.pkl --doc-file data/test.txt \
	--lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \
	--skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
	--num-candidates 500 --num-templates 100 \
	--num-topic-word 100 --type-consistency-threshold 0.3 \
	--pun-words data/semeval/hetero/dev.json \
	--outdir results/semeval/hetero/dev/rule \
	--scorer random \
	--max-num-examples 100




python -m pungen.wordvec.train --weights --data data/bookcorpus/skipgram/train.bin \
    --save_dir models/bookcorpus/skipgram \
    --mb 3500 --epoch 15 \
    --vocab data/bookcorpus/skipgram/dict.txt




https://worksheets.codalab.org/rest/bundles/0xbfb2e7cdcb27494e893010b265894177/contents/blob/retriever.pkl

['data/bookcorpus/raw/sent.tokenized.txt']


missing sent.tokenized.txt




python -m pungen.wordvec.preprocess --data-dir data/bookcorpus/skipgram \
	--corpus data/bookcorpus/raw/train.txt \
	--min-dist 5 --max-dist 10 --threshold 80 \
	--vocab data/bookcorpus/skipgram/dict.txt


data/bookcorpus/raw/books1/epubtxt
data/bookcorpus/raw/books1/epubtxt/zone-defense.epub.txt


python -m pungen.wordvec.preprocess
	this takes in a tokenized file and stores vocab and processed data

### USE GPT
langchain chat gpt
documentation
dont use GPT3


python scripts/preprocess_raw_text.py \
	--input data/bookcorpus/raw/books1/epubtxt/zone-defense.epub.txt \
	--output test.txt

nano scripts/preprocess_raw_text.py




- pip install -U spacy==2.0.11 (2.2.4)
	en-core-web-sm 2.2.0 has requirement spacy>=2.2.0, but you'll have spacy 2.0.11 which is incompatible. 
- pip install -U thinc==6.10.3  (7.4.0)
	spacy 2.2.4 has requirement cymem<2.1.0,>=2.0.2, but you'll have cymem 1.31.2 which is incompatible.
	spacy 2.2.4 has requirement preshed<3.1.0,>=3.0.2, but you'll have preshed 1.0.1 which is incompatible.
	spacy 2.2.4 has requirement thinc==7.4.0, but you'll have thinc 6.10.3 which is incompatible.
	- pip install -U spacy==2.0.11 (2.2.4)
		en-core-web-sm 2.2.0 has requirement spacy>=2.2.0, but you'll have spacy 2.0.11 which is incompatible.
	- python -m spacy download en_core_web_sm
	  (pip install -U en_core_web_sm==2.0.0 (2.2.0))


# normal
python generate_pun.py data/bookcorpus/edit/bin/data \
	--path models/bookcorpus/edit/delete/checkpoint_best.pt \
	--beam 20 --nbest 1 --unkpen 100 \
	--system rule --task edit \
	--retriever-model models/bookcorpus/retriever.pkl --doc-file data/bookcorpus/raw/sent.tokenized.txt \
	--lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \
	--skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
	--num-candidates 500 --num-templates 100 \
	--num-topic-word 100 --type-consistency-threshold 0.3 \
	--pun-words data/semeval/hetero/dev.json \
	--outdir results/semeval/hetero/dev/rule \
	--scorer random \
	--max-num-examples 100


# raw text for --doc-file
python generate_pun.py data/bookcorpus/edit/bin/data \
	--path models/bookcorpus/edit/delete/checkpoint_best.pt \
	--beam 20 --nbest 1 --unkpen 100 \
	--system rule --task edit \
	--retriever-model models/bookcorpus/retriever.pkl --doc-file data/bookcorpus/raw/books1/epubtxt/zone-defense.epub.txt \
	--lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \
	--skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
	--num-candidates 500 --num-templates 100 \
	--num-topic-word 100 --type-consistency-threshold 0.3 \
	--pun-words data/semeval/hetero/dev.json \
	--outdir results/semeval/hetero/dev/rule \
	--scorer random \
	--max-num-examples 100
# THIS WORKS!!!!!!!!!!

{"id": "het_24", "tokens": ["we", "welcome", "you", "with", "open", "psalms", "."], "pun_word": "psalms", "alter_word": "arm", "pun_word_id": 5}
# HOW IT WORKS
	RAW TEXT: --doc-file
		ie: --doc-file data/bookcorpus/raw/books1/epubtxt/zone-defense.epub.txt \
	PUNS (JSON): --pun-words
		ie: --pun-words data/semeval/hetero/dev.json \


#!/bin/bash
# Ask the user for their name
echo Hello, who am I talking to?
read varname
echo It\'s nice to meet you $varname


python generate_pun.py data/bookcorpus/edit/bin/data \
--path models/bookcorpus/edit/delete/checkpoint_best.pt \
--beam 20 --nbest 1 --unkpen 100 \
--system rule --task edit \
--retriever-model models/bookcorpus/retriever.pkl \
--doc-file data/bookcorpus/raw/books1/epubtxt/narrator-magazine-blue-mountains-winter-2011.epub.txt data/bookcorpus/raw/books1/epubtxt/zone-the-end-and-the-beginning.epub.txt data/bookcorpus/raw/books1/epubtxt/narrator-magazine-central-tablelands-spring-2011.epub.txt data/bookcorpus/raw/books1/epubtxt/zorana-confessions-of-a-small-town-super-villain.epub.txt \
--lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \
--skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
--num-candidates 500 --num-templates 100 \
--num-topic-word 100 --type-consistency-threshold 0.3 \
--pun-words data/semeval/hetero/dev.json \
--outdir results/semeval/hetero/dev/rule \
--scorer random \
--max-num-examples 100


data/bookcorpus/raw/books1/epubtxt/narrator-magazine-blue-mountains-winter-2011.epub.txt  
data/bookcorpus/raw/books1/epubtxt/zone-the-end-and-the-beginning.epub.txt
data/bookcorpus/raw/books1/epubtxt/narrator-magazine-central-tablelands-spring-2011.epub.txt
data/bookcorpus/raw/books1/epubtxt/zorana-confessions-of-a-small-town-super-villain.epub.txt



python generate_pun.py data/bookcorpus/edit/bin/data \
	--path models/bookcorpus/edit/delete/checkpoint_best.pt \
	--beam 20 --nbest 1 --unkpen 100 \
	--system rule --task edit \
	--retriever-model models/bookcorpus/retriever.pkl --doc-file templates.txt \
	--lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \
	--skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
	--num-candidates 500 --num-templates 100 \
	--num-topic-word 100 --type-consistency-threshold 0.3 \
	--pun-words puns.json \
	--outdir results/semeval/hetero/dev/rule \
	--scorer random \
	--max-num-examples 100


{"id": "het_24", "tokens": ["we", "welcome", "you", "with", "open", "psalms", "."], "pun_word": "psalms", "alter_word": "arm", "pun_word_id": 5}


python generate_pun.py data/bookcorpus/edit/bin/data \
	--path models/bookcorpus/edit/delete/checkpoint_best.pt \
	--beam 20 --nbest 1 --unkpen 100 \
	--system rule --task edit \
	--retriever-model models/bookcorpus/retriever.pkl --doc-file data/bookcorpus/raw/books1/epubtxt/to-kill-a-mocking-dog.epub.txt \
	--lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \
	--skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
	--num-candidates 500 --num-templates 100 \
	--num-topic-word 100 --type-consistency-threshold 0.3 \
	--pun-words data/semeval/hetero/dev.json \
	--outdir results/semeval/hetero/dev/rule \
	--scorer random \
	--max-num-examples 100





python generate_pun.py data/bookcorpus/edit/bin/data \
	--path models/bookcorpus/edit/delete/checkpoint_best.pt \
	--beam 20 --nbest 1 --unkpen 100 \
	--system rule --task edit \
	--retriever-model models/bookcorpus/retriever.pkl --doc-file data/bookcorpus/raw/books1/epubtxt/zone-defense.epub.txt \
	--lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \
	--skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
	--num-candidates 500 --num-templates 100 \
	--num-topic-word 100 --type-consistency-threshold 0.3 \
	--pun-words data/semeval/hetero/dev.json \
	--outdir results/semeval/hetero/dev/rule \
	--scorer random \
	--max-num-examples 100

	RuntimeError: Attempting to deserialize object on a CUDA device but torch.cuda.is_available() is False. If you are running on a CPU-only machine, please use torch.load with map_location=torch.device('cpu') to map your storages to the CPU.



# THIS ONE WORKS ! VVV
PYTHONPATH=. python scripts/parsed_to_tokenized.py --input data/train.txt --output /tmp/train.tokenized.txt;
PYTHONPATH=. python scripts/parsed_to_tokenized.py --input data/valid.txt --output /tmp/valid.tokenized.txt;
cat /tmp/train.tokenized.txt /tmp/valid.tokenized.txt > /tmp/sent.tokenized.txt;
cat /tmp/sent.tokenized.txt;
NLTK_DATA=nltk_data
python generate_pun.py combiner-data \
    --path combiner/models/checkpoint_best.pt \
    --beam 20 --nbest 1 --unkpen 100 --task edit --system rule \
    --retriever-model models/bookcorpus/retriever.pkl \
    --doc-file /tmp/sent.tokenized.txt \
    --skipgram-model skipgram/dict.txt skipgram/model.pt \
    --num-candidates 500 --num-templates 100 \
    --num-topic-word 100 --type-consistency-threshold 0.3 \
    --pun-words data/semeval/hetero/dev.json \
    --outdir ./ \
    --scorer random --max-num-examples 100 \
    --word-counts-path data/bookcorpus/skipgram/dict.txt


	map_location=torch.device('cpu'))

	generate.py:32
	sgns.load_state_dict(torch.load(model_path))
	sgns.load_state_dict(torch.load(model_path), map_location=torch.device('cpu'))



	python -m pungen.wordvec.train --weights --data data/bookcorpus/skipgram/train.bin \
    --save_dir models/bookcorpus/skipgram \
    --mb 3500 --epoch 15 \
    --vocab data/bookcorpus/skipgram/dict.txt




PYTHONPATH=. python scripts/parsed_to_tokenized.py --input data/train.txt --output /tmp/train.tokenized.txt;
PYTHONPATH=. python scripts/parsed_to_tokenized.py --input data/valid.txt --output /tmp/valid.tokenized.txt;
cat /tmp/train.tokenized.txt /tmp/valid.tokenized.txt > /tmp/sent.tokenized.txt;
NLTK_DATA=nltk_data
python generate_pun.py combiner-data \
    --path combiner/models/checkpoint_best.pt \
    --beam 20 --nbest 1 --unkpen 100 --task edit --system rule \
    --retriever-model models/bookcorpus/retriever.pkl \
    --doc-file data/bookcorpus/raw/books1/epubtxt/zone-defense.epub.txt \
    --skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
    --num-candidates 500 --num-templates 100 \
    --num-topic-word 100 --type-consistency-threshold 0.3 \
    --pun-words data/semeval/hetero/dev.json \
    --outdir ./ \
    --scorer random --max-num-examples 100 \
    --word-counts-path data/bookcorpus/skipgram/dict.txt


	data/bookcorpus/skipgram



Hypothesis: call retriever on text then call generator




python -m pungen.retriever --doc-file templates.txt \
    --path models/bookcorpus/retriever.pkl --overwrite
python generate_pun.py data/bookcorpus/edit/bin/data \
        --path models/bookcorpus/edit/delete/checkpoint_best.pt \
        --beam 20 --nbest 1 --unkpen 100 \
        --system rule --task edit \
        --retriever-model models/bookcorpus/retriever.pkl --doc-file templates.txt \
        --lm-path models/wikitext/wiki103.pt --word-counts-path models/wikitext/dict.txt \
        --skipgram-model data/bookcorpus/skipgram/dict.txt models/bookcorpus/skipgram/sgns-e15.pt \
        --num-candidates 500000 --num-templates 100000 \
        --num-topic-word 1000 --type-consistency-threshold 0.01 \
        --pun-words puns.json \
        --outdir results/semeval/hetero/dev/rule \
        --scorer random \
        --max-num-examples 10000



[{"id": "het_13", "tokens":[], "pun_word": "dye", "alter_word": "die", "pun_word_id": 11}]


[{"id": "het_600", "pun_word": "sea", "alter_word": "seize", "tokens":[], "pun_word_id": 11}]

[{"id": "het_1691", "pun_word": "dam", "alter_word": "damn", "tokens":[], "pun_word_id": 11}]


{"id": 11, "pun_pair": {"id": "het_600", "pun_word": "sea", "alter_word": "seize"}, "context": {"id": 14, "word": "build", "synonyms": ["chassis", "habitus", "human body", "build", "construct", "frame", "physique", "ramp up", "body-build", "progress", "form", "material body", "figure", "bod", "establish", "make", "physical body", "anatomy", "flesh", "shape", "build up", "work up", "soma", "or or build"]}, "prompt1": "Generate 10 sentences containing the word 'seize' and at least one of the following phrases: chassis, habitus, human body, build, construct, frame, physique, ramp up, body-build, progress, form, material body, figure, bod, establish, make, physical body, anatomy, flesh, shape, build up, work up, soma, or or build.", "prompt2": "Generate 100 sentences containing the word 'seize' towards the end and at least one of the following phrases: chassis, habitus, human body, build, construct, frame, physique, ramp up, body-build, progress, form, material body, figure, bod, establish, make, physical body, anatomy, flesh, shape, build up, work up, soma, or or build.", "seed_sentence_count": 10}



python -m pungen.wordvec.preprocess --data-dir data/bookcorpus/skipgram \
	--corpus data/bookcorpus/raw/train.txt \
	--min-dist 5 --max-dist 10 --threshold 80 \
	--vocab data/bookcorpus/skipgram/dict.txt

python -m pungen.wordvec.train --weights --data data/bookcorpus/skipgram/train.bin \
    --save_dir models/bookcorpus/skipgram \
    --mb 3500 --epoch 100 \
    --vocab data/bookcorpus/skipgram/dict.txt