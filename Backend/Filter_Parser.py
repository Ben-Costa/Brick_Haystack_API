from tempfile import tempdir


FILTER_PHRASES = ['and', 'or']
PHRASE_COMPARISONS = ['<', '>', '=<', '=<', '==', '!=']
SITE_TAGS = []
EQUIPMENT_TAGS = []


#upon taking in a phrase from HTML_Request_To_Phrases, return a phrase with info relating to structure of 
# 1. the subject (also add in whether it refers to site, equip, ect (use tag names))
# 2. the comarison (check if in phrase comparisons)
# 3. the value
class FilterPhrase:
    def __init__(self, FPhrase):
        broken_phrase = ''

class FilterParser:
    
    
    def __init__(self, Request):
        self.requestbody = Parse_HTML_Request(Request)
        self.siteFilters 
        self.spaceFilters
        self.equipmentFilters
        self.pointFilters

#given the raw filter string, will be reposnible for calling all functions to convert into a form to make the FilterParser
def Parse_HTML_Request(Request: str):
    pass

#given the raw filter string, find each of the phrases in the string and store in a list of phrases
#Parameters- passed the request string
#returns- list of parameters
def HTML_Request_To_Phrases(Request: str):
    phrases = []
    broken_by_words = Request.split()
    tempStr = ''
    for i in range(len(broken_by_words)):
        if broken_by_words[i] in FILTER_PHRASES:
            #tempStr = tempStr + str(broken_by_words[i])
            phrases.append(tempStr)
            phrases.append(broken_by_words[i])
            i = i+1
            tempStr = ''
        else:
            tempStr = tempStr + str(broken_by_words[i])
    phrases.append(tempStr)
    return phrases

def SubjectReferenceClassification(Phrase: FilterPhrase):
    pass

if __name__ == '__main__':

    #HTML_Request_To_Phrases tests
    Request1 = 'site'
    Request2 = ''
    Request3 = 'curVal < 10 and siteRef == "a-0000" and water'

    print(HTML_Request_To_Phrases(Request1))
    print(HTML_Request_To_Phrases(Request2))
    print(HTML_Request_To_Phrases(Request3))

