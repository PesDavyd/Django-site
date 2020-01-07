from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from django.urls import path
from news.models import News


urlpatterns = [
	path('',
	ListView.as_view(queryset = News.objects.all().order_by("-date")[:20],
	 template_name="news/posts.html")),
	 url('(?P<pk>\d+)/', DetailView.as_view
	 (model = News, template_name = "news/post.html"))
]
