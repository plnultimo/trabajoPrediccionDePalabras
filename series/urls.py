from django.conf.urls import url
from series import views


urlpatterns = [
    url(r'^series/$', views.serie_list),
    url(r'^series/(?P<pk>[^/]+)/$', views.serie_detail),
    url(r'^seriesTotal/$', views.serie_listando),

    url(r'^listarTexto/$', views.texto_lista),
    url(r'^eliminarTexto/$', views.eliminar_texto),


    url(r'^listarPredicciones/$', views.prediccion_lista),
    url(r'^prediccion/$', views.prediccion),
]