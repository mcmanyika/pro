# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from events.admin import *

# Create your views here.

def calendar(request):

	context = {
		"calendar" : calendar,
	}
	template = "change_list.html"
	return render(request, template, context)
