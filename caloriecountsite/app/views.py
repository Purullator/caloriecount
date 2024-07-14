from django.shortcuts import render
from .models import Food, Consume

# Create your views here.

def index(request):

    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed) #getting the actual food object
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'app/index.html', {'foods':foods, 'consumed_food':consumed_food})