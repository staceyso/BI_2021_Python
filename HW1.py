def transcribe(dna):
    return dna.replace("T", "U").replace("t", "u")


def reverse(seq):
    return seq[::-1]


def complement(seq):
    compl_seq = []
    # list of complementary nucleotides:
    compl = dict(A='T', C='G', G='C', T='A', U='A', a='t', c='g', g='c', t='a', u='a')
    for nucl in seq:
        compl_seq.append(compl[nucl])
    return "".join(compl_seq)


def reverse_complement(seq):
    compl_seq = []
    # list of complementary nucleotides:
    compl = dict(A='T', C='G', G='C', T='A', U='A', a='t', c='g', g='c', t='a', u='a')
    for nucl in seq:
        compl_seq.append(compl[nucl])
    return "".join(compl_seq)[::-1]


def enter_sequence():
    while True:  # infinite cycle
        seq = input("Enter your sequence: ")
        ok_letters = set('aAcCgGtTuU')  # letters that occur in DNA or RNA
        score = 0  # count for symbols that are not in the "ok_letters"
        for elem in seq:
            if elem not in ok_letters:  # checks if the element does not occur in DNA or RNA
                score += 1  # then score is increased by 1
        if score != 0:  # if some of the elements do not occur in DNA or RNA
            print('This DNA or RNA sequence does not exist. Try again')  # repeats the cycle
        else:  # if everything is ok with the sequence
            break
    return seq


def enter_dna():
    while True:  # infinite cycle
        dna = input("Enter your sequence: ")
        ok_letters_dna = set('aAcCgGtT')  # letters that occur in DNA
        score = 0  # count for symbols that are not in the "ok_letters_dna"
        for elem in dna:
            if elem not in ok_letters_dna:  # checks if the element does not occur in DNA
                score += 1  # then score is increased by 1
        if score != 0:  # if some of the elements do not occur in DNA
            print('This DNA sequence does not exist. Try again')  # repeats the cycle
        else:  # if everything is ok with the sequence
            break
    return dna


while True:  # infinite cycle for entering commands and sequences
    command = input("Enter command: ")
    if command == 'exit':
        break  # if the command is exit, infinite cycle breaks
    elif command == 'transcribe':
        dna = enter_dna()  # we use special function to enter DNA sequence
        print(transcribe(dna))
    elif command == 'reverse':
        seq = enter_sequence()  # we use special function to enter DNA or RNA sequence
        print(reverse(seq))
    elif command == 'complement':
        seq = enter_sequence()  # we use special function to enter DNA or RNA sequence
        print(complement(seq))
    elif command == 'reverse complement':
        seq = enter_sequence()  # we use special function to enter DNA or RNA sequence
        print(reverse_complement(seq))  # выводится результат функции
    else:    # if the command does not exist in the program
        print('This command does not exist, try again')
