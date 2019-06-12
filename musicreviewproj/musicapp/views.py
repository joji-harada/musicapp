from django.shortcuts import render, get_object_or_404
from .models import MusicType, Product, Review
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'musicapp/index.html')

def gettypes(request):
    type_list=MusicType.objects.all()
    return render(request, 'musicapp/types.html', {'type_list' : type_list})

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'musicapp/products.html', {'products_list': products_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    discount=prod.memberdiscount
    reviews=Review.objects.filter(product=id).count()
    context={
        'prod' : prod,
        'discount' : discount,
        'reviews' : reviews,
    }
    return render(request, 'musicapp/productdetails.html', context=context)

# form view
@login_required
def newproduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'musicapp/newproduct.html', {'form': form})

# login / logout views

def loginmessage(request):
    return render(request, 'musicapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'musicapp/logoutmessage.html')