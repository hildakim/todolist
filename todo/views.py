from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.core.paginator import Paginator
from django.http import HttpResponse
import json
from django.utils import timezone
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

def todo(request):
    contents = Todo.objects.all()

    todo_list = Todo.objects.all().order_by('-id')
    paginator = Paginator(todo_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    today = DateFormat(datetime.now()).format('Y-m-d')
    today_list = Todo.objects.filter(todo_date = today)
    return render(request, 'home.html', {'contents': contents, 'posts': posts, 'today_list':today_list})


def new(request, mt20id):
  if request.method == 'POST': 
    form = TodoForm(request.POST)
    if form.is_valid():
      new_todo = form.save(commit=False)
      new_todo.created = timezone.now()
      new_todo.author = request.user
      new_todo.save()
      return redirect('todo:home')
    return redirect('todo:home')

def delete(request, id):
  if request.method == 'GET':
    delete_todo = Todo.objects.get(id = id)
    delete_todo.delete()
    return redirect('todo:home')


def edit(request, id):
    post = get_object_or_404(Todo, pk = id)
    if request.method == 'GET':
        todo_form = TodoForm(instance = post)
        return render(request, 'edit.html', {'edit_todo' : todo_form, 'todo' : post})
    else:
        todo_form = TodoForm(request.POST, instance = post)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False) 
            todo.save()
        return redirect('todo:home', todo.id)


def post_likes(request):
  if request.is_ajax():
    blog_id = request.GET.get('blog_id')
    post = Todo.objects.get(id=blog_id)

    user = request.user
    if post.like.filter(id = user.id).exists():
      post.like.remove(user)
      message = "좋아요 취소"
    else:
      post.like.add(user)
      message = "좋아요"
  context = {
    'like_count' : post.like.count(),
    'message' : message,
  }
  return HttpResponse(json.dumps(context), content_type="application/json")


@login_required
def mail(request):
  posts = Todo.objects.filter(author=request.user).order_by('created')
  posts = posts.filter(isCompleted=False)
  todo_list = '아직 완료되지 않은 일정이 ' + str(posts.count()) + '개 있습니다\n\n'
  for post in posts:
    todo_list += post.title + '\n'
  if request.method == 'GET':
      return render(request, 'mail.html', {'todo_list':todo_list})
  else:
      send_mail(
          subject = request.POST['subject'], # 제목
          message = request.POST['message'], # 내용
          from_email =  settings.EMAIL_HOST_USER, # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
          recipient_list = [request.POST['recipient_list']], # 받는 이메일 리스트
      )
      return redirect('/todo')