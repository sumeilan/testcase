# -*- coding:utf-8 -*-
import time, sys, os

sys.path.append('D:\\chuman_Interface\\test_case')
sys.path.append('D:\\chuman_Interface\\pubilc')
from base import HTMLTestRunner
import unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib


def send_email(filename):
    mail_host = 'smtp.qq.com'
    port = 465  # 端口
    mail_user = '912041511@qq.com'  # 邮箱名
    mail_pass = 'aospagluwfcbbdgb'  # 密码

    sender = '912041511@qq.com'  # 发送邮件名
    # receivers = ['yanhuo@dreampix.cn', 'shiyuan@dreampix.cn', 'sumeilan@dreampix.cn', 'yuqin@dreampix.cn']  # 收件人
    receivers = ['sumeilan@dreampix.cn']
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
    message['Subject'] = Header("接口自动化测试报告", "utf-8")

    smtp = smtplib.SMTP_SSL(mail_host, port)
    # smtp.connect(mail_host)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()


def report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    filename = os.path.join(testreport, lists[-1])
    print(filename)
    return filename


if __name__ == '__main__':
    test_dir = 'D:\\chuman_Interface\\test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'D:\\chuman_Interface\\report\\' + now + '_result.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="接口自动构建测试报告", description="测试结果如下(可下载并用浏览器打开查看完整附件)：")
    runner.run(discover)
    fp.close()

    test_report = "D:\\chuman_Interface\\report"
    rep = report(test_report)
    send_email(rep)
