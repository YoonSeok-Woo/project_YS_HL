from django.shortcuts import render

# Create your views here.
from .models import Community,Comment
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import CommunityForm, CommentForm

@require_http_methods(['GET','POST'])
def index(request):
    communities = Community.objects.all()
    context = {
        'communities': communities
    }
    return render(request,'community/index.html',context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = CommunityForm(request.POST)
            if form.is_valid():
                community = form.save(commit = False)
                community.user=request.user
                community.save()
                return redirect('community:detail',community.pk)
        else:
            form = CommunityForm()
        context = {
            'form': form,
        }
        return render(request,'community/create.html',context)

    return redirect('user:login')

def detail(request, commu_pk):
    community = Community.objects.get(pk=commu_pk)
    comments = Comment.objects.filter(community=commu_pk)
    context = {
        'community':community,
        'comments' :comments,
    }
    return render(request,'community/detail.html',context)

@require_http_methods(['GET','POST'])
def update(request, commu_pk):
    community = get_object_or_404(Community,pk=commu_pk)
    if request.user.is_authenticated:
        if request.user==community.user:
            if request.method=='POST':
                form = CommunityForm(request.POST,instance=community)
                if form.is_valid():
                    form.save()
                    return redirect('community:detail',community.pk)
            else:
                form = CommunityForm(instance=community)
        else:            
            return redirect('community:index')
        context = {
            'community':community,
            'form': form,
        }
        return render(request,'community/updated.html',context)
    return redirect('user:login')

@require_http_methods(['GET'])
def delete(request,commu_pk):
    community = get_object_or_404(Community,pk=commu_pk)
    if request.user.is_authenticated:
        if request.user==community.user:
            community.delete()
            return redirect('community:index')
    return redirect('user:login')

@require_POST
def comment_create(request,commu_pk):
    if request.user.is_authenticated:
        community = get_object_or_404(Community,pk=commu_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.community = community
            comment.user = request.user
            comment.save()
        return redirect('community:detail',community.pk)
    return redirect('user:login')

@require_POST
def comment_delete(request,commu_pk,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.user==comment.user:
        if request.user.is_authenticated:
            comment.delete()
    return redirect('community:detail',commu_pk)
