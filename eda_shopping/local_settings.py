#!/usr/bin/env python
# -*- coding:utf-8 -*-
LANGUAGE_CODE = 'zh-hans'

# redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://8.130.172.12:6383/0",  # 安装redis的主机的 IP 和 端口
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8'
            },
            "PASSWORD": "123456"  # redis密码
        }
    }
}

# 腾讯云短信的app_id
SECRET_ID = "AKIDRkqkRtMfkbEeqoX1HI9oFSQAk7LQHuIS"

SECRET_KEY = "3sSovpVxA9tQluteAVeZFhwxjGafW8Vd"

SmsSdk_Appid = "1400528911"

TENCENT_SMS_APP_ID = 1400528911

# 腾讯云短信的app_key
TENCENT_SMS_APP_KEY = '8bc6858877d2ca1a70c05bccafff1ebf'

# 腾讯云短信的签名
TENCENT_SMS_SIGN = 'Jade1te'
TENCENT_SMS_TEMPLATE = {
    'register': 977725,
    'login': 977723,
    'reset_pwd': 977728,
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eda-shopping',
        'USER': 'root',
        'PASSWORD': 'Zjy559988!',
        'HOST': '8.130.172.12',
        'PORT': '3307',
    }
}
