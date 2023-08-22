from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """Reads file and creates list of words."""
        self.filepath = filepath
        self.list_of_words = []
        self.read_file()

    def __repr__(self):
        return f"<WordFinder filepath={self.filepath}>"

    def read_file(self):
        """Reads file line by line and appends to list of words."""
        file = open(self.filepath)
        for line in file:
            self.list_of_words.append(line[:-1])
        file.close()

        print(f"{len(self.list_of_words)} words read")

    def random(self):
        """Returns a random word from the list of words."""
        return choice(self.list_of_words)
