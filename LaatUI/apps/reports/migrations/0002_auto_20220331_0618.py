# Generated by Django 3.2.12 on 2022-03-31 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportmodel',
            name='state',
            field=models.CharField(default='成功', help_text='状态', max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='project',
            field=models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, related_name='report', to='projects.projectmodel', verbose_name='所属项目'),
        ),
    ]
