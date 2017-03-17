import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Runner', 'plans'))
import SAXparser
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Runner', 'gui'))
import mainWindow

testCases = SAXparser.parseFile('plans/testPlan1.xml')
mainWindow.createWindow(testCases)