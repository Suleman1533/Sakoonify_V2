#1.  From memory: word-frequency counter (count how many times each word appears in a sentence) using a dict.
#2. store the conversation as a list of dicts [{"role":"user","text":...}]. Add a /history command that prints all past messages.
#3. Write a function that returns the first non-repeating character in a string. If every character repeats, return None
#4. Reverse the order of the words in a sentence without reversing the letters inside each word.

#5. Write a function that returns the three most frequent words in a sentence.


freq={}
def priority(sentence):
    words = sentence.split()
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
    
    
sentence = "ahmad ali ahmad, ahmed ahmed ahmed usman man man zain zain zain zain zain "
print(priority(sentence))


items = list(freq.items())
print(len(items))


for i in range(len(items)):
    for j in range(i+1, len(items)):
        if items[i][1] < items[j][1]:
            items[i], items[j] = items[j] , items[i]

print(items[:3])



