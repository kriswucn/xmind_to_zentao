from utils.xmind_utils1 import XmindUtils

path = r'F:\py_projects\xmind_to_zentao\tests\dcc.xmind'

xu = XmindUtils(path)
xu.parse_test_cases()

ts = xu.testcases

for t in ts:
    print(t)
