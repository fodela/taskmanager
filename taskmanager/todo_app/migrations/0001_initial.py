# Generated by Django 3.2.16 on 2022-10-28 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TaskState',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_due', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=264)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.taskcategory')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.taskstate')),
            ],
        ),
    ]