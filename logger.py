import logging

# Basic logger setup
logging.basicConfig(
    filename="test_logs.log",
    filemode="w",  # Append mode
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG  # Set to DEBUG to capture all logs
)

logger = logging.getLogger(__name__)
