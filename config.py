import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Application
    APP_NAME = "Elektrik Yönetim Sistemi"
    APP_VERSION = "1.0.0"
    DEBUG = False
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
    
    # Database
    DATABASE_PATH = os.getenv("DATABASE_PATH", "./data/elektrik_system.db")
    
    # Backup
    BACKUP_DIR = os.getenv("BACKUP_DIR", "./backups")
    AUTO_BACKUP_INTERVAL = 86400  # 24 hours
    
    # Logging
    LOG_DIR = os.getenv("LOG_DIR", "./logs")
    LOG_LEVEL = "INFO"
    
    # UI
    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 900
    
    # DWG
    DWG_UPLOAD_DIR = "./uploads/dwg"
    MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
    
    # Reports
    REPORT_DIR = "./reports"
    
    @staticmethod
    def get_db_path():
        os.makedirs(os.path.dirname(Config.DATABASE_PATH), exist_ok=True)
        return Config.DATABASE_PATH
    
    @staticmethod
    def get_backup_path():
        os.makedirs(Config.BACKUP_DIR, exist_ok=True)
        return Config.BACKUP_DIR
    
    @staticmethod
    def get_log_path():
        os.makedirs(Config.LOG_DIR, exist_ok=True)
        return Config.LOG_DIR