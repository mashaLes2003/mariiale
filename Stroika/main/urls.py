from django.urls import path

from . import views
app_name = 'mat'

urlpatterns = [
    path('', views.MaterialView.as_view()),
    path('category/<int:category_id>', views.MaterialListView.as_view(), name = 'categories'),

]