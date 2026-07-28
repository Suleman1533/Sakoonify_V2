#— From memory: word-frequency counter (count how many times each word appears in a sentence) using a dict. Then rewrite it with collections.Counter


def frequency(string_data):
    new_list = string_data.split()
    #print(new_list)
    conversations={}
    for word in new_list:
        conversations[word] = conversations.get(word , 0) + 1
    return conversations    
    
freq = 'my name is suleman , king suleman, great and king and kind suleman, am so goated no need to my thanks'
print(frequency(freq))


print("=========================================================================================================")

#Find the first non-repeating character in a string.
def first_non_repeating(text):
    counting = {}

    # Step 1: Count the frequency of each character
    for char in text:
        counting[char] = counting.get(char, 0) + 1

    # Step 2: Find the first character with frequency 1
    for char in text:
        if counting[char] == 1:
            return char

    return None


text = "Suleman Gull"

result = first_non_repeating(text)

if result:
    print("First non-repeating character:", result)
else:
    print("No unique character found.")
    