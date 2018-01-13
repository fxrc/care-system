#coding=utf8

from judge_permission import judgeIfPermiss
from get_total_page import getTotalPage
from api_define import set_one_role_team
from orm import *

class SetOneRoleTeam(set_one_role_team):
    """
    设置一个角色组：
    "userId": "admin",
    "userTeamName": "一号角色组",
    "data": {
        "index": 0, //0表示不可以看
        "person": 0,
        "officeExport": 0,
        "officeSuggestion": 0,
        "dataUpdateBasic": 0,
        "dataUpdateScore": 0,
        "systemUserTeam": 0, //用户组权限设定页
        "systemRoleTeam": 0, //角色组权限设定页
        "systemUsers": 0 //用户设定页
    }
    本函数接收该信息，判断userId用户是否拥有该权限并根据结果将其修改入库，返回：
    {
    "status":1,//1表示成功，0表示失败
    "errorInfo":"该用户没有权限"//status为0时，前端展示errorinfo
    }
    """
    def entry(self, response_self):

        body = eval(response_self.request.body)
        user_id = str(body["userId"])
        role_team_name = str(body["roleTeamName"])
        data = eval(str(body["data"]))

        if judgeIfPermiss(user_id=user_id, mode=1, page="systemRoleTeam") == False:
            return {"status":0, "errorInfo":"用户没有权限设置"}
        elif len(MyBaseModel.returnList(new_user_role.select().where(new_user_role.userrolename == role_team_name).dicts())) == 0:
            return {"status":0, "errorInfo":"不存在所要设置的角色组"}
        else:
            return self.updateMysql(role_team_name, data)

    def updateMysql(self, role_team_name, data):
        """更改数据库内的数据"""

        if not set(data) == set(getTotalPage()):
            return {"status":0, "errorInfo":"设置的角色组项与系统当前不符"}
        try:
            with db.execution_context():
                new_user_role.update(**{"permission":str(data)}).where(new_user_role.userrolename == role_team_name).execute()
        except:
            raise
            # return {"status":0, "errorInfo":"更新数据库过程中出错，请稍候重试"}
        return {"status":1, "errorInfo":""}
