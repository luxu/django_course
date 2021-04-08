from django.views.generic import ListView


class Home(ListView):
    template_name = 'core/home.html'

    def get_queryset(self):
        ...
