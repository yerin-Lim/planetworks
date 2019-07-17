from django.db import models
from django.contrib.auth.decorators import login_required
# Create your models here.

class Message(models.Model):
    message_id = models.IntegerField(primary_key=True)
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', verbose_name=_("Sender"), on_delete=models.SET_NULL)
    recipient = models.ForeignKey(CustomUser, related_name='received_messages', verbose_name=_("Recipient"), null=True, blank=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=1000, blank=True)
    sent_at = models.DateTimeField(_("sent at"), null=True, blank=True)
    replied_at = models.DateTimeField(_("replied at"), null=True, blank=True)
    
class Inbox(models.Model):
    message_id = models.ForeignKey(Message, on_delete='CASCADE')
    sender = models.ForeignKey(CustomUser, on_delete='CASCADE')
    receiver = models.ForeignKey(CustomUser, on_delete='CASCADE')

class Outbox(models.Model):
    message_id = models.ForeignKey(Message, on_delete='CASCADE')
    sender = models.ForeignKey(CustomUser, on_delete='CASCADE')
    receiver = models.ForeignKey(CustomUser, on_delete='CASCADE')