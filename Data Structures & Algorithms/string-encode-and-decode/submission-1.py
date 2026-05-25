class Solution:

    # use the len of the word + a char delimiter
    # ex: word -> 4#word
    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    # read the number before the delimiter to know how many chars to read after the delimiter
    # this will be our original word to add onto the res list
    # ["we","say",":","yes","!@#$%^&*()"]
    # 2#we3#say1#:3#yes10#!@#$%^&*()
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # logic for determining word
            length_of_word = int(s[i:j])
            i = j + 1
            j = i + length_of_word
            word = s[i:j]
            res.append(word)
            i = j
        return res