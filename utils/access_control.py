from fastapi import Request, HTTPException
import ipaddress
from functools import wraps
import asyncio

def get_request_from_args_kwargs(*args, **kwargs):
    for arg in args:
        if isinstance(arg, Request):
            return arg
    for kwarg in kwargs.values():
        if isinstance(kwarg, Request):
            return kwarg
    raise RuntimeError("Request parameter missing in route function")

def internal_only(func):
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = get_request_from_args_kwargs(*args, **kwargs)
            if request.client.host != "127.0.0.1":
                raise HTTPException(status_code=403, detail="Forbidden: internal API only")
            return await func(*args, **kwargs)
    else:
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = get_request_from_args_kwargs(*args, **kwargs)
            if request.client.host != "127.0.0.1":
                raise HTTPException(status_code=403, detail="Forbidden: internal API only")
            return func(*args, **kwargs)
    return wrapper

def lan_only(func):
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = get_request_from_args_kwargs(*args, **kwargs)
            ip = request.client.host
            try:
                ip_obj = ipaddress.ip_address(ip)
                if not ip_obj.is_private:
                    raise HTTPException(status_code=403, detail="Forbidden: LAN-only access")
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid IP address")
            return await func(*args, **kwargs)
    else:
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = get_request_from_args_kwargs(*args, **kwargs)
            ip = request.client.host
            try:
                ip_obj = ipaddress.ip_address(ip)
                if not ip_obj.is_private:
                    raise HTTPException(status_code=403, detail="Forbidden: LAN-only access")
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid IP address")
            return func(*args, **kwargs)
    return wrapper
