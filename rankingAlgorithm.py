import nltk
import gensim as gn
import numpy
import sys
from operator import itemgetter
import csv
import string
import time
nltk.download('stopwords')
# pip install nltk
# pip install gensim
# for gensim to work, most recent numpy must be installed aswell
# do pip install --upgrade numpy


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
if __name__ == "__main__":
    beg = time.time()

    users = {
        "Akhil": "How do central banks control inflation? The US Federal Reserve typically designs financial policy to achieve an inflation target of 2 % . Inflation targeting is a central banking policy that revolves around adjusting monetary policy to achieve a specified annual rate of inflation. Interest rates can be seen as a mechanism or tool to achieve inflation targeting. When inflation is high, banks will raise interest rates. This has a trickle down effect starting with central banks, going down to commercial banks, and eventually down to commercial bank clients such as businesses and individual consumers.",
        "WAISL": "DigiYatra The beta version of the DigiYatra app is presently available at the Play Store (Android platform). The same app will also be available at App Store (iOS platform) in a few weeks??? time. Domestic passengers flying from Terminal 3, Delhi Airport by any airline can download the app and register themselves before witnessing the seamless travel experience at the airport. ???DigiYatra??? is a Biometric Enabled Seamless Travel experience (BEST) based on Facial Recognition Technology. It aims to provide a paperless and seamless travel experience to passengers. With this technology, passengers' entry would be automatically processed based on the facial recognition system at all checkpoints including entry into the airport, security check areas, aircraft boarding, etc. The technology will make the boarding process significantly faster and more seamless as each passenger would need less than 3 seconds at every touchpoint. Their face would act as their documents, like ID proof, Vaccine proof, and also act as a boarding pass. It will also ensure enhanced security at the airport as the passenger data is validated with Airlines Departure Control System, thereby only designated passengers can only enter the terminal. The entire process is non-intrusive and automatic leading to the optimization of staff for stakeholders like CISF, airlines, and others.",
        "Aavenir": "Delivering the Future of Work - AI-ready Source-to-Pay Solutions built on the ServiceNow Platform Aavenir???s next-gen Source-to-Pay suite revolutionizes age-old procurement processes by using the latest Machine Learning and Natural Language Processing technologies to reduce cycle time, yet offering insightful best practices suggestions based on historical data. For example, Aavenir???s Contractflow - Contract Lifecycle Management (CLM) product solves the hardest text analytics problems for risk and obligation management while, Invoiceflow - Accounts Payable (AP) automation product solves multi-vendor invoice data extraction and processing problems by harnessing the power of AI & ML technologies. Aavenir SaaS-based source-to-pay solutions are powered by the most advanced cloud-based ServiceNow platform that is delivering unified digital workflows to create great experiences. Also, the ServiceNow platform unlocks productivity for approximately 5,400 enterprise customers worldwide, including Fortune 500 companies. We deliver the future of work! We know that the future of work is changing and we want to be at the forefront of it. Our Values: * Customer success: We believe that when our customers succeed, we succeed naturally. It???s a cohesive process, we are committed to enhancing, always. * Innovation: we strive to leverage modern technologies like AI, ML & NLP to make intelligent solutions for changing the nature of work at organizations. * Joy: our focus is to bring in joy in everything we do, from delivering a joyful user experience for our customers to creating an amazing work culture for our employees so, in turn, they delight our customers. Founded in 2019 by experts having more than 25 years of experience in the S2P industry, Aavenir is a start-up that???s growing fast and headquartered in the USA with an office in India. For more information, please visit www.aavenir.com.www.aavenir.com",
        "Joe": "Today I wrote a script that helped me automate an algorithm.",
        "Goutham": "Both players are given the same string, . Both players have to make substrings using the letters of the string . Stuart has to make words starting with consonants. Kevin has to make words starting with vowels. The game ends when both players have made all possible substrings.",
        "Digiyarata": "The beta version of the DigiYatra app is presently available at the Play Store (Android platform). The same app will also be available at App Store (iOS platform) in a few weeks??? time. Domestic passengers flying from Terminal 3, Delhi Airport by any airline can download the app and register themselves before witnessing the seamless travel experience at the airport. DigiYatra is a Biometric Enabled Seamless Travel experience (BEST) based on Facial Recognition Technology. It aims to provide a paperless and seamless travel experience to passengers. With this technology, passengers' entry would be automatically processed based on the facial recognition system at all checkpoints including entry into the airport, security check areas, aircraft boarding, etc. The technology will make the boarding process significantly faster and more seamless as each passenger would need less than 3 seconds at every touchpoint. Their face would act as their documents, like ID proof, Vaccine proof, and also act as a boarding pass. It will also ensure enhanced security at the airport as the passenger data is validated with Airlines Departure Control System, thereby only designated passengers can only enter the terminal. The entire process is non-intrusive and automatic leading to the optimization of staff for stakeholders like CISF, airlines, and others."
    }

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
    d = {}
    for key in wrdCount.keys():
        d[key] = tuple(d[key] for d in ds)
    print(d)

    # outputs fields to csv file
    fields = ['User', 'Words', 'Technical Words', 'Sentences', 'Similarity']
    with open('out.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for key in d.keys():
            writer.writerow({'User': key, 'Words': d.get(key)[0], 'Technical Words': d.get(key)[1],
                             'Sentences': d.get(key)[2], 'Similarity': d.get(key)[3]})
    end = time.time()


    code = """
def f(x):
    x = x + 1
    return x

print('This is my output.')
"""
#beg = time.time()
#end = time.time()

    #insert text into beginning of code variable
    code = """
import time
begg = time.time()
""" + str(users) + """
endd = time.time()
print('Time taken: ', endd-begg)
    """

    # count the amount of lines of code in the code string
    lines = code.splitlines()
    exec(code)
    print("Line Count", (lines.__len__() + 1) - 4)

    print(end-beg)
