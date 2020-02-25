from django.conf.urls import url, include
from django.contrib import admin
from api.resources import InputDataResource
from api.views import input_data_view
input_data_resource = InputDataResource()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(input_data_resource.urls)),
    url(r'^api/data/', input_data_view),
]
