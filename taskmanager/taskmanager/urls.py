from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#TODO указывам пути
urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('main/', include('main.urls')),
    path('', include('shop.urls', namespace='shop')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
