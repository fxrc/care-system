from calculate.get_abnormal_stu import getAbnormalStu

class AbnormalStu(object):
    def entry(self,startdate,enddate,sleepdays,moneydays,failnum,maxmoney,allstuid):
        try:
            return getAbnormalStu(startdate,enddate,sleepdays,moneydays,failnum,maxmoney,allstuid)
        except:
            return {'status': 0, 'errorInfo': "操作出错，请稍候再试", 'data': ''}