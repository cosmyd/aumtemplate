from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Member, News, Project, Event, YEvent, Number, Collaborator

def home(request):

    news = News.objects.all().order_by('-id')[:3]
    numbers = Number.objects.all().order_by('id')[:5]
    context = {
        'news': news,
        'numbers': numbers,
        'page_title': "Home"

    }
    return render(request, 'aum/index.html', context)

def about(request):
    members = Member.objects.all()
    context = {
        'members': members,
        'page_title': "About"
    }
    return render(request, 'aum/about.html', context)

class MemberListView(ListView):
    model = Member
    template_name = 'aum/team.html'
    context_object_name = 'members'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Team'
        return data

class NewsListView(ListView):
    model = News
    template_name = 'aum/news.html'
    context_object_name = 'news'
    ordering = ['-date_uploaded']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'News'
        return data

class NewsDetailView(DetailView):
    model = News
    template_name = 'aum/news_detail.html'  

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = self.get_object().title
        return data

def projects(request):
    context = {
        'pastprojects': Project.objects.filter(present=False).order_by('-id')[:2],
        'presentprojects': Project.objects.filter(present=True).order_by('-id')[:2],
        'page_title': "Projects"

    }
    return render(request, 'aum/projects.html', context)

class PresProjectListView(ListView):
    model = Project
    template_name = 'aum/present_projects.html'
    context_object_name = 'projects'
    ordering = ['-id']
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.filter(present=True).order_by('-id')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Present Projects'
        return data

class PastProjectListView(ListView):
    model = Project
    template_name = 'aum/past_projects.html'
    context_object_name = 'projects'
    ordering = ['-id']
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.filter(present=False).order_by('-id')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Past Projects'
        return data

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'aum/project_detail.html' 

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = self.get_object().title
        return data 

class EventListView(ListView):
    model = Event
    template_name = 'aum/events.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Events'
        return data

def YEventView(request, id):

    xevent = Event.objects.get(id = id) 
    context = {
        'event': xevent,
        'yevents': YEvent.objects.filter(event = xevent).order_by('-id'),
        'page_title': xevent.title
    }


    return render(request, 'aum/yevents.html', context)

        

def contact(request):

    return render(request,'aum/contact.html')

def donate(request):
    context = {
        'page_title': "Donate"
    }
    return render(request,'aum/donate.html', context)

def blog(request):
    context = {
        'page_title': "Blog"
    }
    return render(request,'aum/blog.html', context)

def collaborators(request):
    context = {
        'localcollabs': Collaborator.objects.filter(local=True).order_by('-id'),
        'intcollabs': Collaborator.objects.filter(local=False).order_by('-id'),
        'page_title': "Collaborators"
    }
    return render(request,'aum/collaborators.html', context)