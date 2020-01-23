from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.views.generic import TemplateView
from .forms import PostForm


# Create your views here.

class PostListView(TemplateView):
    
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    template_name = 'blog/post_list.html'
    context = {'post' : post}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

class PostDetailView(TemplateView):

    template_name = 'blog/post_detail.html'
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

    
class PostCreateView(TemplateView):

    template_name = 'blog/post_edit.html'
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):

        form = PostForm(self.request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

        else:
            form = PostForm()

        return render(self.request, self.template_name, self.context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})