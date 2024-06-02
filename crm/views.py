from django.core.paginator import Paginator
from django.shortcuts import render
from crm.models import AppUser
import django_filters

from silk.profiling.profiler import silk_profile

class AppUserFilter(django_filters.FilterSet):
    class Meta:
        model = AppUser
        fields = '__all__'
    
    @classmethod
    def get_fields(cls):
        fields = super().get_fields()
        for field_name in fields.copy():
            lookup_list = cls.Meta.model._meta.get_field(field_name).get_lookups().keys()
            fields[field_name] = lookup_list
        return fields


@silk_profile()
def list_appusers(request):
    f = AppUserFilter(request.GET, AppUser.objects.select_related("address").prefetch_related("customerrelationship_set").all())

    qs = f.qs.order_by(request.GET.get("order_by", "first_name"))

    per_page = request.GET.get("per_page", 25)
    paginator = Paginator(qs, per_page)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'appusers.html', {'page_obj': page_obj})
