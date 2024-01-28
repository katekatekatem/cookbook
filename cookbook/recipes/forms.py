from django import forms


class AddProductToRecipeForm(forms.Form):
    recipe_id = forms.IntegerField(label='ID рецепта', min_value=1)
    product_id = forms.IntegerField(label='ID продукта', min_value=1)
    amount = forms.IntegerField(label='Вес продукта в граммах', min_value=1)


class CookRecipeForm(forms.Form):
    recipe_id = forms.IntegerField(label='ID рецепта', min_value=1)


class ShowRecipesWithoutProductForm(forms.Form):
    product_id = forms.IntegerField(label='ID продукта', min_value=1)
