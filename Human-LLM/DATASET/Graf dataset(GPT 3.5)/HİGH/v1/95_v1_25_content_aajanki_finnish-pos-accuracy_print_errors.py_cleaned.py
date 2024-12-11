import logging
import conll18_ud_eval
import typer
from pathlib import Path
from datasets import load_dataset
a1 = 1
a2 = 2
def fonk1():
    logging.basicConfig(b1 = '%(levelname)s: %(message)s', level=logging.INFO)
    b2 = Path('results')
    b3 = b2 / 'errors'
    b3.mkdir(b4 = True, exist_ok=True)
    b5 = b2 / 'predictions'
    for model_result_dir in b5.glob('*'):
        b6 = model_result_dir.stem
        b7 = model_result_dir.glob('*.conllu')
        for predictions_file in b7:
            b8 = predictions_file.stem
            b9 = conll18_ud_eval.load_conllu_file(gold_path(b8))
            b10 = conll18_ud_eval.load_conllu_file(predictions_file)
            b11 = b3 / f'lemma_errors_{b6}_{b8}.txt'
            print(f'Writing errors in {b11}')
            with open(b11, 'w') as f:
                for system_sentence, gold_sentence in zip(b10.sentences, b9.sentences):
                    b12 = [w for w in b10.words if w.span.start >= system_sentence.start and w.span.end <= system_sentence.end]
                    b13 = [w for w in b9.words if w.span.start >= gold_sentence.start and w.span.end <= gold_sentence.end]
                    b14 = [x.columns[a2].lower() for x in b12 if not x.is_multiword]
                    b15 = [x.columns[a2].lower() for x in b13 if not x.is_multiword]
                    b16 = [x.columns[a1].lower() for x in b13 if not x.is_multiword]
                    if b14 != b15:
                        f.write(' '.join(b16) + '\n')
                        f.write(' '.join(b15) + '\n')
                        f.write(' '.join(b14) + '\n')
                        f.write('\n')
if b17 = = '__main__':
    typer.run(main)