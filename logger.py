import logging
import os
from config import Config
from datetime import datetime

class Logger:
    def __init__(self):
        self.log_dir = Config.get_log_path()
        self.setup_logger()
    
    def setup_logger(self):
        log_file = os.path.join(self.log_dir, f'app_{datetime.now().strftime("%Y%m%d")}.log')
        
        self.logger = logging.getLogger('ElektrikSistem')
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)
    
    def log(self, level, message):
        if level == "INFO":
            self.logger.info(message)
        elif level == "WARNING":
            self.logger.warning(message)
        elif level == "ERROR":
            self.logger.error(message)
        elif level == "SECURITY":
            self.logger.warning(f"[SECURITY] {message}")
        elif level == "AUDIT":
            self.logger.info(f"[AUDIT] {message}")