from django.urls import path
from . import views
from .views import(
    MemberListView,
    NewsListView,
    NewsDetailView,
    PastProjectListView,
    PresProjectListView, 
    ProjectDetailView,
    EventListView,


)

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about'),
    path('about/team', MemberListView.as_view(), name='team'),
    path('news', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('projects', views.projects, name='projects'),
    path('projects/past', PastProjectListView.as_view(), name='past-projects'),
    path('projects/present', PresProjectListView.as_view(), name='pres-projects'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('events', EventListView.as_view(), name='events'),
    path('events/<id>', views.YEventView, name='event-detail'),
    
    path('donate/', views.donate, name='donate'),
    #path('collaborators/', CollaboratorsView.as_view(), name='colaborators'),
    path('collaborators/', views.collaborators, name='collaborators'),
    path('blog/', views.blog, name='blog'),
]    