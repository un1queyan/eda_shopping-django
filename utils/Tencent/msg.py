#!/usr/bin/env python
# -*- coding:utf-8 -*-
from eda_shopping import settings
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.sms.v20190711 import sms_client, models
# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

def send_msg(phone,random_code):
        try:
            cred = credential.Credential(settings.SECRET_ID, settings.SECRET_KEY)
            # cred = credential.Credential(
            #     os.environ.get(""),
            #     os.environ.get("")
            # )
            # 实例化要请求产品(以sms为例)的client对象
            # 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量
            client = sms_client.SmsClient(cred, "ap-guangzhou")
            req = models.SendSmsRequest()

            req.SmsSdkAppid = settings.SmsSdk_Appid
            # 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看
            req.Sign = settings.TENCENT_SMS_SIGN
            # 下发手机号码，采用 e.164 标准，+[国家或地区码][手机号]
            # 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号
            req.PhoneNumberSet = [phone]
            # 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看
            req.TemplateID = settings.TENCENT_SMS_TEMPLATE.get('login')
            # 模板参数: 若无模板参数，则设置为空
            req.TemplateParamSet = ["%s"%random_code,"1",]

            # 通过client对象调用DescribeInstances方法发起请求。注意请求方法名与请求对象是对应的。
            # 返回的resp是一个DescribeInstancesResponse类的实例，与请求对象对应。
            resp = client.SendSms(req)


            # 输出json格式的字符串回包

            if resp.SendStatusSet[0].Code == 'OK':
                return True
            print(resp.to_json_string(indent=2))

        except TencentCloudSDKException as err:
            pass