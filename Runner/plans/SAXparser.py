from xml.sax import handler, make_parser
from xml.dom import minidom
Test_file = open('plans/testPlan1.xml','r')
xmldoc = minidom.parse(Test_file)

Test_file.close()

class TestSuit:
    def __init__(self):
        self.name = ""
        self.testCases = []
        
    def __str__(self):
        string = self.name + "\n"
        #print self.name
        for test in self.testCases:
        #    print test
            string += str(test) + "\n"
        return string
    
    def getTestCases(self):
        return self.testCases
    
    def setId(self, id):
        self.id = id
        
    def getId(self):
        return self.id
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name

class TestCase:
    def __init__(self):
        self.name = ""
        self.path = ""
        
    def __str__(self):
        return self.name + ": " + self.path + ": " + self.getId()
        
    def setId(self, id):
        self.id = id
        
    def getId(self):
        return self.id
    
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setPath(self, path):
        self.path = path
        
    def getPath(self):
        return self.path

class TestSuitHandler(handler.ContentHandler):
    
    def __init__(self):
        self.inTestSuit = False
        self.inTestCase = False
        self.inName = False
        self.inPath = False
        self.suitList = []
        self.caseList = []
        
    def getSuitList(self):
        return self.suitList
    
    def startElement(self, name, attrs):                        
        # ulozeni stavu, kde se prave ve XML nachazime
        if(name == "testSuit"):
            self.inTestSuit = True
            self.testSuit = TestSuit()
            self.testSuit.setId(attrs.get("id"))
        elif (name == "testCase"):
            self.inTestCase = True
            self.testCase = TestCase()
            self.testCase.setId(attrs.get("id"))
        elif (name == "name"):
            self.inName = True
        elif (name == "path"):
            self.inPath = True
    # prekryti metody endElement(self, name)
    def endElement(self, name):
        # ulozeni stavu, kde se prave ve XML nachazime
        if(name == "testSuit"):
            self.inTestSuit = False
            self.testSuit.testCases = self.caseList
            self.suitList.append(self.testSuit)
            self.caseList = []
        elif (name == "testCase"):
            self.inTestCase = False
            self.caseList.append(self.testCase)
        elif (name == "name"):
            self.inName = False
        elif (name == "path"):
            self.inPath = False

    # prekryti metody characters(self, chrs)    
    def characters(self, chrs):                                 
        if self.inName:
            if self.inTestCase:
                self.testCase.setName(chrs)
            else:
                self.testSuit.setName(chrs)
        elif self.inPath:
            self.testCase.setPath(chrs)
    
def printCases(caseList):
    for case in caseList:
        print case
        
def parseFile(fileName):
    handler = TestSuitHandler()
    
    parser = make_parser()
    parser.setContentHandler(handler)
    
    inFile = open(fileName, 'r');
    
    parser.parse(inFile)

    testCases = handler.getSuitList()

#    printCases(testCases)
    
    return testCases