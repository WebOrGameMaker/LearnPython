import unittest
def pluralize(words):
    """
    >>> pluralize(['cow', 'pig', 'cow', 'cow'])
    {'cows', 'pig'}
    >>> pluralize(['table', 'table', 'table'])
    {'tables'}
    >>> pluralize(['chair', 'pencil', 'arm'])
    {'chair', 'pencil', 'arm'}
    """
    pluralized_words = set(())
    for i in range(len(words)):
        if words.count(words[i]) > 1:
            pluralized_words.add(words[i] + "s")
        else:
            pluralized_words.add(words[i])
    return pluralized_words

class PluralizeTest(unittest.TestCase):
    def test_pluralized(self):
        self.assertEqual(pluralize(['cow', 'pig', 'cow', 'cow']), {'cows', 'pig'})
        self.assertEqual(pluralize(['table', 'table', 'table']), {'tables'})
        self.assertEqual(pluralize(['chair', 'pencil', 'arm']), {'chair', 'pencil', 'arm'})



if __name__ == "__main__":
    unittest.main()