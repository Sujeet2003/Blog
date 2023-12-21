from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user-registration/', views.userRegister, name="register"),
    path('user-login/', views.userLogin, name="login"),
    path('user-logout/', views.userLogout, name="logout"),
    path('', views.home, name="home"),
    path('facts-need-to-know/', views.allFacts, name="facts"),
    path('create-a-new-fact/', views.createFacts, name="createFacts"),
    path('update-the-fact/<str:pk>/', views.updateFacts, name="updateFacts"),
    path('delete-the-fact/<str:pk>/', views.deleteFacts, name="deleteFacts"),
    path('all-posts/', views.post, name="post"),
    path('displaying-post/<str:pk>/', views.displayPost, name="displayPost"),
    path('displaying-post/', views.uploadPost, name="uploadPost"),
    path('update-post/<str:pk>/', views.updatePost, name="updatePost"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)