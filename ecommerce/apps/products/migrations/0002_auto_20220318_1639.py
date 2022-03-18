# Generated by Django 3.1.3 on 2022-03-18 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproduct',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Producto '},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto ', 'verbose_name_plural': 'Productos'},
        ),
    ]