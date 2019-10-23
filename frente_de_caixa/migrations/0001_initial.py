# Generated by Django 2.2.5 on 2019-10-22 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0010_auto_20191022_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_final', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItensDeVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Servico')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frente_de_caixa.Vendas')),
            ],
        ),
    ]
