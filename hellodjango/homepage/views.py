from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'index.html'

    # variables used in the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_statement'] = 'Nice to see you!'
        context['testing'] = 'Este es un texto en español traido desde get_context_data'
        context['suma'] = 40+40
        return context

    def say_bye(self):
        return 'Goodbye'