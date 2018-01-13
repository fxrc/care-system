from server.tornado_main import tornado_main
from calculate.updata_stu_sleep_count import updataStuSleepCount
from calculate.updata_stu_cost_count import updataStuCostCount
from calculate.updata_stu_score_count import updataStuScoreCount
from updata_mysql import updataMysql
from multiprocessing import Pool
import os
import traceback
import sys
import time
from logConfig import logger,errorMessage

if __name__=='__main__':
    try:
        while(True):
            try:
                updataStuCostCount()
                #updataStuSleepCount()
                updataStuScoreCount()
                updataStuSleepCount()
                break
            except:
                time.sleep(7200)    #每隔两小时检测一次数据库是否导入完成
        print('updata mysql is ok')
        print('start tornado and updata_mysql')
        if os.name=='posix':
            print('run in linux')
            pools=Pool(2)
            pools.apply_async(tornado_main)
            pools.apply_async(updataMysql)
            pools.close()
            pools.join()
            print('all process is close')
        else:
            print('run in windows')
            tornado_main()
    except Exception as e:
        print(e)
        logger.critical(errorMessage(e))
