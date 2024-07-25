# logging_setup.py
import os
from dotenv import load_dotenv
import logging
import seqlog
from seqlog import set_callback_on_failure, log_to_seq

# Load the .env file based on the current environment
if os.environ.get('ENV') == 'dev':
    load_dotenv('.dev.env')
elif os.environ.get('ENV') == 'prod':
    load_dotenv('.prod.env')
else:
    load_dotenv('.env')

def setup_logger(name):
    logger = logging.getLogger(name)
    # Retrieve the desired log level from an environment variable or default to DEBUG
    log_level = os.environ.get('LOGGING_LEVEL', 'DEBUG').upper()
    logger.setLevel(log_level)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    return logger

# Set up Seqlog with retry logic and centralized error logging
def setup_seqlog():
    server_url = os.environ.get('SEQLOG_SERVER_URL', 'http://host.docker.internal:5341/')
    batch_size = int(os.environ.get('SEQLOG_BATCH_SIZE', 10))
    
    def handle_a_failure(e): # type: (requests.RequestException) -> None
        logger = logging.getLogger(__name__)
        logger.error('Failure occurred during log submission: %s' % e, exc_info=True)
        
        # Retry logic or other error handling mechanisms can be implemented here
    
    set_callback_on_failure(handle_a_failure)
    
    seqlog.log_to_seq(
        server_url=server_url,
        level=logging.INFO,
        batch_size=batch_size,
        auto_flush_timeout=10,  # seconds
        override_root_logger=True
    )
    
# Set up Seqlog and console handlers for all available loggers in the application
for name in logging.Logger.manager.loggerDict:
    if not name.startswith('seqlog.'):
        setup_logger(name)  # Create a logger instance with configurable level
        
setup_seqlog()  # Set up Seqlog for centralized log submission
