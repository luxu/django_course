from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.urls import reverse

from .models import Choice, Question


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions
        (not including those set to be published in the future).
        """
        return Question.objects\
            .filter(pub_date__lte=timezone.now())\
            .order_by('-pub_date')[:5]


class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        )


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Mostra novamente o formulário de votação das perguntas.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Sempre retorna um HttpResponseRedirect depois de lidar com sucesso
        # com dados via POST. Isso impede que os dados sejam postados duas vezes se
        # o usuário clicar no botão voltar.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
