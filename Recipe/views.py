from django.shortcuts import render, redirect
from django.views import generic

from .forms import RecipeForm, IngredientFormSet

from .models import Recipe

# Create your views here.
def index(request):
    return render(request, 'index.html')

class RecipeListView(generic.ListView):
    model = Recipe

class RecipeDetailView(generic.DetailView):
    model = Recipe
    

def create_recipe(request):
    if request.method == 'GET':
        form = RecipeForm()
        formset = IngredientFormSet()
        return render(request, 'create_recipe.html', {'form':form, 'formset':formset})
    elif request.method =="POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return redirect('/')
        else:
            return render(request, 'create_recipe.html', {'form': form})

    