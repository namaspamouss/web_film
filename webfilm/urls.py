from django.urls import path
from webfilm import views

urlpatterns = [
    path('', views.index, name="index_webfilm"),
    path('research', views.research, name="research_webfilm"),
    path('role/<int:id>', views.specific_role, name="role_webfilm"),
    path('actor/<int:id>', views.specific_actor, name="actor_webfilm"),
    path('movie/<int:id>', views.specific_movie, name="movie_webfilm"),
]