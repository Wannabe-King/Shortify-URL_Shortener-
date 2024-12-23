from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('shorten/',views.shorten_url,name='shorten_url'),
    path('stats/',views.show_stats,name='show_stats'),
    path('<str:short_url>/',views.redirect_to_original_url,name='redirect_to_original_url'),
]