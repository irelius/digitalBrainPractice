from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def main(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "index.html")

def api_test(request):
    tasks = [{'id': 1, 'title': 'Task 1'}, {'id': 2, 'title': 'Task 2'}]
    return JsonResponse({'tasks': tasks})

def api_store_tasks(request):
    if request.method == "POST":
        data = json.loads(request.body)
        task = data.get("task")

        if task:
            return JsonResponse({'message': 'Task created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
