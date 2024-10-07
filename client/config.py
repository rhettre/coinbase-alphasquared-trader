import json
from typing import Dict, Any

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.

    :param config_path: Path to the configuration file
    :return: Dictionary containing configuration parameters
    """
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    
    required_keys = ['coinbase_api_key', 'coinbase_api_secret', 'alphasquared_api_key', 'product_id', 'strategy_name']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required configuration key: {key}")
    
    return config