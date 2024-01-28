from django.shortcuts import render

from .forms import (
    AddProductToRecipeForm, CookRecipeForm, ShowRecipesWithoutProductForm
)
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request):
    error_message = ''
    success_message = ''

    if request.method == 'POST':
        form = AddProductToRecipeForm(request.POST)
        if form.is_valid():
            recipe_id = form.cleaned_data['recipe_id']
            product_id = form.cleaned_data['product_id']
            amount = form.cleaned_data['amount']

            try:
                recipe = Recipe.objects.get(id=recipe_id)
                product = Product.objects.get(id=product_id)
                recipe_product, created = RecipeProduct.objects.get_or_create(
                    recipe=recipe, product=product, defaults={'amount': amount}
                )
                if not created:
                    recipe_product.amount = amount
                    recipe_product.save()
                success_message = 'Продукт успешно добавлен к рецепту!'
            except (Recipe.DoesNotExist, Product.DoesNotExist):
                error_message = ('Рецепт и/или продукт с указанным ID '
                                 'не существует.')
        else:
            error_message = 'Неверные данные формы.'
    else:
        form = AddProductToRecipeForm()

    return render(request, 'add_product_to_recipe.html', {
        'form': form,
        'error_message': error_message,
        'success_message': success_message
    })


def cook_recipe(request):
    error_message = ''
    success_message = ''

    if request.method == 'POST':
        form = CookRecipeForm(request.POST)
        if form.is_valid():
            recipe_id = form.cleaned_data['recipe_id']
            try:
                recipe = Recipe.objects.get(id=recipe_id)
                for product in recipe.products.all():
                    product.count += 1
                    product.save()
                success_message = 'Блюдо успешно приготовлено!'
            except Recipe.DoesNotExist:
                error_message = 'Рецепт с указанным ID не существует.'
        else:
            error_message = 'Неверные данные формы.'
    else:
        form = CookRecipeForm()

    return render(request, 'cook_recipe.html', {
        'form': form,
        'error_message': error_message,
        'success_message': success_message
    })


def show_recipes_without_product(request):
    error_message = ''
    recipes = []

    if request.method == 'POST':
        form = ShowRecipesWithoutProductForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            try:
                product = Product.objects.get(id=product_id)
                recipes_with_product_less_10 = Recipe.objects.filter(
                    recipeproduct__amount__lt=10,
                    recipeproduct__product_id=product_id
                )
                recipes_without_product = Recipe.objects.exclude(
                    products=product
                )
                recipes = recipes_with_product_less_10.union(
                    recipes_without_product
                ).order_by('id')
            except Product.DoesNotExist:
                error_message = 'Продукт с указанным ID не существует.'
        else:
            error_message = 'Неверные данные формы.'
    else:
        form = ShowRecipesWithoutProductForm()

    return render(request, 'recipes_without_product.html', {
        'form': form,
        'recipes': recipes,
        'error_message': error_message
    })
