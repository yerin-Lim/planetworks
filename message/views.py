from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message, Inbox, Outbox

# Create your views here.
class MessageCreateView(CreateView):

    model = Message
    field = ['']
    def getMessages(request, message_id, nickname):
        user = CustomerUser.objects.get(nickname=nickname)
        inbox = Inbox.objects.get()
        messages = inbox.messages.all().order_by('_date')
        return render(request, )

class MessageReplyView(ReplyView):

    def dispatch(self, request, message_id, *args, **kwargs):
        if request.method.lower() in self.

    def replied(self):
        if self.replied_at is not None:
            return True
        return False

    def __str__(self):
        return self.content

    def save(self, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        super(Message, self).save(**kwargs)

    def admin_sender(self):
        if self.sender:
            return str(self.sender)
        else:
            return '<{0}>'.format(self.email)
    admin_sender.short_description=_("sender")
    admin_sender.admin_order_field="sender"