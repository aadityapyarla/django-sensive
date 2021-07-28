from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
import debug_toolbar
urlpatterns = [
    # ! Template Rendering URL Routes
    # ? These URL's render the templates for further user interactions

    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls, name="admin"),

    # ! Installed App's URL Routes
    # ? These URL's render the installed apps

    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
