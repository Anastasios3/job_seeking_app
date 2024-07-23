from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application

class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'applications/application_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)