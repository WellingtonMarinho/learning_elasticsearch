from django.urls import path
from .views import PeopleSearchView

urlpatterns = [
    path('api/v1/peoples_list/', PeopleSearchView.as_view(), name='peoples-list')

]