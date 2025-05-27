from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteTests(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'Note content here.',
        })
        self.assertEqual(response.status_code, 302)  # should redirect
        self.assertEqual(Note.objects.count(), 2)

    def test_note_update_view(self):
        response = self.client.post(reverse('note_update', args=[self.note.pk]), {
            'title': 'Updated Title',
            'content': 'Updated content.',
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')

    def test_note_delete_view(self):
        response = self.client.post(reverse('note_delete', args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)

    def test_invalid_note_create(self):
        response = self.client.post(reverse('note_create'), {
            'title': '',  # invalid: title required
            'content': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')

