from data import *;
import gensim;

def main():
    # model = gensim.models.Word2Vec.load("myModel.model");
    model = gensim.models.Word2Vec.load("my_model.model");
    while(True):
        s=input('Enter word: ');
        if s=='0':
            break;
        if s not in model.wv:
            continue;
        d=float(-10**2);
        res='?';
        for em in emojis:
            if em in model.wv and model.wv.similarity(s,em)>d:
                d=model.wv.similarity(s,em);
                res=em;
        print(res);
if __name__ == "__main__":
    main()
