//与后端真实交互的可复用函数均写在这里，方便随时切换调试和线上状态

const basicUrl = ""

export const loginUrl = basicUrl + "/login/if-pass"

export const dataUpdateBasicUrl =  basicUrl + "/data/update-basic"
export const dataUpdateBasicUrlGetModel = basicUrl + "/static/学生关怀系统--基础数据导入模板.xlsx"
export const dataUpdateScoreUrl = basicUrl + "/data/update-score"
export const dataUpdateScoreUrlGetModel = basicUrl + "/static/学生关怀系统--成绩数据导入模板.xlsx"
export const dataUpdateFocusUrl = basicUrl + "/data/update-focus"
export const dataUpdateFocusUrlGetModel = basicUrl + "/static/学生关怀系统--关注信息导入模板.xlsx"

export const systemGetTotalUsersUrl = basicUrl + "/system/get-total-user"
export const systemAddOneUserUrl = basicUrl + "/system/add-one-user"

export const systemGetOneUserUrl = basicUrl + "/system/get-one-user"
export const systemSetOneUserUrl = basicUrl + "/system/set-one-user"
export const systemDelOneUserUrl = basicUrl + "/system/del-one-user"

export const systemGetTotalRoleTeamUrl = basicUrl + "/system/get-total-role-team"
export const systemGetTotalUserTeamUrl = basicUrl + "/system/get-total-user-team"

export const systemAddOneUserTeamUrl = basicUrl + "/system/add-one-user-team"
export const systemDelOneUserTeamUrl = basicUrl + "/system/del-one-user-team"
export const systemSetOneUserTeamUrl = basicUrl + "/system/set-one-user-team"
export const systemGetOneUserTeamUrl = basicUrl + "/system/get-one-user-team"

export const systemAddOneRoleTeamUrl = basicUrl + "/system/add-one-role-team"
export const systemDelOneRoleTeamUrl = basicUrl + "/system/del-one-role-team"
export const systemSetOneRoleTeamUrl = basicUrl + "/system/set-one-role-team"
export const systemGetOneRoleTeamUrl = basicUrl + "/system/get-one-role-team"

export const officeSuggestionUrl = basicUrl + "/office/suggestion"
export const officeDataExporeUrl = basicUrl + "/office/export"
export const officeDataFilterUrl = basicUrl + "/office/get-abnormal-stu"

export const indexMajorFocusTableUrl = basicUrl + "/index/focus-table"
export const indexMajorFocusGrowLineUrl = basicUrl + "/index/grow-line"
export const indexMajorFocusGrowBarUrl = basicUrl + "/index/grow-bar"

export const personGetBasicUrl = basicUrl + "/person/static-info"
export const personGetEventInfoUrl = basicUrl + "/person/get-event"
export const personGetPersonScoreInfoUrl = basicUrl + "/person/score"
export const personGetPersonTripInfoUrl = basicUrl + "/person/trip"
export const personGetPersonCardfInfoUrl = basicUrl + "/person/card"
export const personAddEventInfoUrl = basicUrl + "/person/add-event"
export const personAddFocusInfoUrl = basicUrl + "/person/add-focus"
export const personCancelFocusInfoUrl = basicUrl + "/person/cancel-focus"