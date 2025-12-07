import configparser
from pathlib import Path


def get_config_path():
    """
    Returns the path to the config file in ~/.config/wallhavend/config.ini
    """
    home = Path.home()
    config_dir = home / ".config" / "wallhavend"
    config_file = config_dir / "config.ini"
    return config_file


def ensure_config_exists():
    """
    Ensures the config directory and file exist. Creates them with
    default values if they don't exist.
    """
    config_file = get_config_path()
    config_dir = config_file.parent
    
    # Create directory if it doesn't exist
    if not config_dir.exists():
        config_dir.mkdir(parents=True, exist_ok=True)
    
    # Create config file with defaults if it doesn't exist
    if not config_file.exists():
        config = configparser.ConfigParser()
        config['wallhaven'] = {
            'api_key': '',
            'allow_nsfw': 'false'
        }
        with open(config_file, 'w') as f:
            config.write(f)
    
    return config_file


def load_config():
    """
    Loads the configuration from ~/.config/wallhavend/config.ini
    
    Returns a dictionary with the configuration values:
    - api_key: The wallhaven.cc API key (string)
    - allow_nsfw: Whether to allow NSFW content (boolean)
    """
    config_file = ensure_config_exists()
    
    config = configparser.ConfigParser()
    config.read(config_file)
    
    # Extract values with defaults
    api_key = config.get('wallhaven', 'api_key', fallback='')
    allow_nsfw = config.getboolean('wallhaven', 'allow_nsfw', fallback=False)
    
    # Return empty string if api_key is not set
    if api_key.strip() == '':
        api_key = None
    
    return {
        'api_key': api_key,
        'allow_nsfw': allow_nsfw
    }


def save_config(api_key=None, allow_nsfw=None):
    """
    Updates the configuration file with new values.
    
    Params:
        - api_key: The wallhaven.cc API key to save
        - allow_nsfw: Whether to allow NSFW content (boolean)
    """
    config_file = ensure_config_exists()
    
    config = configparser.ConfigParser()
    config.read(config_file)
    
    if not config.has_section('wallhaven'):
        config.add_section('wallhaven')
    
    if api_key is not None:
        config.set('wallhaven', 'api_key', api_key)
    
    if allow_nsfw is not None:
        config.set('wallhaven', 'allow_nsfw', str(allow_nsfw).lower())
    
    with open(config_file, 'w') as f:
        config.write(f)
