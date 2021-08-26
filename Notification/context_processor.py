from .models import * 

def notification(request):
	if request.user.is_authenticated:
		return {'notifications': request.user.notifications.filter()}