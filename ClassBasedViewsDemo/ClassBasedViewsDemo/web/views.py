from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from ClassBasedViewsDemo.web.forms import CarCreateForm
from ClassBasedViewsDemo.web.models import CarModel


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    # extra_context = {
    #     'name': 'Atanas'
    # }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Atanas'  # Can be something retrived from the database
        context['age'] = '40'
        return context


# def create_car(request):
#     if request.method == 'POST':
#         form = CarCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CarCreateForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'create-car.html', context)

class CarCreateView(CreateView):
    template_name = 'create-car.html'
    model = CarModel
    # fields = '__all__' # If we want to use standard form

    form_class = CarCreateForm  # If we want to use special form with fields and widgets set in the form

    # Change the automatic form. Same as the above.
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     for name, field in form.fields.items():
    #         field.widget.attrs['placeholder'] = f'Enter {name}'
    #     return form
    success_url = '/'  # static url - if we want to redirect to index page

    # Dinamic
    def get_success_url(self):
        create_object = self.get_object
        return reverse('details-car', kwargs={
            'pk': create_object.pk
        })


class CarsListView(ListView):
    context_object_name = 'cars'
    model = CarModel
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = 'Atanas'
        return context


class CarDetailsView(DetailView):
    context_object_name = 'car'
    model = CarModel
    template_name = 'details-car.html'
