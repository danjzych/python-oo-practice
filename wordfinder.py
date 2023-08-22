from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.list_of_words = []
        self.read_file()

    def read_file(self):
        file = open(self.filepath)
        for line in file:
            self.list_of_words.append(line[:-1])
        file.close()

        print(f"{len(self.list_of_words)} words read")

    def random(self):
        return choice(self.list_of_words)

