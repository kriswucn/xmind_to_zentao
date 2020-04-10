# coding:utf-8
import xmind
import os


class XmindUtils(object):
    def __init__(self, path):
        self._roots = []
        self._test_nodes = []
        self._test_cases = []

        if not os.path.exists(path):
            raise FileNotFoundError

        self._workbook = xmind.load(path)
        self._sheets = self._workbook.getSheets()

        for sh in self._sheets:
            self._roots.append(sh.getRootTopic())

    @property
    def roots(self):
        return self._roots

    @property
    def test_nodes(self):
        return self._test_nodes

    @property
    def test_cases(self):
        return self._test_cases

    # 测试节点to测试用例
    def node_to_case(self, node):
        if node is None:
            return
        test_case_dict = {}
        # the node is test node
        node_dict = node.getData()
        test_case_dict.update({'case': node_dict.get('title')})
        # print(node_dict.get('title'))
        # step nodes
        step_nodes = node.getSubTopics()
        # 遍历步骤
        # 步骤编号
        step_num = 1

        # 存放步骤和期望
        step_str = ''
        expecting_str = ''
        for step in step_nodes:
            step_dict = step.getData()
            step_str += step_dict.get('title') + '\r\n'
            # expecting为预期
            # 只取一个只节点
            exps = step.getSubTopics()
            # 有期望的情况
            if len(exps) > 0:
                expecting_node = exps[0]
                expecting_dict = expecting_node.getData()
                expecting_str += expecting_dict.get('title') + '\r\n'

            # 没有期望的情况
            else:
                expecting_str += '\r\n'
        test_case_dict.update({'step': step_str.rstrip('\r\n'), 'expecting': expecting_str.rstrip('\r\n')})

        self._test_cases.append(test_case_dict)

    @staticmethod
    def is_test_case(topic):
        if topic is None:
            raise Exception

        topic_dict = topic.getData()
        markers = topic_dict.get('markers')

        for m in markers:
            if m.find('priority') > -1:
                return True

        return False

    # 解析并添加测试用例
    def parse(self):
        for root in self._roots:
            if root.getSubTopics() is None:
                continue
            module_prefix = root.getData().get('title')
            self.save_test_nodes(root.getSubTopics(), module_prefix)

    # 添加测试用例
    def save_test_nodes(self, topics):
        for t in topics:
            if self.is_test_case(t):
                self._test_nodes.append(t)
            else:
                self.save_test_nodes(t.getSubTopics())
