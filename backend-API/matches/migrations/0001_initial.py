# Generated by Django 5.0.6 on 2024-05-30 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_type', models.CharField(choices=[('dogwalker_likes_pet', 'Dogwalker likes Pet'), ('dogowner_likes_dogwalker', 'Dogowner likes Dogwalker')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('liked_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes_received', to=settings.AUTH_USER_MODEL)),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_given', to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
            options={
                'unique_together': {('liker', 'like_type', 'pet', 'liked_user')},
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_user2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user1', 'user2', 'pet')},
            },
        ),
    ]
