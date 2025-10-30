from django.shortcuts import render, get_object_or_404, redirect
from .models import BillOrLaw, Payment
from django.http import FileResponse, HttpResponse


def law_list(request):
    laws = BillOrLaw.objects.all().order_by('-created_at')
    return render(request, 'legislation/law_list.html', {'laws': laws})


def law_detail(request, pk):
    law = get_object_or_404(BillOrLaw, pk=pk)
    return render(request, 'legislation/law_detail.html', {'law': law})


# For handling free and paid download
def download_law(request, pk):
    law = get_object_or_404(BillOrLaw, pk=pk)

    # free law to be downloaded directly
    if law.price == 0:
        if law.file:
            return FileResponse(open(law.file.path, 'rb'), as_attachment=True)
        else:
            return HttpResponse("No document available.")
    else:
        # redirect to mock payment form for paid laws
        return redirect('mock_payment', pk=law.pk)


# Mock payment page
def mock_payment(request, pk):
    law = get_object_or_404(BillOrLaw, pk=pk)

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')

        Payment.objects.create(
            law=law,
            full_name=full_name,
            email=email,
            amount=law.price,
            status='completed'
        )
        # After the mock payment, allow download
        if law.file:
            return FileResponse(open(law.file.path, 'rb'), as_attachment=True)
        else:
            return HttpResponse("No document available.")
    return render(request, 'legislation/mock_payment.html', {'law': law})
