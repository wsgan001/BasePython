#coding=utf8
from functools import wraps
from flask import g
from .errors import forbidden


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')  #如果用户不具有指定权限则返回错误
            return f(*args, **kwargs)
        return decorated_function
    return decorator
