# Generated by Django 3.2.13 on 2022-05-28 20:06

import django.db.models.deletion
from django.db import migrations, models


def save_existing_sla(apps, schema_editor):
    System_Settings_model = apps.get_model('dojo', 'System_Settings')
    SLA_Configuration = apps.get_model('dojo', 'SLA_Configuration')

    system_settings = System_Settings_model.objects.get(id=1)

    SLA_Configuration.name = 'Default'
    SLA_Configuration.critical = system_settings.sla_critical
    SLA_Configuration.high = system_settings.sla_high
    SLA_Configuration.medium = system_settings.sla_medium
    SLA_Configuration.low = system_settings.sla_low

    SLA_Configuration.objects.create(name='Default', description='', critical=system_settings.sla_critical,
                                     high=system_settings.sla_high, medium=system_settings.sla_medium,
                                     low=system_settings.sla_low)


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0161_alter_dojo_group_social_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='SLA_Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A unique name for the set of SLAs.', max_length=128, unique=True, verbose_name='Custom SLA Name')),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('critical', models.IntegerField(default=7, help_text='number of days to remediate a critical finding.', verbose_name='Critical Finding SLA Days')),
                ('high', models.IntegerField(default=30, help_text='number of days to remediate a high finding.', verbose_name='High Finding SLA Days')),
                ('medium', models.IntegerField(default=90, help_text='number of days to remediate a medium finding.', verbose_name='Medium Finding SLA Days')),
                ('low', models.IntegerField(default=120, help_text='number of days to remediate a low finding.', verbose_name='Low Finding SLA Days')),
            ],
            options={
                'ordering': ['name'],
            },
        ),

        migrations.RunPython(save_existing_sla),

        migrations.RemoveField(
            model_name='system_settings',
            name='sla_critical',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='sla_high',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='sla_low',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='sla_medium',
        ),
        migrations.AddField(
            model_name='product',
            name='sla_configuration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='sla_config', to='dojo.sla_configuration'),
        ),
    ]
