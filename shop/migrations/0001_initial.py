# Generated by Django 3.1 on 2020-09-03 17:07

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', wagtail.core.fields.StreamField([('Category', wagtail.core.blocks.ChoiceBlock(choices=['bread', 'cheese', 'meat', 'other', 'sauce']))])),
                ('allergens', wagtail.core.fields.StreamField([('Allergens', wagtail.core.blocks.MultipleChoiceBlock(choices=['dairy', 'eggs', 'meat', 'nuts'], required=False))])),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Toastie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ingredient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]