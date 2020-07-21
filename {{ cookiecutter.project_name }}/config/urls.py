from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('', include('{{ cookiecutter.project_name }}.users.urls', namespace="user")),
]

if settings.DEBUG:
  import debug_toolbar

  urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
  ]

  