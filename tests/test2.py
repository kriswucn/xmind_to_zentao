from utils.xmind_utils1 import XmindUtils
import csv

path = r'E:\PythonProjects\xmind_to_zentao\tests\dcc.xmind'

xu = XmindUtils(path)
xu.parse_test_cases()

ts = xu.testcases

with open('test.csv', 'w', newline='') as f:
    ff = csv.writer(f)
    for t in ts:
        ff.writerow([t.get('id'), t.get('name'), t.get('step'), t.get('expecting'), t.get('priority')])
