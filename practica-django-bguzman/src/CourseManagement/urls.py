
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url='/catalog/', permanent=True)), #hace que la pagina principal sea la de catalogo(redirige a catalogo)
    path('admin/', admin.site.urls),
    path('catalog/', include('Catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('CatologApi.urls')),
]
