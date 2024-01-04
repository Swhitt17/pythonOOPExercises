"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    ...
    def __init__(self, path):
        """Reads and reports # of items read"""
        dict_file = open(path)

        self.words = self.read_through(dict_file)

        print(f"{len(self.words)} words read")

    def read_through(self):
        """Reads file -> list of words"""
        return [w.strip() for w in dict_file]

   
    def random(self):
        """Gets a random word for list"""

        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """Special word finder that ignores blank lines/comments"""

    def read_through(self):
        """Reads file -> list of words"""
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
