# Generated by Django 4.0.2 on 2022-02-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_dest_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=120)),
                ('item_desc', models.CharField(max_length=120)),
                ('item_price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='dest',
        ),
    ]
