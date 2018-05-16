from django.shortcuts import get_object_or_404, render

from django.views import generic

from .models import Team, Player

class Home(generic.TemplateView):

    template_name = 'spfl/home.html'

    def get(self, request, *args, **kwargs):

        players = Player.objects.all()

        context = {
            'players': players
        }


        return render(request, self.template_name, context)