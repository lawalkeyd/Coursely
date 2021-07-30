# Generated by Django 3.2.5 on 2021-07-30 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_content_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='courses.module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='courses.module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='text',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='text', to='courses.module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='courses.module'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
