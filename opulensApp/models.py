from django.db import models # type: ignore

class UserAccount(models.Model):
    username = models.CharField(max_length=101)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class BudgetEntry(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount} on {self.date}"