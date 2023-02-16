## Motivation
Given a word what's the most appropiate emoji describing this word?

For example: 'clown'=🤡.

So i decided to write a program where instead of having to memorize utf-8 encoding of an emoji, or looking it up through a table of emojis (something you would do on a social platform).

## Problem
It's a very tedious task to manually find the right emoji for each word, very erroneous for a human being. It will also take alot of time.

Moreover what if >= 2 different emojis 'fight' for same word?

For example: 'yummy' = 🤤 or 😋?

## Approach: Word Embeddings

Word embedding is a learning technique where words are represented as a vector of real numbers, and, 2 words are similar if they are used in same context.

For example word 'cat' is closer to 'dog' than its to word 'car'.

Why?

Because cats, dogs are pets, we tend to to use same vocabulary around those 2 words, vocabulary like ('cute', 'feed', etc..)

A video that explains vector embeddings better [here](https://www.youtube.com/watch?v=gQddtTdmG_8&t=18s)

It's important to note that word embeddings rely on context rather than meaning, context that a word is used is not exactly meaning of the word but it's close.

Hence, if we use a Word Embedding model and have lots of data, we will get satisfactory results.

A famous Word Embedding model is **Word2Vec** model, the above program(s) uses **Gensim** library on 100 different emojies, specifically the **Word2Vec** model, data is collected from twitter with **Snscrape** library, model is trained on $5*10^5$ tweets.

To test the program just run ```program.py``` in the terminal, type the word you like to enquire about.

Not every word will have an output, infact, only a small subset of words we can enquire about, to save github memory. You can output words supported using ```model_words.py```

Some output of the program:

'cry'=😭

'laugh'=😂

'lol'=😂

'sad'=😢

It's not perfect by all means, for example:

'scared'=😾

'house'=💀

But with some more clever engineering and more data, we can get alot better results.

## Issues to revisit
*  Support all emojis not just 100

*  Can we further improve quality of data?

*  Can we do better than linear search to find best emoji?

*  Can we modify model to get better results for this specific task/is there a better model?
