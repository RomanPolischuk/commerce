
from ast import Return
from re import M
from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField


# money =moneyed.Money.__format__('+000.00')

class User(AbstractUser):
    pass


class Group(models.Model):
    name = models.CharField(max_length=64, verbose_name="Auction group")

    def __str__(self):
        return f"{self.id}:{self.name}"    


class Auction(models.Model):
    # назву, опис, поточну ціну і фото товару (якщо воно існує)
    name = models.CharField(max_length=64, verbose_name="Auction name")
    description = models.CharField(max_length=256, verbose_name="Auction description")
    # price = models.IntegerField( verbose_name="Auction starting price")
    price = MoneyField(decimal_places=2, default=0,  default_currency='USD', max_digits=11, )
    link_to_foto = models.URLField(blank=True, verbose_name=" Auction URL link to the photo")
    active_auction = models.BooleanField(default=True)
    group = models.ManyToManyField(Group,  blank=True,  related_name="auctions", verbose_name=" Auction group")
    cr_user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name="cr_user")
    
    def groups_to_str(self):
        groups=''
        for a in self.group.all():
            groups += str(a.name)+', '
        if len(groups) > 2:
            groups = groups[ :(len(groups)-2)]
        return groups

    def __str__(self):
        
        return f"{self.cr_user}-{self.id} {self.name}: {self.price} - {self.groups_to_str()} "

    
class  Bid(models.Model):
    bid = MoneyField(decimal_places=2, default=0,  default_currency='USD', max_digits=11, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE )
    
    def __str__(self):
        return f"{self.user}:  {self.auction} bid is {self.bid} " 

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE )
    
    def __str__(self):
        return f"{self.user}:  {self.comment} in {self.auction} " 
    


    