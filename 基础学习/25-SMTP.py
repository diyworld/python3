
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "1964128066@qq.com"    # 邮件发送者
#passwd = "tslxfxpipsjyejdb" # CardDAV/CalDAV服务密码
passwd = "jfuzcvmjcvxpdfji"  # IMAP/SMTP服务密码
recver = ["1964128066@qq.com"]  # 邮件接收者

msg = MIMEText("Python 邮件发送测试 ...", "plain", "utf-8")
msg["From"] = Header("test From", "utf-8")
msg["To"] = Header("test To", "utf-8")
msg["Subject"] = Header("Python SMTP 邮件测试", "utf-8")

try:
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtpObj.login(sender, passwd)
    smtpObj.sendmail(sender, recver, msg.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 发送邮件失败")

