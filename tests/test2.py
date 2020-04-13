from utils.xmind_utils import XmindUtils
import csv
import utils.logging_utils as lu
import logging
import utils.file_utils as fu

logger = lu.Logger(__name__, cmd_level=logging.INFO, file_level=logging.INFO)

path = r'dcc.xmind'

xu = XmindUtils(path)
xu.parse_test_cases()

ts = xu.testcases

csv_file = fu.get_csv_name_via_xmind(path)

with open(csv_file, 'w', newline='') as f:
    ff = csv.writer(f)
    for t in ts:
        ff.writerow([t.get('id'), t.get('name'), t.get('step'), t.get('expecting'), t.get('priority')])
        logger.logger.info('解析测试用例 -> %s' % t.get('name'))
