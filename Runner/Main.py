import sys
sys.path.insert(0, "/home/matt/Dokumenty/eclipse_workspace/Runner/plans")
import SAXparser
sys.path.insert(0, "/home/matt/Dokumenty/eclipse_workspace/Runner/gui")
import mainWindow


testCases = SAXparser.parseFile('plans/testPlan1.xml')
mainWindow.createWindow(testCases)