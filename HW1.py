# функция "transcribe"
def transcribe(dna):
    rna = ''
    for i in dna:
        if i == 'T':
            rna += 'U'
        elif i == 't':
            rna += 'u'
        else:
            rna += i
    return rna


# функция "reverse"
def reverse(dna):
    return dna[::-1]


# функция "complement"
def complement(dna):
    compl_dna = ''
    compl = dict(A='T', C='G', G='C', T='A', a='t', c='g', g='c', t='a')
    for i in dna:
        compl_dna += compl[i]
    return compl_dna


# функция "reverse complement"
def reverse_complement(dna):
    compl_dna = ''
    compl = dict(A='T', C='G', G='C', T='A', a='t', c='g', g='c', t='a')
    for i in dna:
        compl_dna += compl[i]
    return compl_dna[::-1]


ok_letters = 'aAcCgGtT'  # буквы, которые встречаются в последовательности ДНК
while True:  # бесконечный цикл для считывания команд и последовательностей
    command = input("Enter command: ")  # ввод команды
    if command == 'exit':
        break  # если команда exit, цикл завершается
    elif command == 'transcribe':  # команда transcribe
        while True:
            seq = input("Enter your sequence: ")  # ввод последовательтности
            score = 0  # счётчик для проверки правильности последовательности
            for i in seq:
                if i not in ok_letters:  # проверка букв в последовательности
                    score += 1
            if score != 0:  # счётчик не равен нулю, если в ДНК есть "неправильные буквы"
                print('This sequence does not exist. Try again')
            else:  # если с последовательностью всё в порядке
                break
        print(transcribe(seq))  # выводится результат функции
    elif command == 'reverse':  # команда reverse
        while True:
            seq = input("Enter your sequence: ")  # ввод последовательтности
            score = 0  # счётчик для проверки правильности последовательности
            for i in seq:
                if i not in ok_letters:  # проверка букв в последовательности
                    score += 1
            if score != 0:  # счётчик не равен нулю, если в ДНК есть "неправильные буквы"
                print('This sequence does not exist. Try again')
            else:  # если с последовательностью всё в порядке
                break
        print(reverse(seq))  # выводится результат функции
    elif command == 'complement':  # команда complement
        while True:
            seq = input("Enter your sequence: ")  # ввод последовательтности
            score = 0  # счётчик для проверки правильности последовательности
            for i in seq:
                if i not in ok_letters:  # проверка букв в последовательности
                    score += 1
            if score != 0:  # счётчик не равен нулю, если в ДНК есть "неправильные буквы"
                print('This sequence does not exist. Try again')
            else:  # если с последовательностью всё в порядке
                break
        print(complement(seq))
    elif command == 'reverse complement':  # команда reverse complement
        while True:
            seq = input("Enter your sequence: ")  # ввод последовательтности
            score = 0  # счётчик для проверки правильности последовательности
            for i in seq:
                if i not in ok_letters:  # проверка букв в последовательности
                    score += 1
            if score != 0:  # счётчик не равен нулю, если в ДНК есть "неправильные буквы"
                print('This sequence does not exist. Try again')
            else:  # если с последовательностью всё в порядке
                break
        print(reverse_complement(seq))  # выводится результат функции
    else:    # если команда не существует
        print('This command does not exist, try again')
