# 4. Read & Write to and from files
# Profanity check 

import urllib

def read_text():
    quotes = open("/Users/pavanboro/workspace/Full Stack NanoDegree/Programming with Python/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    profanity_check(contents_of_file)

def profanity_check(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse word")
    else:
        print("Could not scan the document properly")
    
read_text()

