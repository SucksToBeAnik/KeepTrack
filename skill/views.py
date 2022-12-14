from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import F

from .models import Skill
from .forms import SkillForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login-page")
def single_skill_page(request,pk):
    profile = request.user.profile

    try:
        skill = profile.skill_set.get(id=pk)
    except:
        messages.info(request,'You are not authorized to view this page!')
        return redirect('home-page')
    form = SkillForm(instance=skill)

    if request.method == 'POST' and request.POST.get("action") == "delete" and skill.owner == request.user.profile :
        skill.delete()
        messages.success(request, f"Your skill on {skill.title} has been successfully deleted!")
        return redirect('skill-page')
    elif request.method == 'POST' and request.POST.get("action") == "update" and skill.owner == request.user.profile:
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            return redirect('single-skill-page',pk=skill.id)
    context = {
        'skill':skill,
        'form':form,
    }
    return render(request,'skill/single_skill_page.html',context)

@login_required(login_url="login-page")
def skill_form_page(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
            messages.success(request,'A new skill has been successfully added!')
            return redirect('skill-page')
        else:
            messages.error(request,'An error has occured. Please try again.')
            return redirect('skill-form-page')
    context = {
        'form':form,
    }
    return render(request,'skill/skill_form_page.html',context)


@login_required(login_url="login-page")
def skill_page(request):
    profile = request.user.profile
    
    queryset =profile.skill_set.all()

    context = {
        'queryset':queryset,
    }
    return render(request,'skill/skill_page.html',context)