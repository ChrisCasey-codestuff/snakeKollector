from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Snake
from .forms import FeedingForm
from .models import Toy


#from .forms import FeedingForm

# Add the Cat class & list and view function below the imports

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def snakes(request):
  snakesList = Snake.objects.all()
  return render(request, 'snakes/snakeIndex.html',  { 'snakesList': snakesList })


#from .forms import FeedingForm
# define cotroller logic here

# each controller defined using a function

#cats = [ Cat('Finn', 'fold', 'big grey fluff', 12), Cat('LuckyDuck', 'mangey', 'OG', 11)]

def snake_detail(request, snake_id):

    snake = Snake.objects.get(id = snake_id)
    toys = Toy.objects.exclude(id__in = snake.toys.all().values_list('id'))
    feeding_form = FeedingForm
    return render(request, 'snakes/snakeDetail.html', {'snake': snake, 'feeding_form': feeding_form, 'toys': toys})

    #create new feeding inst
    #validate user form input
    # if can asoc relate cat
    # return a redirect response to the client
def add_feeding (request, snake_id):
   form = FeedingForm(request.POST)
  # validate the form
   if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.snake_id = snake_id
    new_feeding.save()
    return redirect('snake_detail', snake_id=snake_id)



class SnakeCreate (CreateView):
    model = Snake
    ## fields = ('name', 'breed', 'description', 'age')
    fields = '__all__'

class SnakeUpdate (UpdateView):
    model = Snake
    fields = ('name', 'description')


class SnakeDelete (DeleteView):
    model = Snake
    ## fields = ('name', 'breed', 'description', 'age')
    success_url = '/snakes/'

def toys(request):
  toyList = Toy.objects.all()
  return render(request, 'toys/toyIndex.html',  { 'toyList': toyList })


def toy_detail(request, toy_id):
    toy = Toy.objects.get(id = toy_id)
    return render(request, 'toys/toyDetail.html', {'toy': toy })


class ToyCreate (CreateView):
   model = Toy
   fields = '__all__'

class ToyUpdate (UpdateView):
   model = Toy
   fields = ('name', 'description')

class ToyDelete (DeleteView):
   model = Toy
   success_url = '/toys/'


def assoc_toy (request, snake_id, toy_id):
    #find the cat
    snake = Snake.objects.get(id=snake_id)
    snake.toys.add(toy_id)
    return redirect('snake_detail', snake_id=snake_id)
    #associate the toy
    #redirect to detail


def remove_toy (request, snake_id, toy_id):
    #find the cat
    snake = Snake.objects.get(id=snake_id)
    snake.toys.remove(toy_id)
    return redirect('snake_detail', snake_id=snake_id)
    #associate the toy
    #redirect to detail




