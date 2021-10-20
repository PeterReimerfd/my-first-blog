from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#from .views import profile_upload

urlpatterns = [
    path('',views.dataframe,name='dataframe'),
    path('upload-csv/', views.profile_upload, name="profile_upload"),
    path('check-csv/',views.check_csv,name="check_csv"),
    path('test-filter/',views.test_filter,name="test_filter",),
    path('actuallydelete/',views.delete_all,name="delete_all"),
    path('data/', views.data, name='data'),
    path('getColumns', views.get_columns, name='get_columns'),
#    path('',views.post_list,name='post_list'),
#    path('index/',views.index),
#    path('post/<int:pk>/', views.post_detail, name='post_detail'),
#    path('post/new/', views.post_new, name='post_new'),
#    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]