from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'ecommerce2.views.about', name='about'),
    url(r'^blank/$', 'ecommerce2.views.blank', name='blank'),
    url(r'^dash/$', 'ecommerce2.views.blank', name='dash'),
    url(r'^message/$', 'ecommerce2.views.blank', name='message'),
    url(r'^history/$', 'ecommerce2.views.blank', name='history'),
    url(r'^status/$', 'ecommerce2.views.blank', name='status'),
    url(r'^faq/$', 'ecommerce2.views.faq', name='faq'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')), 
    # Django JET URLS
    url(r'^jet/', include('jet.urls', 'jet')), 
    url(r'^item/', include('item.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
