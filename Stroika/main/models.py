from django.db import models

class Product_categories(models.Model):
    name = models.CharField('Категории', max_length=20)
    images = models.ImageField('Изображение категории', upload_to='images/')
    url = models.SlugField(max_length=30)

    def __str__(self):
        return self.name
    

class Material(models.Model):
    title = models.CharField('Название материала', max_length=40)
    image = models.ImageField('Изображение', upload_to='image_Material/')
    quantity = models.CharField('Товар измеряется в:', max_length=10)
    code = models.CharField('Артикул', max_length=10)
    price = models.PositiveSmallIntegerField('Цена', default=0)
    category = models.ForeignKey(Product_categories, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title
    
