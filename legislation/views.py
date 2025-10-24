from django.shortcuts import render, get_object_or_404
from .models import BillOrLaw


def law_list(request):
    laws = BillOrLaw.objects.all().order_by('-created_at')
    return render(request, 'legislation/law_list.html', {'laws', laws})


def law_detail(request, pk):
    law = get_object_or_404(BillOrLaw, pk)
    return render(request, 'legislation/law_detail.html', {'law', law})
