import imaplib
import email
import re


class EmailClient():
    list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')
    username = 'admin@sublimart.pe'
    password = 'admin'
    hostname = 'prince.superdnssite.com'
    directory = 'Inbox'
    connection = None
    
    def __init__(self):
        self.open_connection()

    def open_connection(self, verbose=False):
        self.connection = imaplib.IMAP4_SSL(self.hostname)
        self.connection.login(self.username, self.password)

    def get_email_tickets(self):
        try:
            data = []
            self.connection.select('INBOX', readonly=True)
            status, count = self.connection.select(self.directory)
            count = int(count[0]) + 1
            for index in range(1, count):
                info = {}
                print 'HEADER:'
                typ, msg_data = self.connection.fetch(index, '(BODY.PEEK[HEADER])')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        info['subject'] = msg['subject']
                        info['from'] = msg['from']

                print 'BODY TEXT:'
                typ, msg_data = self.connection.fetch(index, '(BODY.PEEK[TEXT])')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        info['message'] = response_part[1]
                data.append(info)
                # typ, msg_data = self.connection.fetch(index, '(FLAGS)')
                # typ, response = self.connection.store(index, '+FLAGS', r'(\Deleted)')
                # typ, response = self.connection.expunge()
        finally:
            self.close_connection()
        return data

    def parse_list_response(self, line):
        flags, delimiter, mailbox_name = self.list_response_pattern.match(line).groups()
        mailbox_name = mailbox_name.strip('"')
        return (flags, delimiter, mailbox_name)
    
    def close_connection(self):
        self.connection.close()
        self.connection.logout()