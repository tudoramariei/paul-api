from django.db import models
from django.contrib.auth.models import User
import eav

datatypes = (
    ("int", "int"),
    ("float", "float"),
    ("text", "text"),
    ("date", "date"),
    ("bool", "bool"),
    ("object", "object"),
    ("enum", "enum"),
)


class Database(models.Model):
    """
    Description: Model Description
    """

    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Table(models.Model):
    """
    Description: Model Description
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    database = models.ForeignKey("Database", on_delete=models.CASCADE)

    date_created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return self.name


class TableColumn(models.Model):
    """
    Description: Model Description
    """

    name = models.CharField(max_length=50)
    column_type = models.CharField(max_length=20, choices=datatypes)
    table = models.ForeignKey(
        "Table", on_delete=models.CASCADE, related_name="columns"
    )

    class Meta:
        pass

    def __str__(self):
        return "{} [{}]".format(self.name, self.column_type)


class Entry(models.Model):
    """
    Description: Model Description
    """

    table = models.ForeignKey(
        "Table", on_delete=models.CASCADE, related_name="entries"
    )
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.table.name


eav.register(Entry)