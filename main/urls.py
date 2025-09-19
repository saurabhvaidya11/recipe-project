from django.contrib import admin
from django.urls import path
from vege.views import receipes
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vege.views import receipes, delete_receipe, update_receipe, login_page ,register_page, logout_page
from vege import views


urlpatterns = [
    path('', receipes, name="home"),           # root URL → shows recipes
    path('receipes/', receipes, name="receipes"),
    path('delete-receipe/<id>/',delete_receipe, name="delete_receipe"),
    path('update-receipe/<id>/',update_receipe, name="update_receipe"),
    path('admin/', admin.site.urls),
    path('login/', login_page , name='login_page'),
    path('register/', register_page , name='register_page'),
    path('logout/', logout_page , name="logout_page"),
    path('like/<int:id>/', views.like_receipe, name="like_receipe"),
    path('comment/<int:id>/', views.add_comment, name="add_comment"),
    path('delete-comment/<int:id>/', views.delete_comment, name="delete_comment"),
    path('receipe/<int:pk>', views.receipe_detail, name="receipe_detail"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
