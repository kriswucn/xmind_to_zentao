# coding:utf-8
import xmind
from xmind.core.markerref import MarkerRefElement
import os


class XmindUtils(object):
    def __init__(self, path):
        self._roots = []
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
    def test_cases(self):
        return self._test_cases

    @staticmethod
    def is_test_case(topic):
        if topic is None:
            raise TypeError

        topic_dict = topic.getData()
        markers = topic_dict.get('markers')

        for m in markers:
            if m.find('priority') > -1:
                return True

        return False

    # 解析并添加测试用例
    def parse(self, topics):
        for root in self._roots:
            if root.getSubTopics() is None:
                continue

            self.save_test_cases(root.getSubTopics())

    # 添加测试用例
    def save_test_cases(self, topics):
        for t in topics:
            if self.is_test_case(t):
                self._test_cases.append(t)
            else:
                self.save_test_cases(t.getSubTopics())
