from django.conf.urls import url, include
from django.contrib import admin
import emailsignup.urls

urlpatterns = [
    url(r'^auth/', include(emailsignup.urls)),
    url(r'^admin/', admin.site.urls),
]
