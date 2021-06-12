from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, ListView, DeleteView, DetailView, UpdateView, RedirectView
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.views.generic.base import TemplateView

from .models import Post, corona_help
from .forms import Postform, Corona_help_form

from taggit.models import Tag


# Create your views here.


class new_post(LoginRequiredMixin, View):
    # Defining the templates and the initial fiels values
    template_name = "blog/new_post.html"
    raise_exception=True
    permission_denied_message = "You are not allowed here"
    form_class = Postform
    initial = {
        'title': 'Enter your title here',
        'discreption': 'The post Discreption',
        'catagoery': 'E.g wednesday_weekly'
    }

    def get(self, request):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.slug = slugify(newpost.title)
            newpost.save()
            form.save_m2m()
            return redirect('blog:home')
        return render(request, self.template_name, {'form': form})

# The view to update the post have to work on the same.
class Update_post(LoginRequiredMixin,UpdateView):
    model= Post
    template_name = 'blog/update_post.html'
    fields = {'title', 'discreption', 'tags', 'body'}

class about_us(ListView):
    template_name = 'blog/about_us.html'    

class Home_view(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 9
    queryset = Post.objects.all().order_by('-published_date')

class wednesday_weekly(ListView):
    model = Post
    template_name = 'blog/wednesday_weekly.html'
    queryset = Post.objects.filter(catagoery="wednesday_weekly")
    context_object_name = 'wednesday_weekly'
    paginate_by = 9

class khund_charcha(ListView):
    model = Post
    template_name = 'blog/khund_charcha.html'
    queryset = Post.objects.filter(catagoery='khund_charcha')
    context_object_name = 'khund_charcha'
    paginate_by = 9


# for the english newspapers
class english_dalies(ListView):
    model = Post
    template_name = 'blog/english_papers.html'
    queryset = Post.objects.filter(catagoery = 'english_dalies')
    context_object_name = 'english_dalies'
    paginate_by = 9

# for english magazines
class english_magazines(ListView):
    model = Post
    template_name = 'blog/english_magazines.html'
    queryset = Post.objects.filter(catagoery = 'english_magazines')
    context_object_name = 'english_magazines'
    paginate_by = 9

# Punjabi dalies
class punjabi_dalies(ListView):
    model = Post
    template_name = 'blog/punjabi_dalies.html'
    queryset = Post.objects.filter(catagoery= 'punjabi_dalies')
    context_object_name = 'punjabi_dalies'
    paginate_by = 9

# Punjabi Magazines
class punjabi_magazines(ListView):
    model = Post
    template_name = 'blog/punjabi_magazine.html'
    queryset = Post.objects.filter(catagoery='punjabi_magazines')
    context_object_name = 'punjabi_magazines'
    paginate_by = 9

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'common_tags': common_tags,
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_related = post.tags.similar_objects()[:8]
    context = {
        'post': post,
        'post_related': post_related,
    }
    return render(request, 'blog/post_detail.html', context)

# Creating views for the corona functionality

class corona_post(View):
    template_name = "blog/corona_help.html"
    form_class = Corona_help_form
    initial = {
        'title': 'Title of the post',
        'discreption': 'Tell us in detail what is your issue so that people can relate and help you out in the same provide your social media links here so people can contact at your ease.',
        'contact': ' e.g +91 6657XXXXXX '
    }

    def get(self, request):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.save()
            return redirect('blog:help_list')
        return render(request, self.template_name, {'form': form})

class corona_help_posts(ListView):
    model = corona_help
    template_name = 'blog/corona_help_list.html'
    queryset = corona_help.objects.all()
    context_object_name = 'corona_help'

class corona_help_detail_view(DetailView):
    model = corona_help
    template_name= 'blog/help_detail.html'

class about_us(TemplateView):
    template_name = 'blog/about_us.html'