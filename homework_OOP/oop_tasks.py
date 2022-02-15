from Bio.Seq import Seq, back_transcribe
from Bio import SeqIO
from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
import pandas as pd


# 1
class InitError(Exception):
    pass


class Cat:
    """
    Class that gives you an opportunity to create a cat and perform some basic interactions with it.
    """
    def __init__(self, name='Barsik', hungry=True, voice='Meow!'):

        if not isinstance(name, str):
            raise InitError("'name' must be str")
        if not isinstance(hungry, bool):
            raise InitError("'hungry' must be bool")
        if not isinstance(voice, str):
            raise InitError("'voice' must be str")

        self.name = name
        self.hungry = hungry
        self.voice = voice

    def feed(self):
        self.hungry = False
        self.voice = 'Mrrrp^^'

    def pet(self):
        if self.hungry:
            self.voice = 'Meow!'
            print('CatHint: Your cat is hungry, he/she doesn\'t want to be petted! Feed your cat!')
        else:
            self.voice = 'Mrrrp^^'
            self.hungry = True

    def talk_to(self):
        print(self.voice)


# 2
class RNA:
    """
    Class that describes RNA. It creates an object from RNA sequence.
    """
    def __init__(self, seq):
        self.seq = seq
        self.acid_type = 'ribonucleic'
        self.length = len(self.seq)

    def translate(self):
        """
        Method that translates RNA into aminoacid sequence. Returns protein sequence.
        """
        protein = Seq.translate(self.seq)
        return protein

    def reverse_transcribe(self):
        """
        Method that returns complementary DNA sequence (reverse transcription).
        """
        dna = back_transcribe(self.seq)
        return dna


# 3
class OnlyPositiveSet(set):
    """
    Class that is inherited from set, but includes only positive numbers.
    """
    def __init__(self, elements):
        super().__init__()
        for el in elements:
            self.add(el)

    def add(self, element) -> None:
        if isinstance(element, int) or isinstance(element, float):
            if element > 0:
                super().add(element)

    def update(self, *s) -> None:
        for it in s:
            for i in it:
                self.add(i)

    def __ior__(self, other):
        for element in other:
            self.add(element)
        return self

    def __ixor__(self, other):
        for element in other:
            if element not in self:
                self.add(element)
            else:
                self.remove(element)
        return self


# 4
class StatFASTA:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def count_seqs(self):
        nseq = 0
        for seq in SeqIO.parse(self.path, "fasta"):
            nseq += 1
        return nseq

    def histogram_lengths(self, path_to_save=None):
        lengths = [len(seq) for seq in SeqIO.parse(self.path, "fasta")]

        plt.figure(figsize=(10, 5))
        plt.hist(x=lengths,
                 color="lavender",
                 ec="black",
                 linewidth=0.25)
        plt.title('Histogram of sequences lengths', fontsize=18)
        plt.xlabel('Length', fontsize=12)
        plt.ylabel('Number of sequences', fontsize=12)

        if path_to_save is not None:
            plt.savefig(path_to_save)
        plt.show()

    def gc_content(self):
        gc_lst = [round(GC(seq.seq), 2) for seq in SeqIO.parse(self.path, "fasta")]
        gc = pd.DataFrame(gc_lst, columns=['GC-content'])
        return gc

    def all_metrics(self):
        print(f'The number of sequences: {self.count_seqs()}')
        self.histogram_lengths()
        print(f'GC-content for each sequence:\n{self.gc_content()}')
