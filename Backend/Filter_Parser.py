from os import fpathconf
from tempfile import tempdir


FILTER_PHRASES = ['and', 'or']
PHRASE_COMPARISONS = ['<', '>', '=<', '=<', '==', '!=']
SITE_TAGS = ['geoAddr', 'tz', 'area', 'weatherStationRef', 'yearBuilt', 'geoAddr', 'geoCity', 'geoCountry']
SPACE_TAGS = ['siteRef', 'spaceRef', 'floor', 'space', 'floorNum', ]
EQUIPMENT_TAGS = ['siteRef', 'spaceRef', 'equipRef', 'ac', 'elec', 'meter', 'equip', 'water', 'plant']
POINT_TAGS = ['curVal', 'sensor', 'cmd', 'sp', 'point', 'siteRef', 'equipRef', 'writable', 'unit', 'equipRef', 'fan', 'his', 'minVal', 'maxVal']

#quality improvements- need to verify, either it has just a subject and nothing else, or has everything, cannot have any other combo
###################tested##########################
#upon taking in a phrase from HTML_Request_To_Phrases, return a phrase with info relating to structure of 
# 1. the subject (also add in whether it refers to site, equip, ect (use tag names))
# 2. the comarison (check if in phrase comparisons)
# 3. the value
# 4. the relationship- left and right with pointer to left and right phrases with repsective relationship
class FilterPhrase:
    def __init__(self, FPhrase):
        broken_phrase = ''
        
        #find the location of the operator
        comparison_location = ''
        single_letter = ''
        for i in range(len(FPhrase)):
            if FPhrase[i] in PHRASE_COMPARISONS:
                print("found a single")
                comparison_location = i
                single_letter = True
                break
            elif i+2 < len(FPhrase) and FPhrase[i:i+2] in PHRASE_COMPARISONS:
                print("found a double")
                comparison_location = i
                single_letter = False
                break
        
        print(comparison_location)

        #set the variables
        if comparison_location != '':
            if single_letter:
                self.subject = FPhrase[0:comparison_location]
                self.comparison = FPhrase[comparison_location]
                self.value = FPhrase[comparison_location + 1: len(FPhrase)]
            else:
                self.subject = FPhrase[0:comparison_location]
                self.comparison = FPhrase[comparison_location: comparison_location + 1]
                self.value = FPhrase[comparison_location + 2: len(FPhrase)]
        else:        
            self.subject = FPhrase
            self.comparison = 'no comparison found'
            self.value = 'no value found'

        self.tags = []

        #self.leftrelationship = ''
        #self.rightrelationship = ''

        #call function to analyze the subject and add in 
        #self.SubjectTags = RelatedTagsSearch(self.subject)

    def __str__(self):
        return "subject: " + self.subject + " comparison: " + self.comparison + " value: " + self.value

    #Getters
    def getSubject(self) -> str:
        return self.subject

    def getComparison(self) -> str:
        return self.comparison

    def getValue(self) -> str:
        return self.value

    def addTag(self, tagLabel: str) -> None:
        self.tag = RelatedTagsSearch(self.getSubject())


#given a string of the subject ex: curVal, siteRef, will use the provided subject from the phrase to determine 
#what database tags are associated with the phrase: ex: siteRef belongs to Equipment, points, ect
##or could just take the subject and deal with it in the database as the database may store differently
def RelatedTagsSearch(subject : str):
    tags = []
    if subject in SITE_TAGS:
        tags.append('SITE')
    if subject in SPACE_TAGS:
        tags.append('SPACE')
    if subject in EQUIPMENT_TAGS:
        tags.append('EQUIPMENT')
    if subject in POINT_TAGS:
        tags.append('POINT')
    else:
        tag.appemd("Error: Tag Not Found")

class FilterParser:
    
    def __init__(self, Request: str):
        self.phrases = HTML_Request_To_Phrases(Request)

    def getPhraseList(self) -> list:
        return self.phrases

    def __str__(self):
        temp = ''
        for i in self.phrases:
            temp += i.__str__() + "\n"
        return temp


###################tested##########################
#given the raw filter string, will be reposnible for calling all functions to convert into a form to make the FilterParser
def Parse_HTML_Request(Request: str):
    
    #check if empty request
    if Request == '':
        return ''
    
    #use function to break up request string into phrases
    broken_request_string = HTML_Request_To_Phrases(Request)
    request_phrases = []

    #iterate through split list and get list of phrases
    for phrase in broken_request_string:
        #remove unneeded ands for ******will need to change this behavior later to do something with the ands
        if phrase == 'and':
            continue
        temp_phrase = FilterPhrase(phrase)
        request_phrases.append(temp_phrase)

    return request_phrases

    


###################tested##########################
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




#unit tests
if __name__ == '__main__':

    #HTML_Request_To_Phrases tests
    Request1 = 'site'
    Request2 = ''
    Request3 = 'curVal < 10 and siteRef == "a-0000" and water'

    print(HTML_Request_To_Phrases(Request1))
    print(HTML_Request_To_Phrases(Request2))
    print(HTML_Request_To_Phrases(Request3))
    
    Phrase1 = FilterPhrase('curVal<10')
    Phrase2 = FilterPhrase('siteRef=="a-0000"')
    #Phrase3 = FilterPhrase('')
    

    print(Phrase1)
    print(Phrase2)
    #print(Phrase3)

    listreq = Parse_HTML_Request(Request3)
    for i in listreq:
        print(i)

    testfilterparser = FilterParser(Request3)
    print(testfilterparser)


