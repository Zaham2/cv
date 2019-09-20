"""cv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys

sys.path.insert(0, 'D:\Programming\Dev\secondPortf\src\jobs')

from django.contrib import admin
from django.urls import path, include

# added imports
from django.conf import settings
from django.conf.urls.static import static
import jobs.views  # IDE Gives error but server runs and page loads!!

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', jobs.views.home, name='home'),
                  # path('blog/', include('blog.urls')), intentionally removed
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Adding this static line makes it so I can see media files in the admin view... SK !!?
