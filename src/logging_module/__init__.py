import logging

logging.basicConfig(
    filename='failed_login_attempts.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_alert(message):
    print(message)  # Always print to console
    logging.info(message)