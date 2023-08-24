from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from app.models import Task, User
import json

# Create your views here.
def main(request):
    return render(request, "index.html")

def demo_user_login(request):
    user = authenticate(username='demo_user', password='demo-password')
    if user is not None:
        login(request, user)
        return HttpResponse("Demo user logged in successfully!")
    else:
        return HttpResponse("Demo user authentication failed.")


def api_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            csrf_token = get_token(request)  # Get the CSRF token
            response_data = {
                'message': 'Logged in successfully',
                'csrf_token': csrf_token
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid login credentials'}, status=400)


def api_get_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.filter(user="1")  # Retrieve all tasks from the database
        task_list = [{'id': task.id, 'task': task.task} for task in tasks]
        return JsonResponse({'tasks': task_list})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def api_create_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        task_text = data.get("task")

        if task_text:
            user = User.objects.get(id=1)
            task = Task.objects.create(task=task_text, user=user)
            return JsonResponse({'message': 'Task created successfully', 'id': task.id})
        else:
            return JsonResponse({'error': 'Missing task text'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def api_delete_task(request, task_id):
    if request.method == "DELETE":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
