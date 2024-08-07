# Generated by Django 5.0.6 on 2024-07-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDB',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120, unique=True)),
                ('description', models.CharField(max_length=350)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image_url', models.ImageField(null=True, upload_to='MainApp/static/img/')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'db_table': 'ItemDB',
            },
        ),
    ]
