"""Categories Model."""

# Django
from django.db import models


# Utilities
from myhandycrafts.utils.models import MyHandycraftsModel


class Category(MyHandycraftsModel):
    """ Category model.

    This model represent the category of craft
    that make the craftsman.
    """

    name=models.CharField(
        'Category name',
        max_length=128,
        blank=False,
    )

    description=models.TextField(max_length=512,blank=True)

    def __str__(self):
        """ Return category name"""
        return self.name




