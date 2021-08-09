from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField('书名', max_length=50, unique=True)
    pub = models.CharField('出版社', max_length=100, null=False, default='')
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=7, decimal_places=2, null=True)

    class Meta:
         db_table = 'book'


class Author(models.Model):
    name = models.CharField(max_length=11, null=False)
    age = models.IntegerField(default=1)
    email = models.EmailField(null=True)

    class Meta:
        db_table = 'author'
