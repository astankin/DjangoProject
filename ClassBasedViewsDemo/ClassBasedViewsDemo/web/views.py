from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

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
        context['name'] = 'Atanas'  # Can be something retrieved from the database CarModel.objects.get(pk=pk)
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
# Mixin for disabled fields
class DisableFieldFormMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for name, field in form.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attrs['placeholder'] = f'Enter {name}'
        return form


class CarCreateView(CreateView):
    template_name = 'create-car.html'
    model = CarModel
    # fields = '__all__' # 1. If we want to use standard form

    form_class = CarCreateForm  # 2.If we want to use special form with fields and widgets set in the form

    # 3. Change the automatic form. Same as the above.
    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     for name, field in form.fields.items():
    #         field.widget.attrs['disabled'] = 'disabled'
    #         field.widget.attrs['readonly'] = 'readonly'
    #         field.widget.attrs['placeholder'] = f'Enter {name}'
    #     return form
    # success_url = '/'  # static url - if we want to redirect to index page
    success_url = reverse_lazy('dashboard')

    # Dinamic
    # def get_success_url(self):
    #     create_object = self.get_object
    #     return reverse('details-car', kwargs={
    #         'pk': create_object.pk
    #     })


class CarUpdateView(UpdateView):
    template_name = 'update-car.html'
    model = CarModel
    fields = '__all__'


class CarsListView(ListView):
    context_object_name = 'cars'
    model = CarModel
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = 'Atanas'
        return context

    ordering = ['model']


class CarDetailsView(DetailView):
    context_object_name = 'car'
    model = CarModel
    template_name = 'details-car.html'


class DeleteCarView(DisableFieldFormMixin, DeleteView):
    context_object_name = 'car'
    model = CarModel
    template_name = 'delete-car.html'
    success_url = reverse_lazy('dashboard')
    # form_class = modelform_factory(
    #     CarModel,
    #     fields=('model', 'type', 'year_of_manufacturing')
    # )
    # disabled_fields = ['model', 'type', 'year_of_manufacturing']


    # def get_form_kwargs(self):
    #     instance = self.get_object()
    #     form_kwargs = super().get_form_kwargs()
    #
    #     form_kwargs.update(instance=instance)
    #     return form_kwargs
