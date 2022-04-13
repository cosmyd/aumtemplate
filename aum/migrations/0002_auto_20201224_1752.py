# Generated by Django 3.1.4 on 2020-12-24 15:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='news_pics')),
                ('paragraph1', models.TextField()),
                ('article', models.TextField()),
                ('gallery', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
