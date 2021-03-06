from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'blog', include('blog.urls', namespace='blog')),
	url(r'cursos', include('courses.urls', namespace='courses')),
	url(r'seleccion', include('seleccion.urls', namespace='seleccion')),
	url(r'acciones', include('acciones.urls', namespace='acciones')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)