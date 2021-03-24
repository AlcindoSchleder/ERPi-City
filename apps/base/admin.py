from django.contrib import admin
from .models import Tenants

# Register your models here.


class TenantsAdmin(admin.ModelAdmin):
    model = Tenants
    extra = 0
    readonly_fields = ('pk_tenants', )
    list_display = ('fk_empresas', 'db_name', 'db_mode')
    list_filter = ('fk_empresas', 'db_name', 'db_mode')
    search_fields = ('db_name', 'db_mode')


admin.site.register(Tenants, TenantsAdmin)
