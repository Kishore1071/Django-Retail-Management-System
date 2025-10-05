from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# @login_required(login_url='/')
def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'bill_list.html', {'bills': bills})


def bill_create(request):

    bill_form = BillForm(request.POST or None)

    BillItemFormSet = forms.modelformset_factory(BillItem, form=BillItemForm, extra=1)

    formset = BillItemFormSet(request.POST or None, queryset=BillItem.objects.none())

    if bill_form.is_valid() and formset.is_valid():

        bill = bill_form.save()

        for f in formset:

            if f.cleaned_data:

                bill_item = f.save(commit=False)

                bill_item.bill = bill

                bill_item.save()

        return redirect('bill_list')

    return render(request, 'bill_create.html', {'bill_form': bill_form, 'formset': formset})

