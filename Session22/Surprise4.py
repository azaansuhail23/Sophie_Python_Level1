# Reverse every word in a sentence.
sentence="Sophie is living in canada"

split_sent=sentence.split(' ')
print(split_sent)

# reverse a word : [::-1]
def reverse(word):
    word.reverse()

for i in range(len(split_sent)):
    split_sent[i]=reverse(split_sent[i])

print(split_sent)