from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('projects', views.ProjectViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns=[
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<username>/profile', views.user_profile, name='user_profile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit_profile'),
    path('project/<project>', views.project, name='project'),
    path('search/', views.search_project, name='search'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
