from django.http import JsonResponse


def auth_login(request):
    """
    管理员用户登录
    :param request: 从前端框架传过来的请求
    :return: 按这种格式返回
    """
    print(request.body)
    result = {
        'id': 1,
        'name': 'name',
        'username': 'admin',
        'password': '',
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