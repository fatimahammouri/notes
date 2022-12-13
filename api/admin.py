from django.contrib import admin

from .models import Note
"""to see the modelas that I've created in the Admin panel
I need to register them here."""
admin.site.register(Note)

