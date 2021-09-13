from django.conf.urls import url
from .controller.demo import DemoViewSet

urlpatterns = [
    
    url(r'^$', DemoViewSet.as_view(), name='hello'),
]