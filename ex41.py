import random
from urllib.request import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

phrases = {
    "class %%%(%%%)" : "Make a class %%% that is-a %%%",
    "class %%%(object):\ndef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** parameters", 
    "class %%%(object):\ndef ***(self, @@@)" : "class %%% has-a function nnamed *** that takes self and @@@ parameters.",
    "*** = %%%()": "set *** to an instance of class %%%",
    "***.***(@@@)" : "From *** get *** function, and call it with parameters self, @@@",
    "***.*** = '***'" : "From *** get the *** attribute and set it to '***'"
}

# do they want to drill phrases first
phrase_first = False
if len(sys.argv) == 2 and sys.argv[1] == "english" : 
    phrase_first = True

# load up the words from the website
for word in urlopen(word_url).readlines():
    words.append(word.decode('utf-8').strip())

def convert(snippet, phrase) : 
    class_names = [ w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    other_names = random.sample(words, snippet.count("***"))

    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(", ".join(random.sample(words, param_count)))

    # loop through snippet, then loop through phrase
    for sentence in snippet, phrase:
        #copy a new string
        result = sentence[:]

        # fake class names
        for word in class_names : 
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names : 
            result = result.replace("***", word, 1)
        
        # fake params names
        for word in param_names : 
            result = result.replace("@@@", word, 1)
        
        results.append(result)
    # now the results contains modified version of snippets plus phrases
    return results
    
# keep going until they hit ctrl-d 

try : 
    while True:
        snippets = list(phrases.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if phrase_first : 
                question, answer = answer, question

            print(question)

            input("> ")
            print("answer : {}\n\n".format(answer))
except EOFError:
    print("\nBye")

