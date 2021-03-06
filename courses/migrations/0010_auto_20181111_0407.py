# Generated by Django 2.1.3 on 2018-11-11 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20181111_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.Room'),
        ),
        migrations.AlterField(
            model_name='course',
            name='coreqs',
            field=models.ManyToManyField(blank=True, related_name='_course_coreqs_+', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='countsAs',
            field=models.ManyToManyField(blank=True, related_name='_course_countsAs_+', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prereqs',
            field=models.ManyToManyField(blank=True, related_name='_course_prereqs_+', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='sameAs',
            field=models.ManyToManyField(blank=True, related_name='_course_sameAs_+', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='session',
            name='block',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.Block'),
        ),
    ]
