from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from patterns.models import Author, Book
# from patterns import *


def index(request):
    return render_to_response('index.html')


def manage_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book, fields=('title',))
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(author.get_absolute_url())
    else:
        formset = BookInlineFormSet(instance=author)
    # return render_to_response('manage_books.html', {'formset': formset})
    return render_to_response(template_name='manage_books.html', context=None,
                       context_instance=_context_instance_undefined,
                       content_type=None, status=None, dirs=_dirs_undefined,
                       dictionary=_dictionary_undefined, using=None)
