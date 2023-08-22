from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> test = WordFinder("test.txt")
    8 words read

    >>> test.random() in ['mango', 'banana', 'strawberry', '', '# this is a comment', '# so is this']
    True

    >>> test.random() in ['mango', 'banana', 'strawberry', '', '# this is a comment', '# so is this']
    True

    >>> test.random() in ['mango', 'banana', 'strawberry', '', '# this is a comment', '# so is this']
    True

    """

    def __init__(self, filepath):
        """Reads file and creates list of words."""
        file = open(filepath)
        self.list_of_words = self.read_file(file)
        file.close()

        print(f"{len(self.list_of_words)} words read")

    def __repr__(self):
        return f"<WordFinder filepath={self.filepath}>"

    def read_file(self, file):
        """Reads file line by line and returns list of words."""
        return [line[:-1] for line in file]

    def random(self):
        """Returns a random word from the list of words."""
        return choice(self.list_of_words)


class SpecialWordFinder(WordFinder):
    '''SpecialWordFinder - find words that aren\'t spaces or comments

    >>> test = SpecialWordFinder("test.txt")
    3 words read

    >>> test.random() in ['mango', 'banana', 'strawberry']
    True

    >>> test.random() in ['mango', 'banana', 'strawberry']
    True

    >>> test.random() in ['mango', 'banana', 'strawberry']
    True


    '''

    def __repr__(self):
        return f'SpecialWordFinder filepath={self.filepath}'

    def read_file(self, file):
        '''Returns a random line that is not a comment or blank'''
        return [line for line in super().read_file(file) if not line.startswith('#') and line != '']
