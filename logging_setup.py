# logging_setup.py
import seqlog
import json
import logging
from seqlog import set_callback_on_failure

seqlog.log_to_seq(
    server_url="http://host.docker.internal:5341/",
    level=logging.INFO,
    batch_size=10,
    auto_flush_timeout=10,  # seconds
    override_root_logger=True,
    json_encoder_class=json.encoder.JSONEncoder,  # Optional
    support_extra_properties=True  # Optional
)

def handle_a_failure(e): # type: (requests.RequestException) -> None
     print('Failure occurred during log submission: %s' % (e, ))

set_callback_on_failure(handle_a_failure)

logger = logging.getLogger('my-fast-api')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

