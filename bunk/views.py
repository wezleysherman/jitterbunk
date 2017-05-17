# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.template import loader
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from .models import Bunk, User
from .forms import BunkForm

# Create your views here.
class MainFeed(generic.ListView):
    template_name = 'bunk/main.html'
    context_object_name = 'bunk_list'
    def get_queryset(self):
        return Bunk.objects.filter(time__lte = timezone.now()).order_by('-time')[:20]

class UserFeed(generic.ListView):
    template_name = 'bunk/user.html'
    context_object_name = 'bunk_list'
    def get_context_data(self, **kwargs):
        context = super(UserFeed, self).get_context_data(**kwargs)
        context['feed_user'] = User.objects.get(pk=self.kwargs['pk'])
        return context
    # Filtering mult. objects: http://stackoverflow.com/questions/739776/django-filters-or
    # Credit: Alex Koshelev
    def get_queryset(self):
        return Bunk.objects.filter(Q(from_user__id=self.kwargs['pk']) | Q(to_user__id=self.kwargs['pk'])).order_by('-time')[:20]

class BunkView(generic.FormView):
    template_name = 'bunk/bunkview.html'
    form_class = BunkForm
    success_url = '../'
    def form_valid(self, form):
        user_name = form.cleaned_data['bunk_name']
        new_bunk = Bunk()
        bunk_user = get_object_or_404(User, username=user_name)
        new_bunk.from_user = get_object_or_404(User, username='wezley')
        new_bunk.to_user = bunk_user
        new_bunk.time = datetime.datetime.now()
        new_bunk.save()
        return super(BunkView, self).form_valid(form)
