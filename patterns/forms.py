from django.forms.models import modelform_factory
from django.forms import inlineformset_factory
from patterns.models import Page, Author, Book, Friendship

PageForm = modelform_factory(Page)
PageFormTwo = modelform_factory(Page, fields=("meta_title", "meta_keywords"))


BookFormSet = inlineformset_factory(Author, Book, fields=('title',))
author = Author.objects.get(id=1)
formset = BookFormSet(instance=author)

FriendshipFormSet = inlineformset_factory(
    Author, Friendship, fk_name='from_friend',
    fields=('to_friend', 'length_in_months')
)

