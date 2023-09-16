import snscrape.modules.twitter as sntwitter

from gensim.test.utils import common_texts;
from gensim.models import Word2Vec;

# use data constants
from data import *
# use OR class & base query
from query_util import *
# use proper tokenize to tokenize tweet
from tweet_util import proper_tokenize
# use date object to get tweets from all years
import datetime

def main(i=0):
    if i>=len(emojis ):
        return -1;
    d=datetime.date(YEAR,DAY,MONTH);
    corpus=[];
    pref_corpus=[];
    for idx in range(MUL):
        d2=d;
        d1=d-datetime.timedelta(days=DAYS);
        tweet_time='since:'+str(d1)+' until:'+str(d2);

        # important note, query max length is 512 characters
        query=or_query(emojis[i:min(i+Q_LEN,len(emojis ) ) ] )+' lang:en '+tweet_time;
        j=0;
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            doc=tweet.rawContent;
            # print(tweet.rawContent)
            res=proper_tokenize(doc);
            if len(res)<=0:
                continue;
            corpus.append(doc);
            pref_corpus.append(res)
            if j>=T:
                break;
            j+=1;
        d-=datetime.timedelta(days=DAYS);
    # print(pref_corpus);
    # print(query);
    return pref_corpus;
if __name__ == "__main__":
    main()

# tweet_time='';
# tweet_time='until:'+str(d2);