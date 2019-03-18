# Generated by Django 2.1.5 on 2019-03-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('score', models.IntegerField(default=0)),
                ('link', models.URLField()),
                ('timestamp', models.IntegerField()),
                ('top_order_no', models.IntegerField(null=True, unique=True)),
                ('sentiment_score', models.FloatField(blank=True)),
                ('new_order_no', models.IntegerField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'stories',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='story',
            field=models.ManyToManyField(blank=True, related_name='categories', to='top_articles.Story'),
        ),
    ]
