import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_mail(my_sender, my_pass, my_user):
    judge = True
    try:
        content = '' # 邮件主题内容
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["bridi", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["someone", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "Hello"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25 163, 465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码(授权码不是密码)
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        judge = False
    finally:
        if judge:
            print("邮件发送成功")
        else:
            print("邮件发送失败")


if __name__ == '__main__':
    MY_SENDER = '2109046031@qq.com'  # 发件人邮箱账号
    MY_PASS = 'myyvturhulrtdjjc'  # 发件人邮箱密码
    MY_USER = '2109046031@qq.com'  # 收件人邮箱账号，我这边发送给自己

    send_mail(MY_SENDER, MY_PASS, MY_USER)

# 1683388048@qq.com, zhqgvojadcpkbfej
# 2109046031@qq.com, myyvturhulrtdjjc
# biscuit@163.com, fd83ra