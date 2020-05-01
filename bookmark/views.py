from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark # 어떤 모델의 입력을 받을 것인지 결정
    paginate_by = 6 # 한 페이지에 6개씩 출력

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url'] # 사용자로부터 어떤 필드의 입력을 받을 것인지 결정
    success_url = reverse_lazy('list') # 완료했을 때 'list' 이름의 페이지로 이동
    template_name_suffix = '_create' # 템플릿 파일의 접미사 변경

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')