import nltk
nltk.download('stopwords')

users = {
    "Akhil": "How do central banks control inflation? The US Federal Reserve typically designs financial policy to achieve an inflation target of 2 % . Inflation targeting is a central banking policy that revolves around adjusting monetary policy to achieve a specified annual rate of inflation. Interest rates can be seen as a mechanism or tool to achieve inflation targeting. When inflation is high, banks will raise interest rates. This has a trickle down effect starting with central banks, going down to commercial banks, and eventually down to commercial bank clients such as businesses and individual consumers.",
    "WAISL": "DigiYatra The beta version of the DigiYatra app is presently available at the Play Store (Android platform). The same app will also be available at App Store (iOS platform) in a few weeks’ time. Domestic passengers flying from Terminal 3, Delhi Airport by any airline can download the app and register themselves before witnessing the seamless travel experience at the airport. ‘DigiYatra’ is a Biometric Enabled Seamless Travel experience (BEST) based on Facial Recognition Technology. It aims to provide a paperless and seamless travel experience to passengers. With this technology, passengers' entry would be automatically processed based on the facial recognition system at all checkpoints including entry into the airport, security check areas, aircraft boarding, etc. The technology will make the boarding process significantly faster and more seamless as each passenger would need less than 3 seconds at every touchpoint. Their face would act as their documents, like ID proof, Vaccine proof, and also act as a boarding pass. It will also ensure enhanced security at the airport as the passenger data is validated with Airlines Departure Control System, thereby only designated passengers can only enter the terminal. The entire process is non-intrusive and automatic leading to the optimization of staff for stakeholders like CISF, airlines, and others.",
    "Aavenir": "Delivering the Future of Work - AI-ready Source-to-Pay Solutions built on the ServiceNow Platform Aavenir’s next-gen Source-to-Pay suite revolutionizes age-old procurement processes by using the latest Machine Learning and Natural Language Processing technologies to reduce cycle time, yet offering insightful best practices suggestions based on historical data. For example, Aavenir’s Contractflow - Contract Lifecycle Management (CLM) product solves the hardest text analytics problems for risk and obligation management while, Invoiceflow - Accounts Payable (AP) automation product solves multi-vendor invoice data extraction and processing problems by harnessing the power of AI & ML technologies. Aavenir SaaS-based source-to-pay solutions are powered by the most advanced cloud-based ServiceNow platform that is delivering unified digital workflows to create great experiences. Also, the ServiceNow platform unlocks productivity for approximately 5,400 enterprise customers worldwide, including Fortune 500 companies. We deliver the future of work! We know that the future of work is changing and we want to be at the forefront of it. Our Values: * Customer success: We believe that when our customers succeed, we succeed naturally. It’s a cohesive process, we are committed to enhancing, always. * Innovation: we strive to leverage modern technologies like AI, ML & NLP to make intelligent solutions for changing the nature of work at organizations. * Joy: our focus is to bring in joy in everything we do, from delivering a joyful user experience for our customers to creating an amazing work culture for our employees so, in turn, they delight our customers. Founded in 2019 by experts having more than 25 years of experience in the S2P industry, Aavenir is a start-up that’s growing fast and headquartered in the USA with an office in India. For more information, please visit www.aavenir.com.www.aavenir.com",
    "Joe": "Today I wrote a script that helped me automate an algorithm.",
    "Goutham": "Both players are given the same string, . Both players have to make substrings using the letters of the string . Stuart has to make words starting with consonants. Kevin has to make words starting with vowels. The game ends when both players have made all possible substrings."
}
output = {}
filteredUsers = {}
stpwords = set(nltk.corpus.stopwords.words('english'))
stpwords.add('the')
stpwords.add('this')
for userName, text in users.items():
    tolowerCase = text.lower()
    filtered = filter(lambda w: not w in stpwords, tolowerCase.split())
    output[userName] = list(filtered)
sentences = {}
print(output)
for userName, text in output.items():
    sentenceCount = 0
    for token in text:
        if (token.endswith(".") or token.endswith("?") or token.endswith("!")):
            sentenceCount+=1
            sentences[userName] = sentenceCount
print(sentences)
