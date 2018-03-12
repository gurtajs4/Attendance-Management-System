# Generated by Django 2.0.3 on 2018-03-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClassMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentId', models.IntegerField()),
                ('classId', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='classdetails',
            name='classDay',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='classdetails',
            name='classEndTime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='classdetails',
            name='classStartTime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='professordetails',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='attendancedetails',
            name='classId',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='attendancedetails',
            name='raspPieMacAddress',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='attendancedetails',
            name='studentMacAddress',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='classdetails',
            name='classId',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='classprofessormapping',
            name='classId',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='macAddress',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
