from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views import generic

from .metodosimplex import SimplexPrimal, SimplexDual
# Create your views here.

class Index(generic.TemplateView):
    template_name = 'core/index.html'

index = Index.as_view()

class GetSimplesView(generic.TemplateView):
    template_name = 'core/enter_simplex.html'

    def get_context_data(self, **kwargs):
        context = super(GetSimplesView, self).get_context_data(**kwargs)

        insert_var = []
        for i in range(int(self.request.GET.get('var'))):
            insert_var.append(i)

        lines = []
        for i in range(int(self.request.GET.get('sa'))):
            lines.append(i)

        context['var'] = self.request.GET.get('var')
        context['insert_vars'] = insert_var
        context['number_var'] = 2*(len(insert_var))
        context['sa'] = self.request.GET.get('sa')
        context['lines'] = lines


        return context

getsimplex = GetSimplesView.as_view()

class ResolvedSimplexView(generic.TemplateView):
    template_name = 'core/tmp/simplex.html'

    def get_context_data(self, **kwargs):
        context = super(ResolvedSimplexView, self).get_context_data(**kwargs)

        # A = [[1, 2, 1, 0, 0],
        #      [2,-1, 0, 1, 0],
        #      [5, 3, 0, 0, 1]]
        # b = [6, 4, 15]
        # c = [-5, -4]

        c = []
        for resp in range(int(self.request.GET.get('var'))):
            c.append(self.request.GET.get('var{}'.format(resp)))
        A = []

        for resp in range(int(self.request.GET.get('sa'))):
                line = []
                for l in range(int(self.request.GET.get('var'))):
                    line.append(int(self.request.GET.get('sa_{}_{}'.format(resp,l))))
                A.append(line)

        b = []
        for resp in range(int(self.request.GET.get('sa'))):
            b.append(self.request.GET.get('b{}'.format(resp)))

        print(b)

        prob = SimplexPrimal(A,b,c, output='html=simplex.html,minimal')
        prob.resolver()

        return context

resolved = ResolvedSimplexView.as_view()
