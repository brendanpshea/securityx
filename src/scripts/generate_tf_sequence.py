"""Generate a balanced random T/F answer sequence for review questions."""
import random
import sys


def generate(n=20, seed=None):
    rng = random.Random(seed)
    half = n // 2
    seq = ['T'] * half + ['F'] * (n - half)
    rng.shuffle(seq)
    return seq


if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    seq = generate(20, seed)
    print(f'Seed: {seed}')
    for i, v in enumerate(seq, 1):
        print(f'{i:2d}. {v}')
    print(f'\nTotal True:  {seq.count("T")}')
    print(f'Total False: {seq.count("F")}')
