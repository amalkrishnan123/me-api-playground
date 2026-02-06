from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

@api_view(['GET','POST'])
def profile(request):
    if request.method == 'GET':
        p = Profile.objects.first()
        return Response(ProfileSerializer(p).data)

    serializer = ProfileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def projects(request):
    skill = request.GET.get('skill')
    qs = Project.objects.all()

    if skill:
        qs = qs.filter(skills__name__icontains=skill)

    return Response(ProjectSerializer(qs, many=True).data)

@api_view(['GET'])
def search(request):
    q = request.GET.get('q')
    projects = Project.objects.filter(title__icontains=q)
    return Response(ProjectSerializer(projects,many=True).data)

@api_view(['GET'])
def skills_top(request):
    skills = Skill.objects.all()
    return Response(SkillSerializer(skills,many=True).data)

@api_view(['GET'])
def health(request):
    return Response({"status":"ok"})
