# -*- coding: utf-8 -*-

from apps.base.models import Tenants
from configs.configs import (
    APP_DBMODE_SINGLE_DATABASE,
    APP_DBMODE_MULTI_DATABASES,
    APP_DBMODE_MULTI_SCHEMAS,
    APP_DBMODES,
)

DEFAULT_DOMAIN = 'erp.icity.net.br'
DEFAULT_DATABASE_NAME = 'erp_icity'


class TenantsConfig:
    """
    Class that define Database Access Mode
    """
    tenant_database = DEFAULT_DATABASE_NAME
    tenant_app_mode = APP_DBMODE_SINGLE_DATABASE
    flag_request_based = False
    pk_company = 0

    def __init__(self, request=None, **kwargs):
        """
        Initialization of the class TenantsConfig
        :param request: default None. If request param is not null
                        then database config is based in the domain of request
                        Obs: This parameter discard kwargs
        :param kwargs:  A dictionary that contains parameter to config database
                        based into Tenants table that store the configuration
                        for each Company:
                        parameters are:
                            pk_company: Primary key of Company assigned to user
                                        loged in
        """
        self.flag_request_based = (request is not None)
        self.pk_company = None

        if kwargs:
            self.pk_company = kwargs['pk_company'] if 'pk_company' in kwargs.keys() else None
            self.tenant_app_mode = kwargs['app_mode'] if 'app_mode' in kwargs.keys() else APP_DBMODE_SINGLE_DATABASE

        if self.flag_request_based and self.pk_company:
            self.flag_request_based = False;
            self.pk_company = None
            return True

        if self.flag_request_based:
            self._set_database_config_from_request(request)
        elif self.pk_company:
            self._set_database_config_from_company()
        else:
            self.tenant_database = DEFAULT_DATABASE_NAME
            self.app_mode = APP_DBMODE_SINGLE_DATABASE

    def _set_database_config_from_request(self, request):
        hostname = request.get_host().split(":")[0].lower()

        self.tenant_database = hostname.replace(DEFAULT_DOMAIN, '')
        if self.tenant_database == '':
            self.tenant_database = None
        else:
            self.tenant_database = self.tenant_database.replace('.', '')
        if not self.tenant_app_mode:
            self.app_mode = APP_DBMODE_SINGLE_DATABASE

    def _set_database_config_from_company(self):
        try:
            _qry_tenants = Tenants.objects.filter(id=self.pk_company)
            if _qry_tenants:
                self.tenant_database = _qry_tenants.db_name \
                    if _qry_tenants.db_name else DEFAULT_DATABASE_NAME
                self.app_mode = _qry_tenants.db_mode \
                    if _qry_tenants.db_mode in APP_DBMODES else APP_DBMODE_SINGLE_DATABASE
        except:
            self.tenant_database = DEFAULT_DATABASE_NAME
            self.app_mode = APP_DBMODE_SINGLE_DATABASE

    def get_app_mode(self):
        return self.tenant_app_mode

    def set_app_mode(self, value):
        if self.tenant_app_mode != value:
            self.tenant_app_mode = value if value in APP_DBMODES else DEFAULT_DATABASE_NAME

    app_mode = property(get_app_mode, set_app_mode)


tenants = Tenants()
