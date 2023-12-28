# Models.py
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

# Views.py
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Payment processing (using Stripe as an example)
stripe.api_key = settings.STRIPE_SECRET_KEY
charge = stripe.Charge.create(
    amount=int(total_price * 100),
    currency='usd',
    description='Order #1234',
    source=request.POST['stripeToken']
)
