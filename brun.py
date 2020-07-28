# -*- coding:utf-8 -*-
import time
import os
from base import HTMLTestRunnerCN, readConfig, send_report_to_ding
import unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib


def send_email(filename):
    mail_host = 'smtp.qq.com'
    port = 465  # 端口
    mail_user = '912041511@qq.com'  # 邮箱名
    mail_pass = 'pwitsrzesjesbebc'  # 密码

    sender = '912041511@qq.com'  # 发送邮件名
    receivers = ['912041511@qq.com']
    message = MIMEMultipart('related')

    f = open(filename, 'rb')
    mail_body = f.read()
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename = "report.html"'
    message.attach(att)
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    message.attach(msg)

    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = Header("lemon 接口测试报告", "utf-8")

    smtp = smtplib.SMTP_SSL(mail_host, port)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()


def report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    filename = os.path.join(testreport, lists[-1])
    print(filename)
    return filename


def update_config():
    baseurl = readConfig.ReadConfig.get_http('baseurl')
    print(baseurl)


def result_data(result, domain):
    total_case = result.success_count + result.error_count + result.failure_count
    failCase = result.failCase.replace('<li>', '').replace('</li>', '\n')
    errorCase = result.errorCase.replace('<li>', '').replace('</li>', '\n')
    result_data = '测试环境：' + domain + '\n' + '测试结果: ' + ' 共' + str(total_case) + ',' + ' 通过' + str(
        result.success_count) + ',' + ' 失败' + str(
        result.failure_count) + ',' + ' 错误' + str(
        result.error_count) + '\n' + '失败用例集：' + '\n' + failCase + '\n' + '错误用例集：' + '\n' + errorCase
    return result_data


if __name__ == '__main__':
    root = os.path.abspath(os.path.dirname(__file__)) #获取上级目录
    # root = os.getcwd()
    print("root:",root)
    # root = "E:\\python\\testcase"
    domain = readConfig.ReadConfig.get_http('baseurl')
    testcase_dir = root + '\\b_testcase'

    print(testcase_dir)
    discover = unittest.defaultTestLoader.discover(testcase_dir, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = root + '\\report\\' + now + '_result.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp, domain=domain, title='接口测试报告', description='测试结果如下')
    result = runner.run(discover)
    fp.close()
    test_report = root + "\\report"
    rep = report(test_report)
    result_data = result_data(result, domain)
    # send_report_to_ding.dingmessage(str(result), result_data, str(rep))
    send_email(rep)
