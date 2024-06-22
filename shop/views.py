from django.shortcuts import render
from .models import Prod, ProdCategory, Staff, Contacts, News

def index(request):
    products = Prod.objects.filter(is_visible=True).order_by('sort')
    categories = ProdCategory.objects.filter(is_visible=True).order_by('sort')
    staff = Staff.objects.filter(is_visible=True)
    contacts = Contacts.objects.all()
    news = News.objects.all().order_by('-created_at')
    return render(request, 'shop/index.html', {
        'products': products,
        'categories': categories,
        'staff': staff,
        'contacts': contacts,
        'news': news
    })
