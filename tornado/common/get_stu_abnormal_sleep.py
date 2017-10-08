#coding=utf8
from orm import *
import sys
from datetime import datetime,timedelta
sys.path.append("..")

def getStuAbnormalSleep(startdate,enddate,days):
    #获取归寝存在异常的学生名单,输入变量依次为：起始时间，结束时间，异常次数，两个时间变量为字符串类型
    try:
        allStuId=stu_basic_info.select()
        abnormalStu=[]
        for i in range(len(allStuId)):
            result=judgeStuAbnormalSleep(allStuId[i].stuID,startdate,enddate,days)
            if result:
                singStu=getStuInformation(allStuId[i])
                abnormalStu.append(singStu)
        return {'status':1,'data':abnormalStu}
    except:
        print('find sleep fail ')
        return {'status':0,'errorInfo':"操作出错，请稍候再试",'data':''}


def judgeStuAbnormalSleep(stuId,startdate,enddate,days):
    #判断该学生是否存在归寝的情况，异常返回Ture，没有异常或出错返回False
    nowStuRecord=entry_and_exit.select().where(entry_and_exit.stuID==stuId).order_by(entry_and_exit.id)
    startdates=startdate.split('-')
    enddates=enddate.split('-')
    startDate=datetime(int(startdates[0]),int(startdates[1]),int(startdates[2]))
    endDate=datetime(int(enddates[0]),int(enddates[1]),int(enddates[2]))
    # disDays = (endDate - startDate).days + 1  # 两者相距多少天
    # day=timedelta(days=1)
    # nowStuRecord=[]
    # for i in range(len(nowsturecord)):
    #     nowStuRecord.append(nowsturecord[i])
    abnomalDays=0
    startFlag=0
    for i in range(len(nowStuRecord)):
        if nowStuRecord[i].entryDate!=None and startFlag==0:
            if (nowStuRecord[i].entryDate.date()-startDate.date()).days>=0:
                startFlag=1
        if startFlag==1:
            if nowStuRecord[i].exitDate!=None:  #出去的时间不为null
                if i<len(nowStuRecord)-1 and nowStuRecord[i+1].entryDate!=None: #进来的时间不为null且还不是最后一个记录
                    if nowStuRecord[i].exitDate.date()!=nowStuRecord[i+1].entryDate.date(): #外出跟回来不是同一天
                        abnomalDays=abnomalDays+1   #异常天数加1

        if  startFlag==1 and nowStuRecord[i].entryDate!=None:
            if (nowStuRecord[i].entryDate.date() - endDate.date()).days >=0:  #到达截至日期,不包含当天的统计
                break

    if abnomalDays>=days:
        return True
    else:
        return False



def getStuInformation(stu):
    #获取该学生的信息，用于返回给前端
    nowStuInfo={"specialitiesid":stu.specialitiesid,"collegeid":stu.collegeid,
                "state":stu.state,"stuID":stu.stuID,"stuName":stu.stuName,"sex":stu.sex}
    return nowStuInfo