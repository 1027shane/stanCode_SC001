"""
File: similarity.py
Name: Shane Liu
-------------------------
This program called "HOMOLOGY", 
compares short DNA sequence(s2) with sub sequences of a long DNA sequence(s1).
"""


def main():
    """
    This program compares short dna sequence with part sequences of a long DNA sequence,
    and finds the best match one.
    """
    # case-insensitive
    long_sequence = input('Please give me a DNA sequence to search: ').upper()
    short_sequence = input('What DNA sequence would you like to match? ').upper()
    best_match = similarity(long_sequence, short_sequence)
    print('The best match is '+best_match)


def similarity(long_sequence, short_sequence):
    """
    :param1 long_sequence: str, the original DNA sequence to search
    :param2 short_sequence: str, the original DNA sequence to match
    :return: str, the best matched string
    """
    # highest_counter: the highest match counter
    highest_counter = 0

    best_match_str = ''
    for i in range(len(long_sequence)-len(short_sequence)+1):
        part_long_sequence = long_sequence[i:i+len(short_sequence)]

        # counter: to record similarity between short_sequence and part_long_sequence
        counter = 0
        for j in range(len(short_sequence)):
            if part_long_sequence[j] == short_sequence[j]:
                counter += 1

        if highest_counter < counter:
            highest_counter = counter
            best_match_str = part_long_sequence
    return best_match_str


if __name__ == '__main__':
    main()
