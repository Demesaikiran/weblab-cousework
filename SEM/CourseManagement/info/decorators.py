from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext, Template, Context


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None

			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)

			else:
				html = Template('{% load static %} <img src="{% static "info/images/forbidden.png" %}" width="100%" height="100%"/>')
				return HttpResponse(html.render(Context(request)))

		return wrapper_func

	return decorator



def admin_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None

		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'admin':
			return view_func(request, *args, **kwargs)

		elif group == 'Teacher' or group == 'student':
			html = Template('{% load static %} <img src="{% static "info/images/forbidden.png" %}" width="100%" height="100%"/>')
			return HttpResponse(html.render(Context(request)))


	return wrapper_func
