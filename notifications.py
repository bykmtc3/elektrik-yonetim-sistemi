import smtplib
from email.mime.text import MIMEText

class NotificationSystem:
    def __init__(self, email_settings):
        self.email_settings = email_settings
        
    def send_email_notification(self, subject, message):
        # Set up the server
        server = smtplib.SMTP(self.email_settings['smtp_server'], self.email_settings['smtp_port'])
        server.starttls()
        server.login(self.email_settings['username'], self.email_settings['password'])

        # Create the email
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.email_settings['from_addr']
        msg['To'] = self.email_settings['to_addr']

        # Send the email
        server.sendmail(self.email_settings['from_addr'], self.email_settings['to_addr'], msg.as_string())
        server.quit()

    def notify_low_stock(self, item, quantity):
        subject = 'Low Stock Alert'
        message = f'Item {item} is low on stock. Current quantity: {quantity}'
        self.send_email_notification(subject, message)

    def notify_price_change(self, item, old_price, new_price):
        subject = 'Price Change Alert'
        message = f'Item {item} price has changed from {old_price} to {new_price}'
        self.send_email_notification(subject, message)

    def notify_backup_status(self, success):
        subject = 'Backup Status'
        message = 'Backup succeeded!' if success else 'Backup failed!'
        self.send_email_notification(subject, message)

    def notify_system_health(self, status):
        subject = 'System Health Monitoring'
        message = f'System health status: {status}'
        self.send_email_notification(subject, message)