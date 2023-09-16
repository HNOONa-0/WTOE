import gensim;

def main(model=-1):
    if model==-1:
        model = gensim.models.Word2Vec.load("my_model.model");
    ans=[];
    for i in range(0,len(model.wv) ):
        ans.append(model.wv.index_to_key[i] );
    print(ans)
if __name__ == "__main__":
    main()
