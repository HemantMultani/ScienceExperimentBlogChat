from django.contrib import admin
from django.urls import path
from posts import views as pv
from chat import views as cv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pv.index, name='index'),
    path('post/<str:name>', pv.post, name='post'),
    path('post/<str:exp>/chat', cv.chat_home, name='chat'),
    path('<str:room>/', cv.room, name='room'),
    path('post/<str:exp>/checkview', cv.checkview, name='checkview'),
    path('send', cv.send, name='send'),
    path('getMessages/<str:room>/', cv.getMessages, name='getMessages'),
]
