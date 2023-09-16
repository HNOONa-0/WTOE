from data import *;
import gensim;
from heapq import heapify,heappush,heappop;
model = gensim.models.Word2Vec.load("my_model.model");

def get_result(s):
    if s not in model.wv:
        return "";
    heap=[];
    heapify(heap);
    for em in emojis:
        if em in model.wv and len(heap)<K:
            heappush(heap,(model.wv.similarity(s,em), em) );
        elif em in model.wv and model.wv.similarity(s,em)>heap[0][0]:
            heappop(heap);
            heappush(heap,(model.wv.similarity(s,em), em) );
    # print(len(heap) );
    heap.sort(reverse=True);
    res="";
    for tup in heap:
        res+=tup[1]+' ';
    return res;
def main():
    while(True):
        s=input('Enter word: ');
        if s=='0':
            break;
        if s not in model.wv:
            continue;
        d=float(-10**2);
        print(get_result(s) );
    
if __name__ == "__main__":
    main()
