from django import template
from Notification.models import Notification

register = template.Library()

@register.inclusion_tag('home/show_notification.html', takes_context=True)

def show_notifications(context):
	request_user = context['request'].user
	notifications = Notification.objects.filter(user=request_user).exclude(viewd=True).order_by('-id')
	return {'notifications':notifications}