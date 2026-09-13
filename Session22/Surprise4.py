# Reverse every word in a sentence.
sentence="Sophie is living in canada"

split_sent=sentence.split(' ')
print(split_sent)

reverse=[]

for i in range(len(split_sent)):
    curr=split_sent[i]
    print(curr)
    
    temp=curr[::-1]
    
    reverse.append(temp)

print(reverse)

result = " ".join(reverse)
print(result)


final_revese=[]
