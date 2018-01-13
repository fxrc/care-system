#coding=utf8

from data.update_basic import UpdateBasic
from data.update_score import UpdateScore

from index.focus_table import FocusTable
from index.grow_bar import GrowBar
from index.grow_line import GrowLine

from login.login_if_pass import LoginIfPass
from login.login_session import LoginSession

from office.export import Export
from office.suggestion import Suggestion
from office.get_abnormal_stu import GetAbnormalStu

from person.add_event import AddEvent
from person.get_event import GetEvent
from person.add_focus import AddFocus
from person.cancel_foucs import CancelFocus
from person.card import PersonCard
from person.score import PersonScore
from person.static_info import StaticInfo
from person.trip import PersonTrip

from system.add_one_user import AddOneUser
from system.del_one_role_team import DelOneRoleTeam
from system.del_one_user import DelOneUser
from system.del_one_user_team import DelOneUserTeam
from system.get_one_role_team import GetOneRoleTeam
from system.get_one_user import GetOneUser
from system.get_one_user_team import GetOneUserTeam
from system.get_total_role_team import GetTotalRoleTeam
from system.get_total_user import GetTotalUser
from system.get_total_user_team import GetTotalUserTeam
from system.set_one_role_team import SetOneRoleTeam
from system.set_one_user import SetOneUser
from system.set_one_user_team import SetOneUserTeam
from system.add_one_user_team import AddOneUserTeam
from system.add_one_role_team import AddOneRoleTeam
from login.get_user_role import GetUserRole
import tornado.web
import tornado.ioloop
import json
import io
from data.update_focus import UpdateFocus

from datetime import datetime
import json
import sys
import traceback
from logConfig import logger,errorMessage

class DateEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.__str__()
    return json.JSONEncoder.default(self, obj)



def getErrorMessage(post):
    def diyPost(self_request):
        try:
            urlPath = self_request.request.uri
            body = eval(self_request.request.body)
            user_id = str(body['data']["userId"])
        except:
            try:
                body = eval(self_request.request.body)
                user_id = str(body["userId"])
            except:
                logger.critical('\n\trequest:%s is not contain userId\n'%urlPath)
                user_id='null'
        try:
            post(self_request)
            logger.info('user: %s request url: %s is successful'%(user_id,urlPath))
        except Exception as e:
            # _, reason, exc_tb = sys.exc_info()
            # error = traceback.extract_tb(exc_tb)
            # result = error[len(error) - 1]
            # message=("file: %s--line: %s--errorfunc: %s()--reason: %s" % (result[0], result[1], result[2], reason))
            logger.error(errorMessage(e,user_id,urlPath))
            self_request.finish({"status":0, "errorInfo":"服务器出错，请稍后再试"})
    return diyPost



class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Max-Age", 3628800)
        self.set_header('Content-type','multipart/form-data')
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,authorization")
        self.set_header('Access-Control-Allow-Methods', 'POST,GET,PUT,DELETE,OPTIONS')
        # self.my_session = Session(self)

class GetUserRoleHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(GetUserRole().entry(self))

class GrowLineHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(GrowLine().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class IndexHandler(tornado.web.RequestHandler):
    def get(self,):
        self.render("index.html")

class GrowBarHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(GrowBar().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class FocusTableHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        middledata = FocusTable().entry(self)
            # print(len(middledata["data"]["data"]), len(middledata))
        middletest = json.dumps(middledata, cls=DateEncoder, ensure_ascii=False)
            # print(len(middletest))
        self.finish(middletest)

    def options(self):
        self.set_status(204)
        self.finish()

class StaticInfoHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        middledata = StaticInfo().entry(self)
        middletest = json.dumps(middledata, cls=DateEncoder, ensure_ascii=False)
        self.finish(middletest)

    def options(self):
        self.set_status(204)
        self.finish()


class TripHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(PersonTrip().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()


class CardHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(PersonCard().entry(self,))

    def options(self):
        self.set_status(204)
        self.finish()


class CancelFocusHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        # userID = self.get_argument("userId")
        # stuID = self.get_argument("stuId")
        self.finish(CancelFocus().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()


class AddFocusHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(AddFocus().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class GetEventHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(GetEvent().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class ScoreHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(PersonScore().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()


class AddEventHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(AddEvent().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class ExportHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(Export().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()


class SuggestionHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(Suggestion().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()


class GetTotalUserTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        get_total = GetTotalUserTeam()
        self.finish(get_total.entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class GetOneUserTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(GetOneUserTeam().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class SetOneUserTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(SetOneUserTeam().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class DelOneUserTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(DelOneUserTeam().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class GetTotalRoleTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        get_total = GetTotalRoleTeam()
        self.finish(get_total.entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class GetOneRoleTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(GetOneRoleTeam().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class SetOneRoleTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(SetOneRoleTeam().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class DelOneRoleTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(DelOneRoleTeam().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class GetTotalUserHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        get_total = GetTotalUser()
        self.finish(get_total.entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class GetOneUserHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(GetOneUser().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class SetOneUserHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(SetOneUser().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class DelOneUserHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(DelOneUser().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class AddOneUserTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(AddOneUserTeam().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class AddOneRoleTeamHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(AddOneRoleTeam().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class AddOneUserHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(AddOneUser().entry(self))

    def options(self):
        self.set_status(204)
        self.finish()

class UpdateBasicHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        file = self.request.files['file'][0]
        update = UpdateBasic()
        self.finish(update.entry(file))

    def options(self):
        self.set_status(204)
        self.finish()

class UpdateFocusHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        file = self.request.files['file'][0]
        update = UpdateFocus()
        self.finish(update.entry(file))

    def options(self):
        self.set_status(204)
        self.finish()

class UpdateScoreHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        file = self.request.files['file'][0]
        update = UpdateScore()
        self.finish(update.entry(file))

    def options(self):
        self.set_status(204)
        self.finish()

class LoginIfPassHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(LoginIfPass().entry(self))

class LoginSessionHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(LoginSession().entry(self))

class GetAbnormalStuHandler(BaseHandler):
    @getErrorMessage
    def post(self):
        self.finish(GetAbnormalStu().entry(self))
