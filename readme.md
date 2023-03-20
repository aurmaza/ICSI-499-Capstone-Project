Project Title: Reccomendation System for NexClap

Project Description: This code acts as a reccomendation system that consumes user information
and outputs a rank based on a user's interaction with the NexClap website. The main algorithm
"ranking algorithm" can take in a user:text dictioanry and compute similarity scores, sentence count and technical word count. The other scripts are for converting different types of posts
to text which can then be consumed by our ranking algorithm.

Project Algorithms:

1. Ranking Algorithm:
   The Ranking Algorithm takes in a user dictionary. The user dictionary consists of a key which
   is the user's username and a value which is a user's blog post content. The ranking algorithm
   takes in account sentence count and technical word count. The ranking algorithm also uses
   the gensim library for computing similarities between documents.

    A simple step process:
        Given Documents A,B,C,D
        If we want to compare A to B,C,D

        On B,C,D:

        1. Tokenize words of each document
        2. Create a dictionary that maps every word to a number so that each word has a unique id.
        3. Create a bag of words, an object that contains a word id and its frequency
        4. Use the Term Frequency - Inverse Document Frequency (TFIDF) model from gensim. TFIDF creates weights for each word, where more frequent words have a lower weight.
        5. Create a similarity measuring object with gensim. The similarity measure object creates an index for a given set of documents so that you can compare multiple documents.
        6. Create a query document, document A, and compare it to the TFIDF object created with B,C,D.

2. Medium Web Scraper:
   The Medium WebScraper uses beautifulSoup4, a webScraping library, to extract
   a user's text from Medium, where nexClap users often post their blog posts.

3. s4u Web Scraper:
   The s4u WebScraper uses beautifulSoup4, a webScraping library, to extract
   a user's text from silicionvalley4u.com, where nexClap users often post their blog posts.

4. speechRecognizer:
   The speechRecognizer uses the youtubeAPI library to extract user captions from a given video.
   These captions can then be used to rate a user's post as the text can be consumed by the
   ranking algoritm.

5. mp4ToText:
   NexClap users often upload mp4 files directly to nexClap. In order to evaluate what was
   presented the mp4, we converted the mp4 file to an audio file using the VideoFileClip library.
   The speech in this file was then recognized by speech_recognition library.

Packages:
Package Name: beautifulSoup4
Package Version: 4.9.3

Package Name: nltk
Package Version: 3.6.1

Package Name: gensim
Package Version: 4.0.3

Package Name: numpy
Package Version: 1.24.1

Package Name: requests
Package Version: 2.25.1

Package Name: python-dotenv-0.21.1
Package Version: 0.21.1

Package Name: google-api-python-client
Package Version:2.78.0

Package Name: moviepy
Package Version:1.0.3

Package Name: SpeechRecognition
Package Version:3.9.0

Package Name: pandas
Package Version: 1.2.4
