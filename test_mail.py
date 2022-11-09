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

import smtplib
smtpObj = smtplib.SMTP_SSL("smtp.qq.com")
smtpObj.login("499908174@qq.com","sqzumccutcqvbiaf")
smtpObj.sendmail("499908174@qq.com","mapengfei@mail.nwpu.edu.cn","dfasdfa")
smtpObj.quit()
