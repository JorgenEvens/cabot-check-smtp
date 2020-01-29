import sys
import smtplib

from django.db import models

from cabot.cabotapp.models import StatusCheck, StatusCheckResult

class SmtpSession:

    def __init__(self):
        self.c = smtplib.SMTP()
        self.conversation = []

    def connect(self, host, port):
        self._handle_response(self.c.connect(host, port))

    def ehlo(self, name):
        self.log("> EHLO " + name)
        self._handle_response(self.c.ehlo(name))

    def call(self, cmd, args = ''):
        self.log("> " + cmd + " " + args)
        self._handle_response(self.c.docmd(cmd, args))

    def log(self, message):
        self.conversation.append(message)

    def quit(self):
        if self.c and hasattr(self.c, 'sock'):
            self.log('> QUIT');
            code, message = self.c.quit()
            self.log(str(code) + " " + str(message))

    def _handle_response(self, res):
        code, message = res
        self.log(str(code) + " " + str(message))

        if (code >= 300):
            raise Exception('Unexpected response code')

class SmtpStatusCheck(StatusCheck):
    check_name = 'smtp'
    edit_url_name = 'update-smtp-check'
    duplicate_url_name = 'duplicate-smtp-check'
    icon_class = 'glyphicon-envelope'
    host = models.TextField(
        help_text='Host to check.',
    )
    port = models.PositiveIntegerField(
        help_text='Port to check.',
    )
    helo_address = models.TextField(
        help_text='Advertised client address',
    )
    sender = models.EmailField(
        help_text='Address to test sending as',
    )
    recipient = models.EmailField(
        help_text='Address to test sending to',
    )

    def _run(self):
        result = StatusCheckResult(status_check=self)

        sess = SmtpSession()
        conversation = []
        try:
            sess.connect(self.host, self.port)
            sess.ehlo(self.helo_address)

            if self.sender:
                sess.call('MAIL FROM:', self.sender)

            if self.sender and self.recipient:
                sess.call('RCPT TO:', self.recipient)

        except Exception as e:
            result.error = u'Error occurred: %s' % (e.message,)
            result.succeeded = False
        except:
            result.error = u'Error occurred: %s' % (sys.exc_info()[0],)
            result.succeeded = False
        else:
            result.succeeded = True
        finally:
            sess.quit()

        result.raw_data = "\n".join(sess.conversation)

        return result
