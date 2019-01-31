# Generated by Django 2.1.5 on 2019-01-31 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_articles', '0003_story_order_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='story',
            old_name='order_no',
            new_name='top_order_no',
        ),
        migrations.AddField(
            model_name='story',
            name='new_order_no',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='story',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to='top_articles.Story'),
        ),
    ]
