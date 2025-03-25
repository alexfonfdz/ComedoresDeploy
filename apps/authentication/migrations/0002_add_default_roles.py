# Generated by Django 3.2.6 on 2024-12-14 03:41

from django.db import migrations

def create_default_roles(apps, schema_editor):
    Role = apps.get_model('authentication', 'Role')
    roles = ['Administrador', 'Estándar']
    for role in roles:
        if not Role.objects.filter(name=role).exists():
            Role.objects.create(name=role)

def create_default_user_admin(apps, schema_editor):
    User = apps.get_model('authentication', 'CustomUser')
    Role = apps.get_model('authentication', 'Role')
    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_user(
            username='admin',
            password='admin',
        )
        user.role = Role.objects.get(name='Administrador')
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_roles),
        migrations.RunPython(create_default_user_admin),
    ]