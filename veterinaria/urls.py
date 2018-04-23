from django.contrib import admin
from django.urls import path, include

from django.conf.urls import  url
from django.conf import settings
from django.views.static import serve

from accounts import urls as accounts_urls
#from alimento import urls as alimento_urls
#from animal import urls as animal_urls
#from medicamento import urls as medicamento_urls





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    #path('alimento/', include(alimento_urls, namespace='accounts')),
    #path('animal/', include(animal_urls, namespace='accounts')),
    #path('medicamento/', include(medicamento_urls, namespace='accounts')),
    url(
        regex=r'media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    )
]
