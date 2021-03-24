# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from erpicity.settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from apps.base import urls as base_urls
from apps.login import urls as login_urls
from apps.cadastro import urls as cadastro_urls
from apps.fiscal import urls as fiscal_urls
from apps.vendas import urls as vendas_urls
from apps.compras import urls as compras_urls
from apps.financeiro import urls as financeiro_urls
from apps.estoque import urls as estoque_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_urls)),
    path('login/', include(login_urls)),
    path('cadastro/', include(cadastro_urls)),
    path('fiscal/', include(fiscal_urls)),
    path('vendas/', include(vendas_urls)),
    path('compras/', include(compras_urls)),
    path('financeiro/', include(financeiro_urls)),
    path('estoque/', include(estoque_urls)),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
