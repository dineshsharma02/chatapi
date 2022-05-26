from rest_framework.routers import DefaultRouter
from .views import GenericFileUploadView, MessageView

from django.urls import path,include

router = DefaultRouter(trailing_slash=False)

router.register("file-upload",GenericFileUploadView,basename='generic_file_upload')
router.register("message",MessageView,basename="message_routess")

urlpatterns = [
    path("",include(router.urls))
]
