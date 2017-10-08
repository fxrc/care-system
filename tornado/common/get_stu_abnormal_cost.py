#coding=utf8
from orm import *
import sys
from datetime import datetime,timedelta
sys.path.append("..")

def getStuAbnormalCost(startdate,enddate,times,money):
    #获取异常消费的学生名单,输入变量依次为：起始时间，结束时间，异常次数，限定金额,两个时间变量为字符串类型
    try:
        allStuId=stu_basic_info.select()
        abnormalStu=[]
        for i in range(len(allStuId)):
            result=judgeStuAbnormalCost(allStuId[i].stuID,startdate,enddate,times,money)
            if result:
                singStu=getStuInformation(allStuId[i])
                abnormalStu.append(singStu)
        return {'status':1,'data':abnormalStu}
    except:
        return {'status':0,'errorInfo':"操作出错，请稍候再试",'data':''}
    
    
def judgeStuAbnormalCost(stuId,startdate,enddate,times,money):
    #判断该学生是否存在异常消费的情况，异常消费返回Ture，没有异常消费返回False
    nowsturecord=stu_transaction_record.select().where(stu_transaction_record.stuID==stuId)
    startdates=startdate.split('-')
    enddates=enddate.split('-')
    startDate=datetime(int(startdates[0]),int(startdates[1]),int(startdates[2]))
    endDate=datetime(int(enddates[0]),int(enddates[1]),int(enddates[2]))
    disDays = (endDate.date() - startDate.date()).days + 1  # 两者相距多少天
    day=timedelta(days=1)
    nowStuRecord=[]
    for i in range(len(nowsturecord)):
        nowStuRecord.append(nowsturecord[i])

    abnomalDays=0
    for i in range(disDays):
        nowdate=startDate+day*i
        addr=0
        todayMoney=0.0
        while addr!=len(nowStuRecord):
            if nowStuRecord[addr].tradingTime.date()==nowdate.date():
                if nowStuRecord[addr].turnover <0:
                    todayMoney=todayMoney+nowStuRecord[addr].turnover  
                nowStuRecord.pop(addr)
                addr=addr-1

            addr=addr+1
        if abs(todayMoney) >=money:
            abnomalDays=abnomalDays+1
    
    if abnomalDays>=times:
        return True
    else:
        return False



def getStuInformation(stu):
    #获取该学生的信息，用于返回给前端
    nowStuInfo={"specialitiesid":stu.specialitiesid,"collegeid":stu.collegeid,
                "state":stu.state,"stuID":stu.stuID,"stuName":stu.stuName,"sex":stu.sex}
    return nowStuInfo