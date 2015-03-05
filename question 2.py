sentence={'my':1,'birthday':2,'is':3,'march':4,'21st':5} 
for word in sentence: 
    print(word)               
def word_frequency():
    word_list=[x.lower() for x in['my','birthday','is','march','21st','my','birthday','is','march','21st']]
    sentence ={}
    for word in word_list:
        if word in sentence:
            sentence[word]+=1
        else:
            sentence[word]=1    
    print(sentence)     
print(word_frequency()) 
