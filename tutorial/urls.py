"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import music
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views
from tutorial.quickstart.controller import demo
from music.views import MusicViewSet
from music import views as myView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# url的前缀 musicApp
# router.register(r'music', MusicViewSet,basename="music")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('demo', include('tutorial.quickstart.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('music', MusicViewSet.as_view()),
    path('music/me', myView.snippet_detail),
    path('music/me/<int:pk>', myView.snippet_item_detail),
]
