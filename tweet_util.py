# use string.translate to remove punctuation
import string
# use nltk to tokenize tweets including emojis
from nltk.tokenize.casual import TweetTokenizer
t=TweetTokenizer();
# use data constants
from data import *
emoji_set=set(emojis);

# Create a set of frequent words
stop_list = set('for a an of the and to in'.split(' ') );
# another useless word list
rm_list = set('if is on at has have had it its iam am my your his her our their mine yours his hers theirs either both who which that thats as this these that those i we you he she it they him hers'.split(' ') );
# min_len of word
def clean_str(s):
    # if contigous character appear more than twice remove it;
    j=1;
    c=1;
    s=list(s);
    for i in range(1,len(s) ):
        if s[i]!=s[j-1]:
            s[j]=s[i];
            j+=1;
            c=1;
        else:
            if c<2:
                s[j]=s[i];
                j+=1;
            c+=1;
    return "".join(s[0:j]);
def proper_tokenize(doc):
    # put doc content in temp
    tmp=[];
    # sometimes scrape will give us a tweet with no emoji in it, ok will tell us
    ok=0;
    # make sure to lowercase the doc
    for word in t.tokenize(doc.lower() ):
        # remove punctuation from the word, the extra string at the end for symbols not in punctuation
        word=word.translate(str.maketrans('', '', string.punctuation+'’–‘') );
        # remove characters that occur > 2 times
        word=clean_str(word);
        # stem the word ? cant find a good library to get required property
        # check if length is too small or in stop,rm list
        if (word not in emoji_set and len(word)<MIN_LEN) or word in stop_list or word in rm_list:
            continue;
        # check if word is @ or link
        if word.startswith('@') or word.startswith('http'):
            continue;
        tmp.append(word);
        ok=1 if word in emoji_set else ok;
    return tmp if ok==1 else [];

def main():
    # s[a:b]=[a...b)=[a...b-1];
    print('hello');
    
if __name__ == "__main__":
    main()
