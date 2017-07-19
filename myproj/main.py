# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale

import unittest

from testcases.bugfree_login_or_condition import *


def main():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(BugfreeAdminLoginLogout))
    #不生成报表
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #生成报表
    fp = open('./reports/test_result_%s.html' % time.strftime("%Y-%m-%d-%H-%M-%S"), 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title=u'后台管理-用户管理',
                            description=u'复制-用户创建-用户组创建')
    runner.run(suite)


if __name__ == "__main__":
    main()