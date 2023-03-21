import nltk
import gensim as gn
import numpy
import sys
from operator import itemgetter
import csv
import string
import time
# nltk.download('stopwords')
# pip install nltk
# pip install gensim
# for gensim to work, most recent numpy must be installed aswell
# do pip install --upgrade numpy

userDict = {}


def stopWordRemoval(users):
    res = {}
    stpwords = set(nltk.corpus.stopwords.words('english'))
    stpwords.add('the')
    stpwords.add('this')
    for userName, text in users.items():
        tolowerCase = text.lower()
        filtered = filter(lambda w: not w in stpwords, tolowerCase.split())

        res[userName] = list(filtered)
    return res


def wordCount(users):
    wordCount = {}
    for key in users:
        wordCount[key] = len(users[key]) + 1
    return wordCount


def techWordCount(users):
    techWordCount = {}
    for userName, text in users.items():
        techCount = 0
        for token in text:
            # Removes punctuation from the word, resolving comparison issues
            token = token.translate(str.maketrans('', '', string.punctuation))
            if token in coding_terms:
                techCount += 1
            techWordCount[userName] = techCount
    return techWordCount


def sentenceCount(res):
    sentences = {}
    for userName, text in res.items():
        sentenceCount = 0
        for token in text:
            if (token.endswith(".") or token.endswith("?") or token.endswith("!")):
                sentenceCount += 1
                sentences[userName] = sentenceCount
    return sentences


def similarities(blogList):
    users = list(blogList.keys())
    similarity = {}
    for idx, name in enumerate(users):
        others = users[:idx] + users[idx+1:]

        compares = [blogList[k] for k in others]
        # Assigns Every word in every post to a unique id
        dicto = gn.corpora.Dictionary(compares)

        # counts overall number of words to each id
        corpus = [dicto.doc2bow(docs) for docs in compares]
        # # Inverse Document Frequency which weighs down tokens that appear frequently
        tf_idf = gn.models.TfidfModel(corpus)
        sims = gn.similarities.Similarity(
            '', tf_idf[corpus], num_features=len(dicto))
        queryDocument = dicto.doc2bow(blogList[name])
        queryDocumentTFIDF = tf_idf[queryDocument]

        print('Individual similaritiy score for', name,
              'against the other blog posts: ', sims[queryDocumentTFIDF])
        average = sum(sims[queryDocumentTFIDF])
        print('The average similarity score for', name, ': ', average)
        similarity[name] = average
    return similarity


# List of technical words that are not stopwords
coding_terms = ["algorithm",    "syntax",    "compiler",    "debugging",    "interpreter",    "library",    "API",    "library function",    "variable",    "data type",    "loop",    "conditional statement",    "function",    "argument",    "parameter",    "recursion",    "object-oriented programming",    "class",    "method",    "attribute",    "inheritance",    "polymorphism",    "encapsulation",    "abstraction",    "structured programming",
                "unstructured programming",    "high-level programming language",    "low-level programming language",    "source code",    "machine code",    "binary",    "bytecode",    "compression",    "decompression",    "binary tree",    "hash table",    "stack",    "queue",    "linked list",    "binary search",    "linear search",    "graphical user interface",    "command line interface",    "front-end development",    "back-end development"]


#

# In this we will have to take each document which acts as a key word, create a new dictonary, feature count, corpus etc. from the rest
# of the other words, then see its similarity to all the others
def testAlgorithm(users):

    usersWithfilteredPosts = stopWordRemoval(users)

    wrdCount = wordCount(usersWithfilteredPosts)
    print("Word Count: ", wrdCount)
    techwrdCount = techWordCount(usersWithfilteredPosts)
    print("Tech word count: ", techwrdCount)
    sentenceCnt = sentenceCount(usersWithfilteredPosts)
    postSimilarity = similarities(usersWithfilteredPosts)

    # made similarities func return a dictionary & merged all dictionaries into one
    # was unable to find a library for "technical words"
    ds = [wrdCount, techwrdCount, sentenceCnt, postSimilarity]

    for key in wrdCount.keys():
        userDict[key] = tuple(d[key] for d in ds)

    # outputs fields to csv file
    fields = ['User', 'Words', 'Technical Words', 'Sentences', 'Similarity']
    with open('SampleFiles/out.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for key in userDict.keys():
            writer.writerow({'User': key, 'Words': userDict.get(key)[0], 'Technical Words': userDict.get(key)[1],
                             'Sentences': userDict.get(key)[2], 'Similarity': userDict.get(key)[3]})
    return(userDict)




def runTime(sourceCode):
    timeTaken = 0
    lineCount = 0
    code = """
import time
beg = time.time()
""" + sourceCode + """
end = time.time()
timeTaken = end-beg
lines = code.splitlines()
lineCount = (lines.__len__() + 1)
#print(timeTaken, lineCount)
"""
    _locals = locals()
    exec(code, globals(), _locals)
    timet = _locals.get('timeTaken')
    lc = _locals.get('lineCount')
    return timet, lc