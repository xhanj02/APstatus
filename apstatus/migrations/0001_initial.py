# Generated by Django 2.1.7 on 2019-03-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ips',
            fields=[
                ('ip', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('t11', models.IntegerField(blank=True, null=True)),
                ('t10', models.IntegerField(blank=True, null=True)),
                ('t9', models.IntegerField(blank=True, null=True)),
                ('t8', models.IntegerField(blank=True, null=True)),
                ('t7', models.IntegerField(blank=True, null=True)),
                ('t6', models.IntegerField(blank=True, null=True)),
                ('t5', models.IntegerField(blank=True, null=True)),
                ('t4', models.IntegerField(blank=True, null=True)),
                ('t3', models.IntegerField(blank=True, null=True)),
                ('t2', models.IntegerField(blank=True, null=True)),
                ('t1', models.IntegerField(blank=True, null=True)),
                ('t0', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]