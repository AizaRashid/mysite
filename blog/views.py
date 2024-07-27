from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment,Category,Profile
from .forms import PostForm, CommentForm
from django.contrib.auth.views import LogoutView
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def about(request):
    return render(request,'blog/about.html')

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',''))
    return render(request,'blog/categories.html',{'cats':cats.title().replace('-',''),'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'cat_menu_list':cat_menu_list})


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    cats = Category.objects.all()
    ordering = ['-post_date']

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
   
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class CreatePostView(LoginRequiredMixin,CreateView):
        login_url = '/login/'
        template_name="blog/post_form.html"
        redirect_field_name = 'blog/post_detail.html'

        form_class = PostForm
        model = Post
    
class AddCategoryView(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    redirect_field_name = 'blog/post_detail.html'
    template_name = 'blog/add_category.html'
    model = Category 
    fields = '__all__'
    



class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def add_comment_to_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
            form = CommentForm()
            return render(request, 'blog/comment_form.html', {'form': form})
    else:
        return redirect('post_detail', pk=pk)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

def authorprofile(request, author_id):
    if request.user.is_authenticated:
        author = User.objects.get(pk=author_id)
        profile = Profile.objects.get(user_id=author_id)
        author_profile = Profile.objects.get(user=author)
        author_posts = Post.objects.filter(author=author)
        following = author.profile.followers.filter(id=request.user.id).exists()

        return render(request,'blog/author_profile.html',{"author":author,"following":following,"author_profile":author_profile,"author_posts":author_posts})
    else:
        messages.success(request,("You must be Logged In to see this page!"))
        return redirect('post_list')
@login_required
def follow_toggle(request, author_id):
    author = User.objects.get(pk=author_id)
    if request.user.is_authenticated:
        if author.profile.followers.filter(id=request.user.id).exists():
            author.profile.followers.remove(request.user.profile)
        else:
            author.profile.followers.add(request.user.profile)
            author.profile.save()
            return redirect('post_detail')
    else:
        messages.success(request,("You must be Logged In to Follow!"))
        return redirect('post_list')






