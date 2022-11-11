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
smtpObj.sendmail("499908174@qq.com","mapengfei@mail.nwpu.edu.cn","ddddfasdfa")
smtpObj.quit()

import smtplib
smtpObj = smtplib.SMTP_SSL("smtp.163.com",465)
smtpObj.login("merryjingle@163.com","OCDVFOFNDTXLIXGN")
smtpObj.sendmail("merryjingle@163.com","merryjingle@163.com","ddddfasdfa")
smtpObj.quit()

swaks --to 499908174@qq.com --from mapengfei@mail.nwpu.edu.cn --server smtp.nwpu.edu.cn --auth login --auth-user mapengfei@mail.nwpu.edu.cn  -p 25
swaks --to mapengfei@mail.nwpu.edu.cn --from 499908174@qq.com --server smtp.qq.com --auth plain --auth-user 499908174@qq.com  -tls -p 587
swaks --to 499908174@qq.com --from merryjingle@163.com --server smtp.163.com --auth login --auth-user merryjingle@163.com -p 25
