from django.test import TestCase
from django.contrib.auth.models import User
from cloudbookapp.models import Note
# Create your tests here.
class NoteModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
    def test_note_creation(self):
        # Create a note
        note = Note.objects.create(
            user=self.user,
            title='Test Note',
            content='This is a test note'
        )
        # Retrieve the note from the database
        saved_note = Note.objects.get(id=note.id)
        # Assert that the retrieved note is the same as the created note
        self.assertEqual(saved_note.title, 'Test Note')
        self.assertEqual(saved_note.content, 'This is a test note')
        self.assertEqual(saved_note.user, self.user)
        # Assert the string representation of the note
        self.assertEqual(str(note), 'Test Note')
        # Assert the created_at and updated_at fields are set
        self.assertIsNotNone(saved_note.created_at)
        self.assertIsNotNone(saved_note.updated_at)
