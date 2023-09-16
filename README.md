## What is this?
A word to emoji converter. that is, Given a word, what is the most appropiate emoji(s) that describe this word?

For example: an appropiate emoji for the word clown is 🤡.

## Problem
It's a very tedious task to manually map emoji to a specific word, and one word could be mapped to many emojis and vice versa, for example: the word sad could map to 😢 or 😔, yummy could map to 😋 or 🤤, and emoji 😃 could map to either words smile or happy

## Approach: Word Embeddings

Word embedding is a powerful technique used to represent words as numerical vectors in a high-dimensional space. The main idea behind word embeddings is that words with similar meanings or that are used in similar contexts tend to have similar vector representations.

For instance, consider the words "cat," "dog," and "car." In a well-trained word embedding model, the vectors representing "cat" and "dog" would be closer to each other than either of them would be to the vector representing "car." This is because "cat" and "dog" share a common context as pets, while "car" is unrelated in terms of meaning and usage.

And so word embeddings capture 'context' relationships between words through the analysis of large text. By training a model on vast amounts of textual data, such as Twitter posts, news articles, or books, the model learns to associate words that frequently appear together and assigns them similar vector representations.

A popular word embedding model is Word2Vec, which uses techniques like Skip-gram and Continuous Bag of Words (CBOW) to learn word embeddings. the Gensim library is utilized to apply the Word2Vec model on a collection of **100** different emojis. The dataset for training the model is obtained from Twitter using the Snscrape library, consisting of approximately **600,000** tweets.

Below are some results of the program:
<p align="center">
  <img src="https://github.com/HNOONa-0/WTOE/assets/59091536/12e8a068-006f-412c-9f38-91104a308551" width="400" alt="Image description">
</p>
<p align="center">
  <img src="https://github.com/HNOONa-0/WTOE/assets/59091536/213b32b0-a55a-4ce8-b1ac-1ad1ebb2dd0e" width="400" alt="Image description">
</p>
<p align="center">
  <img src="https://github.com/HNOONa-0/WTOE/assets/59091536/c7308094-2b01-4a13-a6a6-f71f6e8380ec" width="400" alt="Image description">
</p>

## Issues
1) Not all words are present in this model, example:
<p align="center">
  <img src="https://github.com/HNOONa-0/WTOE/assets/59091536/1ed3998c-d1c4-404a-824c-6ad41c6fab05" width="400" alt="Image description">
</p>
2) Some outputs are not satisfactory, example:

<p align="center">
  <img src="https://github.com/HNOONa-0/WTOE/assets/59091536/432f6a64-ef60-4275-996f-723a3e7bb584" width="400" alt="Image description">
</p>

This is due to many reasons, two of which:
1) The dataset is small and unfortunately, ****Twitter API has changed and is now a lot harder to scrape tweets****, it's not easy to scrape more tweets.

2) The quality of the dataset itself. This depends on what query we used to scrape tweets, improving the query we use could go along way.
