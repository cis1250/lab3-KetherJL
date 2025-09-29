import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")
    
cleaned = re.sub(r'[^\w\s]', '', user_sentence) #cleans out any punctuation or number
split_sentence = cleaned.lower().split() #makes everything lowercase

list_a = [] #for words
list_b = [] #for frequncies

for word in split_sentence:
    #check if word has been found before
    if word not in list_a:
        list_a.append(word)
        list_b.append(1)
    
    else:
        #iterates over list_a for duplicates
        index = list_a.index(word) #index() returns index 
        list_b[index] += 1

print(f'Input: "{user_sentence}"')
print("Output:")
#formats the output
for i in range(len(list_a)):
    print(f"{list_a[i]}: {list_b[i]}")
