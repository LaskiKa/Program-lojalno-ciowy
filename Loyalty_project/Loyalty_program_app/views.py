from django.shortcuts import render
from Loyalty_program_app.models import Products
from django.views import View
from django.views.generic import CreateView, UpdateView


# Create your views here.
class Base(View):
    def get(self, request):
        products = Products.objects.all()
        return render(request,
                      'Loyalty_program_app/base.html',
                      {'products': products})


class UserMainSite(View):
    def get(self, request):
        return render(request,
                      "Loyalty_program_app/user-main-site.html")

class ProductAddView(CreateView):
    model = Products
    fields = ["name", "unit_price", "basic_points", "category"]
    success_url = "/base/" # do poprawki + zmiana tempaltki

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Products
    fields = ["name", "unit_price", "basic_points", "category"]
    success_url = "/base/"
    template_name_suffix = '_update_form'