from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """Reads file and creates list of words."""
        # open file here
        #self.filepath = filepath
        self.list_of_words = []
        self.read_file() # this returns a list
        #close file

    def __repr__(self):
        return f"<WordFinder filepath={self.filepath}>"

    #TODO::make this the file that is extended, not the random function
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


class SpecialWordFinder(WordFinder):
    '''SpecialWordFinder - find words that aren\'t spaces or comments'''

    def __init__(self, filepath):
        '''Creates an instance of SpecialWordFinder using filepath'''
        super().__init__(filepath)

    def __repr__(self):
        return f'SpecialWordFinder filepath={self.filepath}'

    def random(self):
        '''Returns a random line that is not a comment or blank'''
        valid_words = [
            line for line in self.list_of_words if not line.startswith('#') and line
            ]
        return choice(valid_words)