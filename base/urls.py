from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user-registration/', views.userRegister, name="register"),
    path('user-login/', views.userLogin, name="login"),
    path('user-logout/', views.userLogout, name="logout"),
    path('', views.home, name="home"),
    path('fact/facts-need-to-know/', views.allFacts, name="facts"),
    path('fact/create-a-new-fact/', views.createFacts, name="createFacts"),
    path('fact/update-the-fact/<str:pk>/', views.updateFacts, name="updateFacts"),
    path('fact/delete-the-fact/<str:pk>/', views.deleteFacts, name="deleteFacts"),
    path('all-posts/', views.post, name="post"),
    path('all-posts/displaying-post/<str:pk>/', views.displayPost, name="displayPost"),
    path('all-posts/upload-post/', views.uploadPost, name="uploadPost"),
    path('all-posts/update-post/<str:pk>/', views.updatePosts, name="updatePost"),
    path('all-posts/delete-post/<str:pk>/', views.deletePosts, name="deletePost"),
    path('all-posts/update-comments/<str:pk>/', views.updateComments, name="updateComments"),
    path('all-posts/delete-comments/<str:pk>/', views.deleteComments, name="deleteComments"),
    path('all-posts/ask-your-query/', views.askQuery, name="askQuery"),
    path('about-me/', views.about, name="about"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)