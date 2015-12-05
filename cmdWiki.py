import wikipedia
import warnings
warnings.filterwarnings("ignore")



def summary():
    print wikipedia.summary(search)
    print "To read further, type: content()"
    print "To go to another page, type: new()"

def content():
    print ny.content
    print " "
    print "To go to another page, type: new()"

def new():
    global search
    global ny
    search = raw_input("What new page would you like to search for? ")
    ny = wikipedia.page(search)
    summary()
def language():
    global lang
    lang = raw_input("what language do you speak? ")
    wikipedia.set_lang(lang)
        
new()
