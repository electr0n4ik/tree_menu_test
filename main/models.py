from django.db import models

nullability = {'blank': True, 'null': True}


class TreeMenuCategory(models.Model):
    """
    Model representing a category for a tree menu.

    Attributes:
        name (str): The name of the category.
        verbose_name (str): A more descriptive name for the category.

    Methods:
        __str__(): Returns a string representation of the category.
    """
    name = models.CharField(
        max_length=255,
        verbose_name='Name')
    verbose_name = models.CharField(
        max_length=255,
        verbose_name='Verbose name')

    def __str__(self):
        return self.verbose_name

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'


class TreeMenu(models.Model):
    """
    Model representing an item in a tree menu.

    Attributes:
        name (str): The name of the menu item.
        category (TreeMenuCategory):
            The category to which the menu item belongs.
        path (str): The path associated with the menu item.
        parent (TreeMenu, optional): The parent menu item. Defaults to None.

    Methods:
        __str__(): Returns a string representation of the menu item.
    """
    name = models.CharField(max_length=255)

    category = models.ForeignKey(
        TreeMenuCategory,
        verbose_name='category',
        on_delete=models.CASCADE,
    )
    path = models.CharField(max_length=1020)

    parent = models.ForeignKey(
        'self',
        verbose_name='parent',
        on_delete=models.SET_DEFAULT,
        default=None,
        **nullability
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
