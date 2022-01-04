from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('app.urls'))
]
