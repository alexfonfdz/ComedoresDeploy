# Generated by Django 3.2.6 on 2025-03-07 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('second_lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('rfc', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='ClientDiner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_diner_client', to='home.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_diner_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client Diner',
                'verbose_name_plural': 'Clients Diners',
                'db_table': 'client_diner',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeed_code', models.CharField(blank=True, max_length=25, null=True)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('second_lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_client', to='home.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='EmployeeClientDiner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('client_diner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_client_diner_client_diner', to='home.clientdiner')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_diner_created_by', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_client_diner_employee', to='home.employee')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_diner_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee Client Diner',
                'verbose_name_plural': 'Employees Clients Diners',
                'db_table': 'employee_client_diner',
            },
        ),
        migrations.CreateModel(
            name='Lots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_diner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lots_client_diner', to='home.clientdiner')),
            ],
            options={
                'verbose_name': 'Lot',
                'verbose_name_plural': 'Lots',
                'db_table': 'lots',
            },
        ),
        migrations.CreateModel(
            name='PayrollType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Payroll Type',
                'verbose_name_plural': 'Payroll Types',
                'db_table': 'payroll_type',
            },
        ),
        migrations.CreateModel(
            name='VoucherType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Voucher Type',
                'verbose_name_plural': 'Voucher Types',
                'db_table': 'voucher_type',
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(blank=True, max_length=100)),
                ('employee', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
                ('lots', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='voucher_lots', to='home.lots')),
            ],
            options={
                'verbose_name': 'Voucher',
                'verbose_name_plural': 'Vouchers',
                'db_table': 'voucher',
            },
        ),
        migrations.AddField(
            model_name='lots',
            name='voucher_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lots_voucher_type', to='home.vouchertype'),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_diner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entry_client_diner', to='home.clientdiner')),
                ('employee_client_diner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entry_employee_client_diner', to='home.employeeclientdiner')),
                ('voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entry_voucher', to='home.voucher')),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
                'db_table': 'entry',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='payroll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_payroll', to='home.payrolltype'),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DiningRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dining_room_created_by', to=settings.AUTH_USER_MODEL)),
                ('in_charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dining_room_in_charge', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dining_room_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dining Room',
                'verbose_name_plural': 'Dining Rooms',
                'db_table': 'dining_room',
            },
        ),
        migrations.AddField(
            model_name='clientdiner',
            name='dining_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_diner_dining_room', to='home.diningroom'),
        ),
        migrations.AddField(
            model_name='clientdiner',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_diner_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
