from django.db import models

# Create your models here.
class Clients(models.Model):
    client_first_name = models.CharField(max_length=254)
    client_last_name  = models.CharField(max_length=254)
    client_address    = models.CharField(max_length=254)
    client_phone      = models.CharField(max_length=11)
    client_email      = models.EmailField(max_length=254)
    client_create_at  = models.DateField(auto_now=True)


class Cards(models.Model):
    cards_id          = models.ForeignKey(Clients, on_delete=models.CASCADE)
    cards_numbers     = models.CharField(max_length=16)
    cards_date        = models.DateField(auto_created=True)
    cards_exp         = models.DateField()
    cards_full_name   = models.CharField(max_length=508)
    cards_cvv         = models.CharField(max_length=3)
    cards_amount      = models.BigIntegerField()


class Transaction(models.Model):
    transaction_reciver = models.CharField()
    transaction_sender  = models.CharField()
    transaction_date    = models.DateField()
    transaction_amount  = models.BigIntegerField()