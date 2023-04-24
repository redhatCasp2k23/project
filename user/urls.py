from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='user_index'),
    path('home/',home,name='home'),
    path('report/',report,name='user_report'),
    path('account/profile/',profile,name='profile'),
    path('history/',history,name="history"),
    path('issue/edit/<int:id>',edit,name='user_edit'),
    path('issue/delete/<int:id>',delete,name='user_delete'),
    path('account/upvote/<int:id>', upvote, name='upvote'),
    path('ltd/',ltd,name='ltd'),
    path('ltd/upload/<int:report_id>/',upload_solved_image, name='ltdimg'),

]