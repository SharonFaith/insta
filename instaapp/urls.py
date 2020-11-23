from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import welcome, index, profile, upload_image, update_profile, search_results, single_image, comments
from django.conf.urls.static import static

urlpatterns = [
    path('', welcome, name = 'welcome'),
#    path('search/', search_results, name = 'search_results'),
    path('landing-page/', index, name = 'index'),
    path('profile/<id>/', profile, name='profile'),
    path('upload_pic/', upload_image, name='upload-pic'),
    path('update_profile/', update_profile, name='update-profile'),
    path('search/', search_results, name='search-results'),
    path('comment/', comments, name='add-comment'),
    path('image/<image_id>/', single_image, name='single-image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 