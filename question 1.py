import string
def letter_frequency(sentence):
    sentence = sentence.lower()
    char_list = list(string.ascii_lowercase)
    char_count = {x:0 for x in char_list}
    dic = {}
    for x in char_list:
        dic[x] = 0
    for i in sentence:
        try:
            char_count[i]+=1
        except:
            char_count[i]=1
    return char_count
sentence="Hello my name is Sabrina"
print(sorted(dict.items(letter_frequency(sentence))))