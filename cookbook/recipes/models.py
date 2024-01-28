from django.db import models


NAME_LENGTH = 255
STR_LENGTH = 30


class Product(models.Model):
    """Модель продуктов."""

    name = models.CharField(max_length=NAME_LENGTH)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name[:STR_LENGTH]


class Recipe(models.Model):
    """Модель рецептов."""

    name = models.CharField(max_length=NAME_LENGTH)
    products = models.ManyToManyField(
        Product,
        through='RecipeProduct',
        related_name='recipes',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name[:STR_LENGTH]


class RecipeProduct(models.Model):
    """Связующая модель рецептов и продуктов."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        ordering = ['recipe', 'product']
        verbose_name = 'Рецепты и продукты'
        verbose_name_plural = 'Рецепты и продукты'

    def __str__(self):
        return f'{self.recipe} - {self.product} {self.amount}'
