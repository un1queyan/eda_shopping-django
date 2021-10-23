from django.shortcuts import render

# Create your views here.
import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import account
from django_redis import get_redis_connection
from utils.SqlUtils import sqlhelpers


class MessageView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        发送短信验证码
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 1. 获取手机号
        # 2. 进行手机格式的校验
        ser = account.MessageSerializer(data=request.query_params)
        print(ser)
        if not ser.is_valid():
            return Response({"status": False, 'message': "手机号格式错误"})

        phone = ser.validated_data.get('phone')
        print(phone)
        obj = sqlhelpers.SqlHelper()
        obj.connect()
        tel = obj.get_one("select u_tel from users where u_tel = %s", [phone,])
        print(tel)
        print(phone + "phone")
        if tel.get("u_tel") != phone:
            return Response({"status": False, 'message': "手机号不存在"})
        obj.close()
        phone = '+86' + phone
        print(phone)
        # 3. 生成随机验证码并发送到手机
        import random

        random_code = random.randint(1000, 9999)
        # 4. 把验证码发送到手机上
        # res = msg.send_msg(phone,random_code)
        # if not res:
        #     return Response({"status": False, 'message': '短信发送失败'})
        # 5. 把验证码存到redis并设置超时时间
        print(random_code)
        conn = get_redis_connection()
        print(conn)
        # conn.set("test", "100", ex=8)
        conn.set(random_code, tel.get("u_tel"), ex=60)
        return Response({"status": True, 'message': '短信发送成功'})

class LoginView(APIView):
    def post(self, requset, *args, **kwargs):
        print(requset.data)
        '''
        1. 校验手机还格式是否合法
        2. 校验验证码 redis中有无
            - 无验证码
            - 有验证码，输入错误
            - 有验证码， 成功

        4. 将一些信息返回给小程序
        '''
        # step：1
        ph = requset.data.get('phone')
        print(ph)
        code = requset.data.get('code')

        # ser = account.LoginSerializer(data=requset.data)
        # if not ser.is_valid():
        #     return Response({'status': False, 'message': '验证码错误'})
        # 2. 从redis中获取验证码
        conn = get_redis_connection()
        tel = conn.get(code)
        tel = str(tel, encoding="utf8")
        if not tel or tel != ph:
            return Response({'status': False, 'message': '验证码错误'})
        # 3.去数据库中获取用户信息
        from api import models
        # phone = ser.validated_data.get('phone')
        obj = sqlhelpers.SqlHelper()
        obj.connect()
        tel = obj.get_one("select u_tel from users where u_tel = %s", [tel, ])
        if not tel:
            return Response({"status": False, 'message': "手机号不存在"})
        print(tel)
        obj.close()
        # if not user:
        #     models.UserInfo.objects.create(phone=phone,token=str(uuid.uuid4()))
        # else:
        #     user.token = str(uuid.uuid4())
        #     user.save()
        phone = requset.data.get('phone')
        code = requset.data.get('code')
        print(phone, code)
        return Response({"status": True, 'msg': "登陆成功"})
