import django_tables2 as tables
from .models import Messages

class MessagesTable(tables.Table):
    
    def render_status(self, value):
        print('go render status')
        return Messages.getStatus(value)

    class Meta:
        model = Messages
        template_name = 'django_tables2/bootstrap.html'