<<<<<<< HEAD

from django.urls import path
from . import views
urlpatterns =[
	path('',views.home, name= 'index')
=======
from django.urls import path
from . import views
urlpatterns =[
	path('',views.index , name= 'index')
>>>>>>> 6a7581b35d56240cf3a535985dd6d48061747cb3
]