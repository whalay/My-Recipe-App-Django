from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.RecipeListView.as_view(), name="recipes"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="recipe-detail"),
    path('create/', views.create_recipe, name='create_recipe')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
    
