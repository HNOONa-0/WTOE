# map between word(s) & emoji(s), can be many to many
# we can do that but
# 1 it requires a good machine, we dont have that
# 2 it requires alot of data, we can download data from above
# given a word find related emoji
# import gensim.downloader as api
from data import *;
import dwl_tweets;
corpus=[];
pref_corpus=[];

def read_file(f_name):
    f=open(f_name,'r');
    content=f.read();
    f.close();
    return int(content);
def write_file(f_name,content):
    f=open(f_name,'w+');
    f.write(content)
    f.close();
def read_write_file(f_name):
    i=read_file(f_name);
    i+=Q_LEN;
    write_file(f_name,str(i) );
    return i-Q_LEN;
def write_corpus(i,corpus):
    f=open(F_NAME_PREF+str(i)+'.txt','w+',encoding='utf-8');
    for arr in corpus:
        f.write(' '.join(arr) );
        f.write('\n');
    f.close();
def main():
    # how many files to create?
    t=1;
    for j in range(t):
        i=read_file('start.txt');
        corpus=dwl_tweets.main(i);
        if corpus==-1:
            break;
        write_corpus(i,corpus)
        i+=Q_LEN;
        write_file('start.txt',str(i) );
if __name__ == "__main__":
    main()