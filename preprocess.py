import re

def text_read(addrs):
    with open('/home/deba/dl/language model/text_dateset/decl_independance.txt', encoding = 'utf-8') as f:
        data_text = f.read()
    return data_text 

def text_cleaner(text):
    # lower case text
    newString = text.lower()
    newString = re.sub(r"'s\b","",newString)
    # remove punctuations
    newString = re.sub("[^a-zA-Z]", " ", newString) 
    long_words=[]
    # remove short word
    for i in newString.split():
        if len(i)>=3:                  
            long_words.append(i)
    return (" ".join(long_words)).strip()

# preprocess the text
data_new = text_cleaner(data_text)