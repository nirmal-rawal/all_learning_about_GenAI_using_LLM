from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .llm_service import chat_service
import json
from django.shortcuts import render
@csrf_exempt


def chat_view(request):
    return render(request, 'chatbot/index.html')
@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message', '')
            
            if not user_input:
                return JsonResponse({'error': 'Empty message'}, status=400)
                
            response = chat_service.get_response(user_input)
            
            return JsonResponse({
                'response': response,
                'status': 'success'
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    # Return a more helpful message for GET requests
    return JsonResponse({
        'error': 'Method not allowed',
        'message': 'Please use POST request with JSON payload containing your message',
        'example': {
            'message': 'Your question here'
        }
    }, status=405)