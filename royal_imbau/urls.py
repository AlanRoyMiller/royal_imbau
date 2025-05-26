# mysite/urls.py

from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # language-switcher endpoint
    path('i18n/', include('django.conf.urls.i18n')),
]

# Wrap everything else in i18n_patterns.
# `prefix_default_language=False` will *not* prefix the default (Spanish) URLs with /es/.
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    prefix_default_language=False,
)

# static files (dev only)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
