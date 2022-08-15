from django.db import models


class Brands(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Models(models.Model):   # I'd rather have a different name tbh
    name = models.CharField(max_length=200, primary_key=True)
    brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Vehicles(models.Model):
    legal_identifier = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    frame_size = models.IntegerField()
    status = models.IntegerField()
    model_id = models.ForeignKey(Models, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
