from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView, TemplateView
from patterns.forms import RegistrationForm
from patterns.models import Author, Book

#
# class RegFormView(FormView):
#     template_name = "index_material.html"
#     form_class = RegistrationForm


class PolymerView(TemplateView):
    template_name = "index_polymer.html"


# class PolymerViewHelper(TemplateView):
#     template_name = "polymer/proto-element.html"

# def index(request):
#     form = RegistrationForm()
#     return render_to_response(template_name='index_material.html', context=locals(),
#                               context_instance=RequestContext(request))

#
# def manage_books(request, author_id):
#     author = Author.objects.get(pk=author_id)
#     BookInlineFormSet = inlineformset_factory(Author, Book, fields=('title',))
#     if request.method == "POST":
#         formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
#         if formset.is_valid():
#             formset.save()
#             return HttpResponseRedirect(author.get_absolute_url())
#     else:
#         formset = BookInlineFormSet(instance=author)
#     return render_to_response(
#         template_name='manage_books.html', context={'formset': formset}, context_instance=RequestContext(request)
#     )
#

