from django.shortcuts import render, redirect
from .forms import furnitureForm

# Create your views here.
def homepage(request):
	return render(request, 'goodasnew/homepage.html', {})

def sale(request):
  return render(request, 'goodasnew/sale.html', {})

def purchase(request):

  def customer_to_id(name):
    return 0

  if request.method == "POST":
    form = furnitureForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.purchase_customer_id = customer_to_id(post.purchase_customer_id)
      # Need to get furniture id
      post.save()
      return redirect('')
  else:
    form = furnitureForm()
  return render(request, 'goodasnew/purchase.html', {'form':form})
