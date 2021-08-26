from django import template
from Member.models import Add_College_and_University
register = template.Library()

@register.inclusion_tag('home/show_list.html', takes_context=True)

def show_lists(context):
	request_user = context['request'].user
	lists = Add_College_and_University.objects.filter(user=request_user).order_by('-id')
	return {'lists':lists}