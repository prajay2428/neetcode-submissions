class Solution:
    def decodeString(self, s: str) -> str:
        # initialise a stack
        # iterate over the string
        # if char = [ continue
        # if char is a number or a letter then append
        # if char is ]
        # then until you find a number pop the strings and add it to word
        # pop the number and multiply the word with the string 
        # append the word
        countStack = []
        wordStack = []

        word=""
        count = ""

        for i in range(len(s)):
            if s[i] == '[':
                countStack.append(count)
                wordStack.append(word)
                word = ""
                count = ""
            
            elif s[i].isdigit():
                count += s[i]
            elif s[i].isalpha():
                word += s[i]
            else:
                word = wordStack.pop() + int(countStack.pop()) * word 
        
        return word

        