from django.shortcuts import render

# Create your views here.
from .models import Community
from .forms import CommunityForm
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

@require_http_methods(['GET','POST'])
def index(request):
    communities = Community.objects.all()
    context = {
        'communities': communities
    }
    return render(request,'communities/index.html',context)
