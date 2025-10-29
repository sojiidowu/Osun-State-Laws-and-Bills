from django.db import models
# from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class BillOrLaw(models.Model):
    BILL = "BILL"
    LAW = "LAW"
    TYPE_CHOICES = [
        (BILL, "Bill"),
        (LAW, "Law"),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="documents/")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.type})"


class Payment(models.Model):
    bill_or_law = models.ForeignKey(BillOrLaw, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.bill_or_law.title} - {self.status}"


# class Payment(models.Model):
#    STATUS_CHOICES = [
#        ("PENDING", "Pending"),
#        ("SUCCESS", "Success"),
#        ("FAILED", "Failed"),
#    ]
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    bill_or_law = models.ForeignKey("BillOrLaw", on_delete=models.CASCADE)
#    amount = models.DecimalField(max_digits=8, decimal_places=2)
#    status = models.CharField(
#        max_length=10, choices=STATUS_CHOICES, default="PENDING")
#    payment_date = models.DateTimeField(auto_now_add=True)
#    reference = models.CharField(max_length=100, unique=True)

#    def __str__(self):
#        return f"{self.user.username} - {self.bill_or_law.title}"
