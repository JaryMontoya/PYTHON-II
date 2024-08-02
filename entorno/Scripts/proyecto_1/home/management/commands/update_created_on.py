# home/management/commands/update_created_on.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import Contact

class Command(BaseCommand):
    help = 'Actualiza el campo creado_en en Contact'

    def handle(self, *args, **kwargs):
        contacts = Contact.objects.filter(creado_en__isnull=True)
        for contact in contacts:
            contact.creado_en = timezone.now()
            contact.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated created_on field'))
