#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from rest_framework.exceptions import ValidationError


def phone_validator(value):
    if not re.match(r"^(1[3-9])\d{9}$", value):
        raise ValidationError('手机格式错误')