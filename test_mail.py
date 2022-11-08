import smtplib
smtpObj = smtplib.SMTP()
smtpObj.connect("mail.nwpu.edu.cn",25)
smtpObj.login("mapengfei@mail.nwpu.edu.cn","a13566946986")
smtpObj.sendmail("mapengfei@mail.nwpu.edu.cn","499908174@qq.com","dfasdfa")
smtpObj.quit()


smtpObj = smtplib.SMTP_SSL("smtp.nwpu.edu.cn")
smtpObj.login("mapengfei@mail.nwpu.edu.cn","a13566946986")
smtpObj.sendmail("mapengfei@mail.nwpu.edu.cn","499908174@qq.com","dfasdfa")
smtpObj.quit()
