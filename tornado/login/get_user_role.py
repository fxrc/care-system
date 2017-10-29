from api_define import get_user_role
from common.get_user_role import getUserRole
import redis
import json

class GetUserRole(get_user_role):
    def entry(self, response_self):
        body = eval(response_self.request.body)
        user_name = str(body["userId"])
        r=redis.Redis(host='127.0.0.1',port=6379)
        result=r.get(user_name)
        if result!=None:
            r.expire(user_name, 1800)   #继续保持登录状态30分钟
            userRole=getUserRole(user_name)
            return json.dumps({"status": 1, 'data': userRole,}, ensure_ascii=False)
        else:
            return json.dumps({"status":0,'data':'','errorinfo':'未登录'})
