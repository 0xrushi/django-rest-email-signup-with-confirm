from django.conf.urls import url, include
from django.contrib import admin
import apps.emailsignup.urls

from apps.djangostickersmanager.views import StickerUploadView

urlpatterns = [
    url(r'^auth/', include(apps.emailsignup.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^upload/$',StickerUploadView.as_view(), name='file-upload'),
]