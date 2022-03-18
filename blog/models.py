from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return f'{self.id}-{self.title}'


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images_blog")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,
                             related_name='images', null=True, blank=True)

    def __str__(self):
        return f'{self.image.url}'


class Hashtag(models.Model):
    title = models.CharField(max_length=50)
    hashtag = models.ManyToManyField(Blog)

    def __str__(self):
        return self.title

