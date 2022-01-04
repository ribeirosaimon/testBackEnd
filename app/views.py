from django import forms
from django.forms import fields
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Place
from .modelForm import PlaceForm
from django.contrib import messages


class PlaceListView(LoginRequiredMixin, FormView):
    login_url = 'accounts/login/'
    redirect_field_name = ''
    template_name = "PlaceForm.html"
    form_class = PlaceForm
    success_url = reverse_lazy('PlaceForm')

    def get_context_data(self, *args, **kwargs):
        context = super(PlaceListView, self).get_context_data(**kwargs)
        context['objects'] = Place.objects.filter(usuario=self.request.user)  
        return context

    def form_valid(self,form,*args,**kwargs):
        myForm = form.save(commit=False)
        myForm.user = self.request.user
        myForm.save()
        messages.success(self.request, 'Saved Place')
        return super(PlaceListView, self).form_valid(form,*args,**kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request,"It's wrong")
        return super(PlaceListView, self).form_valid(form,*args,**kwargs)


class PlaceViewDelete(LoginRequiredMixin, DeleteView):
    model = Place
    template_name = "delete_place.html"
    context_object_name = "place"
    success_url = reverse_lazy('PlaceForm')

class PlaceViewupdate(LoginRequiredMixin, UpdateView):
    model = Place
    template_name = "update_place.html"
    context_object_name = "place"
    fields = ["name","lat","log","timestamp"]
    success_url = reverse_lazy('PlaceForm')