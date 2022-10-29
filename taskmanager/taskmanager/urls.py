from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#TODO указывам пути
urlpatterns = [
    path('cart/', include('cart.urls', namespace='cart')),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('', include('shop.urls', namespace='shop')),


    #path('user/', include('users.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
