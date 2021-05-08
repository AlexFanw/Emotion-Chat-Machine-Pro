from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def auth_login(request):
    """
    管理员用户登录
    :param request: 从前端框架传过来的请求
    :return: 按这种格式返回
    """
    req_body = str(request.body, encoding="utf-8")
    req_body = eval(req_body)
    print(req_body)
    # req_body["password"] = str(req_body["password"], encoding="utf-8")
    # req_body["password"] = eval(req_body["password"])
    # if req_body["username"] != "alexfan" or req_body["password"] != "123456":
    #     return JsonResponse({"isLogin": True, "code": 401, "message": "账户或密码错误"})
    result = {
        'id': 1,
        'name': 'name',
        'username': 'alexfan',
        'password': '123456',
        'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png',
        'status': 1,
        'telephone': '',
        'lastLoginIp': '27.154.74.117',
        'creatorId': 'admin',
        'deleted': 0,
        'roleId': 'admin',
        'lang': 'zh-CN',
        'token': '4291d7da9005377ec9aec4a71ea837f'
    }
    return JsonResponse({"result": result, "code": 200, "message": ""})


@csrf_exempt
def get_user_info(request):
    role = {
        'id': 'admin',
        'name': '管理员',
        'describe': '拥有所有权限',
        'status': 1,
        'creatorId': 'system',
        'createTime': 1497160610259,
        'deleted': 0,
        'permissions': [{
            'roleId': 'admin',
            'permissionId': 'dashboard',
            'permissionName': '仪表盘',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'query',
                'describe': '查询',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'exception',
            'permissionName': '异常页面权限',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query",'
                       '"defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},'
                       '{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete",'
                       '"defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'query',
                'describe': '查询',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'result',
            'permissionName': '结果权限',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'query',
                'describe': '查询',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'profile',
            'permissionName': '详细页权限',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'query',
                'describe': '查询',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'table',
            'permissionName': '表格权限',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"import","defaultCheck":False,"describe":"导入"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'import',
                'describe': '导入',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'form',
            'permissionName': '表单权限',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'query',
                'describe': '查询',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'order',
            'permissionName': '订单管理',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'query',
                'describe': '查询',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'permission',
            'permissionName': '权限管理',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'role',
            'permissionName': '角色管理',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'table',
            'permissionName': '桌子管理',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'query',
                'describe': '查询',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }, {
            'roleId': 'admin',
            'permissionId': 'user',
            'permissionName': '用户管理',
            'actions': '[{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"import",'
                       '"defaultCheck":False,"describe":"导入"},{"action":"get","defaultCheck":False,"describe":"详情"},'
                       '{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete",'
                       '"defaultCheck":False,"describe":"删除"},{"action":"export","defaultCheck":False,'
                       '"describe":"导出"}]',
            'actionEntitySet': [{
                'action': 'add',
                'describe': '新增',
                'defaultCheck': False
            }, {
                'action': 'import',
                'describe': '导入',
                'defaultCheck': False
            }, {
                'action': 'get',
                'describe': '详情',
                'defaultCheck': False
            }, {
                'action': 'update',
                'describe': '修改',
                'defaultCheck': False
            }, {
                'action': 'delete',
                'describe': '删除',
                'defaultCheck': False
            }, {
                'action': 'export',
                'describe': '导出',
                'defaultCheck': False
            }],
            'actionList': 'null',
            'dataAccess': 'null'
        }]
    }
    userInfo = {
        'id': '4291d7da9005377ec9aec4a71ea837f',
        'name': 'Alex Fan',
        'username': 'alexfan',
        'password': '123456alex',
        'avatar': '/avatar2.jpg',
        'status': 1,
        'telephone': '',
        'lastLoginIp': '27.154.74.117',
        'lastLoginTime': 1534837621348,
        'creatorId': 'admin',
        'createTime': 1497160610259,
        'merchantCode': 'TLif2btpzg079h15bk',
        'deleted': 0,
        'roleId': 'admin'
    }
    userInfo['role'] = role
    return JsonResponse({"result": userInfo})


@csrf_exempt
def return_2_step_code(request):
    return JsonResponse({"stepCode": 1})


@csrf_exempt
def auth_logout(request):
    return JsonResponse({"message": "注销成功"})
