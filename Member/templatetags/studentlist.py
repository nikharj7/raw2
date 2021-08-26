from django import template
from Member.models import Add_College_and_University
from Student.models import New_Student
register = template.Library()

@register.inclusion_tag('home/student_lists.html', takes_context=True)

def student_lists(context):
	request_user = context['request'].user
	lists1 = New_Student.objects.filter(user=request_user).order_by('-id')
	return {'lists1':lists1}