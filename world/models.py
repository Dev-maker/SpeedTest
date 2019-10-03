from django.contrib.gis.db import models


class Data(models.Model):
    IpAddress = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    post = models.CharField(max_length=5)
    location = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class speed(models.Model):
    ping_ip = models.ForeignKey(Data, on_delete=models.CASCADE)
    upload = models.CharField(max_length=100)
    download = models.CharField(max_length=100)

    def __str__(self):
        return self.upload


class user(models.Model):
    user_city = models.ForeignKey(Data, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.name
