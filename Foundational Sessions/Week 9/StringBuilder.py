class StringBuilder:
    def __init__(self):
        self._strings = []

    def add(self, string):
        """Adds a new string to the StringBuilder."""
        self._strings.append(string)

    def build(self):
        """Constructs the final string using 'join()'."""
        return ''.join(self._strings)

    def clear(self):
        """Clears the accumulated strings."""
        self._strings = []

    def __str__(self):
        """Returns the current state of the string being built."""
        return self.build()



