from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "active", "service": "backend"})
