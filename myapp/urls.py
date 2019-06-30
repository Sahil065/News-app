from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$',views.business,name='business'),
    url(r'^entertainment/$',views.entertainment,name='entertainment'),
    url(r'^sports/$',views.sports,name='sports'),
    url(r'^health/$',views.health,name='health'),
    url(r'^science/$',views.science,name='science'),
    url(r'^technology/$',views.technology,name='technology'),

]