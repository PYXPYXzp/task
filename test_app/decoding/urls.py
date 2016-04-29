from django.conf.urls import patterns, url


import views

urlpatterns = patterns('',
                       url(r'^$', views.index,  name='index'),
                       url(r'^decoding/$', views.decode_text, name='decoding'),
                       url(r'^change_text/$', views.change_text,
                           name='change_text')
                       )
