from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ServisniUkonForm, VehicleForm
from .models import Vehicle, ServisniUkon


class  VozidlaListView(ListView):
    model = Vehicle
    template_name = 'seznam_vozidel.html'
    context_object_name = 'vozidla'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()  # Dnešní datum
        for vozidlo in context["vozidla"]:
            if vozidlo.stk:
                vozidlo.dni_do_stk = (vozidlo.stk - today).days
            else:
                vozidlo.dni_do_stk = None  # Když není datum STK
        return context

class VozidloDetailView(DetailView):
    model = Vehicle
    template_name = 'detail_vozidla.html'
    context_object_name = 'vozidlo'


class AddUkon(CreateView):
    model = ServisniUkon
    form_class = ServisniUkonForm  # Použití vlastního formuláře
    template_name = 'add_ukon.html'

    def get_success_url(self):
        return reverse_lazy('detail_vozidla', kwargs={'pk': self.object.vozidlo.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vozidlo'] = Vehicle.objects.get(pk=self.kwargs['pk'])  # Přidání vozidla do kontextu
        return context

    def form_valid(self, form):
        vozidlo = Vehicle.objects.get(pk=self.kwargs['pk'])
        form.instance.vozidlo = vozidlo
        return super().form_valid(form)

class EditVozidlo (UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'edit_vozidlo.html'

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vozidlo"] = self.object
        return context

