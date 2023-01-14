# Generated by Django 4.0 on 2022-11-26 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_sdp'),
        ('stories', '0008_alter_story_rep_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=1000)),
                ('isParent', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mention', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentionedComments', to='users.user')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childs', to='stories.storycomment')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='stories.story')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
