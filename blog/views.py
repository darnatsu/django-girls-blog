from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Post
from django.utils import timezone
from django.views.generic import TemplateView
from .forms import PostForm


# Create your views here.

class PostListView(TemplateView):
    
    template_name = 'blog/post_list.html'
    
    def get(self, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
            }

        return render(self.request, self.template_name, context)

class PostDetailView(TemplateView):

    template_name = 'blog/post_detail.html'

    def get(self, *args, **kwargs):

        post_id = kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        context = {
            'post' : post,
        }

        return render(self.request, self.template_name, context)

class PostCreateView(TemplateView):

    template_name = 'blog/post_edit.html'

    def get(self, *args, **kwargs):
        form = PostForm()
        context = { 'form' : form }
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):

        form = PostForm(self.request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.published_date = timezone.now()

            post.save()

            return redirect('post_detail', post_id=post.pk)

        else:

            form = PostForm()

        return render(self.request, self.template_name, self.context)


class PostEditView(TemplateView):
    
    template_name = 'blog/post_edit.html'

    def get(self, *args, **kwargs):

        post_id = kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        form = PostForm(instance=post)

        context = {
            'form' : form
        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        
        post_id = kwargs.get('post_id')
        post = Post.objects.get(id=post_id)

        form = PostForm(self.request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.pk)
        
        return render(self.request, self.template_name, self.context)