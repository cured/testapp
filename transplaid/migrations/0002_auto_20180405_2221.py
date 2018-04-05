# Generated by Django 2.0.1 on 2018-04-05 22:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transplaid', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('transaction_id',)},
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='accounts',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='location',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payment_meta',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='total_transactions',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transactions',
        ),
        migrations.AddField(
            model_name='transaction',
            name='by_order_of',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='payee',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_processor',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='ppd_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='reason',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='reference_number',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='store_number',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='zip',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]