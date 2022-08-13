# Generated by Django 4.0.4 on 2022-07-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auction_cr_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='group',
        ),
        migrations.AddField(
            model_name='auction',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='auctions', to='auctions.group', verbose_name=' Auction group'),
        ),
    ]
