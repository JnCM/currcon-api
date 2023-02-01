from django.shortcuts import render

def index(request):
    currencies = ["BRL", "BTC", "ETH", "EUR", "USD"]
    context = {"currencies": currencies}
    return render(request, "website/index.html", context)
