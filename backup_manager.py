import os
import shutil
import datetime
import zipfile
from cryptography.fernet import Fernet

class BackupManager:
    def __init__(self, database_path, backup_dir):
        self.database_path = database_path
        self.backup_dir = backup_dir
        self.encryption_key = self.generate_key()

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        fernet = Fernet(self.encryption_key)
        encrypted = fernet.encrypt(data)
        with open(file_path + '.encrypted', 'wb') as file:
            file.write(encrypted)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        fernet = Fernet(self.encryption_key)
        decrypted = fernet.decrypt(encrypted_data)
        with open(file_path.replace('.encrypted', ''), 'wb') as file:
            file.write(decrypted)

    def create_backup(self):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        backup_filename = os.path.join(self.backup_dir, f'backup_{today}_db.zip')
        with zipfile.ZipFile(backup_filename, 'w') as zipf:
            zipf.write(self.database_path, os.path.basename(self.database_path))
        self.encrypt_file(backup_filename)

    def restore_backup(self, backup_file):
        self.decrypt_file(backup_file)
        with zipfile.ZipFile(backup_file.replace('.encrypted', ''), 'r') as zipf:
            zipf.extractall(path=self.backup_dir)

if __name__ == '__main__':
    db_path = '/path/to/database'
    backup_path = '/path/to/backup'
    manager = BackupManager(db_path, backup_path)
    manager.create_backup()  # For automatic daily backup you can use a scheduler
