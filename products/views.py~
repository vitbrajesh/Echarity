from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
# Custom Imports
from .forms import VariationInventoryForm
from .models import Product, Variation
# Create your views here.
#################################################################################
#Product list view

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()


    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        # print context
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q")
        return context


#Basic search function
#using q import from django.db.models import Q
# 
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
                )
            try:
                qs2 = self.model.objects.filter(
                Q(price=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs

##################################################################################
#Variation List view
class VariationListView(ListView):
    model = Variation
    queryset = Variation.objects.all()


    # def get_context_data(self, *args, **kwargs):
    #     context = super(VariationListView, self).get_context_data(*args, **kwargs)
    #     # print context
    #     context["now"] = timezone.now()
    #     context["query"] = self.request.GET.get("q")
    #     return context

    def get_queryset(self, *args, **kwargs):
        # qs = super(VariationListView, self).get_queryset(*args, **kwargs)
        # query = self.request.GET.get("q")
        product_pk= self.kwargs.get("pk")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            queryset = Variation.objects.filter(product=product)
        return queryset


    def post (self, request, *args, **kwargs):
        raise Http404


##################################################################################
#Product Detail view
class ProductDetailView(DetailView):
    model = Product
    # template_name = "product.html"

    def product_detail_view_func(request, id):
        # product_instance = Product.objects.get(id=id)
        product_instance =  get_object_or_404(Product, id=id)
        try:
            product_instance = Product.object.get(id=id)
        except Product.DoesNotExist:
            raise Http404
        except:
            raise Http404

        template = "products/product_detail.html"
        context = {
        "object": product_instance
        }

        return render(request, template, context)

########################################################################################

