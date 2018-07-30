# Generated by Django 2.0.3 on 2018-04-07 18:24

from django.db import migrations, models

def set_updated_at_default(apps, schema_editor):
    ConversationMessage = apps.get_model('conversations', 'ConversationMessage')
    ConversationMessage.objects.update(updated_at=models.F('created_at'))

class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0011_auto_20180303_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationmessage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RunPython(set_updated_at_default, elidable=True)
    ]