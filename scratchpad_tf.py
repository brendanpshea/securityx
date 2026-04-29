import random

def generate_sequence(chapter_num):
    # Ensure a roughly even split of True and False
    sequence = [True] * 10 + [False] * 10
    random.shuffle(sequence)
    
    print(f"--- Chapter {chapter_num} Sequence ---")
    for i, val in enumerate(sequence, 1):
        print(f"Q{i}: {'True' if val else 'False'}")
    print("\n")

if __name__ == "__main__":
    generate_sequence(1)
    generate_sequence(2)
