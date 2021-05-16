def sentence_reversal(orig):
    # print(" ".join(reversed(orig.split())))
    #Or
    # print(" ".join(orig.split()[::-1]))
    words = []
    length = len(orig)
    space = [' ']
    i=0

    while i <length:
        if orig[i] not in space:
            word_start = i
            while i < length and orig[i] not in space:
                i+=1
            words.append(orig[word_start,i])
        i+=1
        return ' '.join(words[::-1])


sentence_reversal('This is the best')


def reverseWordSentence(Sentence):
    # Splitting the Sentence into list of words.
    words = Sentence.split(" ")

    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    newWords = [word[::-1] for word in words]

    # Joining the new list of words
    # to for a new Sentence
    newSentence = " ".join(newWords)

    return newSentence


# Driver's Code
Sentence = "I love my India"
# Calling the reverseWordSentence
# Function to get the newSentence
print(reverseWordSentence(Sentence))