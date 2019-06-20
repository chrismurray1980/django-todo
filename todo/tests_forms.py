from django.test import TestCase
from django.shortcuts import get_object_or_404
from .forms import ItemForm
from .models import Item

# Create your tests here.
class TestToDoItemForm(TestCase):
    
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': "Create tests"})
        self.assertTrue(form.is_valid())
        
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        
    def test_post_create_an_item(self):
        response = self.client.post("/add", {'name':'Create a test'})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
        
    def test_post_edit_an_item(self):
        item = Item(name='Create a test')
        item.save()
        id=item.id
        response = self.client.post("/edit/{0}".format(id), {'name':'A different test'})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.name, 'A different test')
        
    def test_toggle_status(self):
        item = Item(name='Create a test')
        item.save()
        id=item.id
        response = self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)