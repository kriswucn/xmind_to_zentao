from utils.xmind_utils import XmindUtils

path = r'E:\PythonProjects\xmind_to_zentao\tests\dcc.xmind'
xu = XmindUtils(path)
roots = xu.roots

r = roots[0]

# print(r.getData())

xu.parse(r)

for t in xu.test_cases:
    print(t.getData())
