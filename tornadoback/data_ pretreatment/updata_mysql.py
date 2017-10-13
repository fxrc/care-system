from datetime import datetime
import time
from calculate.updata_stu_cost_count import updataStuCostCount
from calculate.updata_stu_sleep_count import updataStuSleepCount

def updataMysql():
    nowdate=datetime.today().date()
    while True:
        if nowdate!=datetime.today().date():    #到了新的一天了
            if int(time.strftime("%H%M%S"))>10000:  #凌晨一点开始更新
                print('start updata mysql data')
                updataStuSleepCount()
                updataStuCostCount()
                nowdate=datetime.today().date() #日期更新为今天
        time.sleep(1800)    #每次循环间隔半小时
