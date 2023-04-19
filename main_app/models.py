from django.db import models

from django.urls import reverse
# Create your models here.


# A tuple of 2-tuples
MEALS = (
    ('M', 'Mouse'),
    ('B', 'Bird'),
    ('S', 'Strawberry')
)
# new code above


class Toy (models.Model):
    name = models.CharField( max_length=50 )
    description = models.TextField( max_length=250 )
    def __str__(self):
        return (f"This is a {self.name}, Description: {self.description}")
    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'toy_id': self.id})

class Snake(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    toys = models.ManyToManyField(Toy, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('snake_detail', kwargs={'snake_id': self.id})



# Add new Feeding model below Cat model
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
    )
    snek = models.ForeignKey(Snake, on_delete=models.CASCADE)
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

