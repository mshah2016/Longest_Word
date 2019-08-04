
class LongestWord:

    def __init__(self):
        self.longest_word_size = 0
        self.longest_word = ''

    def find_longest_word(self, string):

        words = string.split(' ')
        longest_word = ''
        for n in words:
            if len(n) > len(longest_word):
                longest_word = n
        return (len(longest_word), longest_word)


if __name__ == '__main__':
    lw = LongestWord()
    print("Please enter the string: ")
    lw_tuple = lw.find_longest_word(str(input()))
    print(lw_tuple)