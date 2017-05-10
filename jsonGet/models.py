from django.db import models
#from django import forms

# Create your models here.

class StockM(models.Model):
    item = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    volume = models.CharField(max_length=30)
    time = models.CharField(max_length=30)

    def as_json(self):
        return dict(item=self.item, price=self.price,
                    volume=self.volume,time=self.time)

'''class MyForm(forms.ModelForm):
    class Meta:
        model = StockN'''
