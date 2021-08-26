from django import template
from Email.models import Student_Activity_Email

register = template.Library()

@register.inclusion_tag('home/AOI.html', takes_context=True)

def Show_AOI(context):
	request_user = context['request'].user
	AOIS = Student_Activity_Email.objects.filter(user=request_user).order_by('-id')
	return {'AOIS':AOIS}