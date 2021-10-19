#  Function that calculates mean quality score in a read
def quality(qual):
    quality_score = 0
    #  For each symbol in quality score line, we calculate its number in ascii table and subtract 33
    for i in qual:
        quality_score += ord(i) - 33
    return quality_score / len(qual)


#  Function that calculates GC-content for a read
def gc_content(seq):
    return (seq.count('G') + seq.count('C')) / len(seq) * 100


#  Function that processes input fastq file
def process_file1(input_fastq):
    with open(input_fastq, 'r') as f:
        reads = f.readlines()
        #  This function reads fastq file in a list and make 4 different new lists:
        identifyer = reads[0::4]
        seq = reads[1::4]
        plus = reads[2::4]
        quality = reads[3::4]
        #  Then we combine them in a list of tuples
        groups = zip(identifyer, seq, plus, quality)
        #  Create new empty list
        lst = []
        #  For each tuple in a "groups" list we make a string out of it and add this string to our new list
        for i in groups:
            lst.append(''.join(i))
        #  Finally we create a dictionary in which keys are our reads sequences
        #  And values are 4 lines that represents each read in fastq file
        data = dict(zip(seq, lst))
    return data


#  Function that processes input fastq file
def process_file2(input_fastq):
    with open(input_fastq, 'r') as f:
        reads = f.readlines()
        #  This function reads fastq file in a list and select reads and quality score sequences
        seq = reads[1::4]
        quality = reads[3::4]
        #  Then it makes dictionary of reads and quality score sequences
        seq_and_qual = dict(zip(seq, quality))
    return seq_and_qual


#  Main function that filters fastq file using previous functions
def main(input_fastq, output_file_prefix, gc_bounds=[0, 100], length_bounds=[0, 2 ** 32], quality_threshold=0,
         save_filtered=False):
    #  Using output file prefix, we create paths to new fastq files
    passed_fastq = output_file_prefix + '_passed.fastq'
    failed_fastq = output_file_prefix + '_failed.fastq'
    #  Using previous functions, create dictionaries out of input file
    data = process_file1(input_fastq)
    seq_and_qual = process_file2(input_fastq)
    #  For each read we check the filter conditions
    for key in seq_and_qual:
        #  The last 2 symbols of each line in fastq file is "/n"
        #  To calculate the quality score correctly, we need to remove them
        qual = seq_and_qual[key][0:-2]
        if quality(qual) >= quality_threshold:
            seq = key.rstrip('\n')
            if gc_bounds[0] <= gc_content(seq) <= gc_bounds[-1]:
                if length_bounds[0] <= len(seq) <= length_bounds[-1]:
                    #  If the read met all the conditions, write 4 lines that represents it into a new "passed" file
                    with open(passed_fastq, 'a') as output1:
                        output1.write(data[key])
        else:
            #  If save_filter == True, we need to save failed reads as well
            if save_filtered:
                with open(failed_fastq, 'a') as output2:
                    output2.write(data[key])


input_fastq = input('Enter path to input fastq file: ')
output_file_prefix = input('Enter output file prefix: ')
gc_bounds = [int(i) for i in input('Enter 2 GC-bounds, divided by space: ').split()]
length_bounds = [int(i) for i in input('Enter 2 length bounds, divided by space: ').split()]
quality_threshold = int(input('Enter quality threshold: '))
save_filtered = input('Do we need to save filtered reads? Yes/No: ') == 'Yes'

main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered)
