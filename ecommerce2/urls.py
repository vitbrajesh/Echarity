from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from dashing.utils import router
from registration.backends.default.views import RegistrationView


urlpatterns = [
    # Examples:

    url(r'^messages/', include('django_messages.urls')),
    #url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'ecommerce2.views.about', name='about'),
    url(r'^blank/$', 'ecommerce2.views.blank', name='blank'),
  
    url(r'^status/$', 'ecommerce2.views.blank', name='status'),
    url(r'^faq/$', 'ecommerce2.views.faq', name='faq'),
    url(r'^policy/$', 'ecommerce2.views.policy', name='policy'),
    url(r'^term/$', 'ecommerce2.views.term', name='term'),
    url(r'^gallery/$', 'ecommerce2.views.gallery', name='gallery'),
    url(r'^dashboard/$', 'dashboard.views.dashboard', name='dashboard'),
    url(r'^profile/$', 'dashboard.views.profile', name='profile'),
    url(r'^history/$', 'ecommerce2.views.blank', name='history'),
    #url(r'^dashboard/', include(router.urls)),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'products.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^register/$', 'driver.views.DriverRegistration'),
    url(r'^login/$', 'driver.views.LoginRequest'),
    url(r'^logout/$', 'driver.views.LogoutRequest'), 
    # Django JET URLS
    url(r'^jet/', include('jet.urls', 'jet')), 
    #url(r'^items/', include('items.urls')),
    url(r'^item/', include('item.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
