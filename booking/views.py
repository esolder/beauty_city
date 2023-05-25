from django.shortcuts import render
from django.views.generic import TemplateView




class AppointmentView(TemplateView):
    template_name = 'service.html'

    def get(self, request):
        return render(request, self.template_name)


class ServiceFinallyView(TemplateView):
    template_name = 'serviceFinally.html'

    def get(self, request):
        return render(request, self.template_name)
