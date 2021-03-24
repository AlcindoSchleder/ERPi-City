# -*- coding: utf-8 -*-

import re
import threading
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from erpicity.settings import LOGIN_NOT_REQUIRED
from configs.configs import APP_DBMODE_MULTI_DATABASES

from .utils import tenants

# from uuid import uuid4

# from django.db import connections

THREAD_LOCAL = threading.local()


class TenantMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if tenants.db_mode == APP_DBMODE_MULTI_DATABASES:
            setattr(THREAD_LOCAL, "DB", tenants.tenant_database)
            return self.get_response(request)
        elif tenants.db_mode == APP_DBMODE_MULTI_DATABASES:
            return tenants.tenant_database
        else:
            return self.get_response(request) # pareii aqui tem algo errado aqui....
            # response = self.get_response(request)
            # return response


def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)


class LoginRequiredMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None, *args, **kwargs):
        self.exceptions = tuple(re.compile(url) for url in LOGIN_NOT_REQUIRED)
        self.get_response = get_response

        return super(LoginRequiredMiddleware, self).__init__(get_response, *args, **kwargs)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Caso o user ja esteja logado:
        if request.user.is_authenticated:
            for url in self.exceptions:
                if url.match(request.path):
                    return redirect('base:index')
            return None

        for url in self.exceptions:
            if url.match(request.path):
                return None

        return redirect('login:loginview')
