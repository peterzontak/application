from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('manager/', admin.site.urls, name='admin'),
    path('', include("app.urls"), name="app"),  # Ensure app.urls is correctly defined
    path('notes/', include("notes.urls", namespace="notes")),  # Added trailing slash
    # path('api/', include("crud.urls")),  # Uncomment if needed
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
]


# 'Python': {
#       'Django': ['deploy.md', 'migrations.md', 'new-project.md', 'postgre.md'],
#       'pip.md': [],
#       'venv.md': []
#   }

# 'Python': [
#       {'Django': ['deploy.md', 'migrations.md', 'new-project.md', 'postgre.md']},
#       'pip.md',
#       'venv.md'
# ]
  