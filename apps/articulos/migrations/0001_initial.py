# Generated by Django 4.2.3 on 2023-07-21 19:01

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
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('contenido_breve', models.CharField(max_length=200)),
                ('contenido_completo', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to='articulos')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_comentario', models.CharField(max_length=100)),
                ('comentario', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('articulo_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='articulos.articulo')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria_articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.categoria'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='usuario_articulo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
