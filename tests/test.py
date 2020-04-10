from utils.xmind_utils import XmindUtils

# path = r'E:\01-智慧燃气管理平台\测试202004xx\采集系统v1.2测试用例.xmind'
path = r'E:\PythonProjects\xmind_to_zentao\tests\dcc.xmind'
xu = XmindUtils(path)
roots = xu.roots

r = roots[0]

# print(r.getData())

xu.parse()

# for t in xu.test_cases:
#     print(t.getData())

nodes = xu.test_nodes

for n in nodes:
    xu.node_to_case(n)

cs = xu.test_cases

for c in cs:
    print(c)
