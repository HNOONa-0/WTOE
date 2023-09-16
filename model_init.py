import gensim;
from data import *;

corpus=[];
pref_corpus=[];

def main():
    sentences=[];
    # prefixes for tweet text files that we use to train model on
    for f_name_pref in ['tw','twt']:
        i=0;
        # total number of subbarrays = len(emojis/Q_LEN)
        for j in range(len(emojis)//Q_LEN):
            f_name=f_name_pref+str(i)+'.txt';
            lines = open(f_name,'r',encoding='utf-8').read().split('\n');
            for line in lines:
                sentences.append(line.split(' ') );
            sentences.pop()
            i+=Q_LEN;
    model = gensim.models.Word2Vec(sentences=sentences, vector_size=VECTOR_SIZE, 
    window=WINDOW, min_count=MIN_CNT, workers=WORKERS);
    # save the model just created
    model.save("my_model.model");
    
if __name__ == "__main__":
    main()