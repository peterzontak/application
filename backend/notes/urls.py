from django.urls import path
# from config.config import load_config
from . import views


app_name = 'notes'

# config = load_config()

urlpatterns = [
    path('', views.notes_show_view, name="index"),
    path('<note>', views.notes_show_view, name="show"),
]

# for route_name in config['routes'].keys():
#     view_name = route_name + '_view'
#     if hasattr(views, view_name) and callable(getattr(views, view_name)):
#         urlpatterns.append(path(config['routes'][route_name], getattr(views, view_name), name=route_name))

