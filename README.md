# wallhavend
Simple daemon to handle retrieve and use wallpapers from wallhaven.cc

# Configuration

wallhavend uses a configuration file located at `~/.config/wallhavend/config.ini`.

On first run, the config file will be created automatically with default values. You can edit it to add your API key and set preferences.

## Example config.ini

```ini
[wallhaven]
api_key = your_api_key_here
allow_nsfw = false
```

### Configuration Options

- `api_key` - Your Wallhaven.cc API key (required for accessing NSFW content and personal collections)
- `allow_nsfw` - Set to `true` to allow NSFW images in search results, `false` to filter them out

# Usage

```shell
$ wallhavend [OPTIONS]
```

## Available command-line options

__Options and Settings__

- `--query <QUERY>` or `-q` - Search term or tag.
- `--pages <LIMIT>` or `-p` - How many pages to run over (API Results are paginated).

__Flags__

- `--nsfw` or `-N` - Override config to enable NSFW images in results for this run.
- `--help` or `-h` - Display help message.

## Installation

1. Download source
2. Use `poetry` to build the wheel package
   ```shell
   $ poetry build
   ```
3. Install wheel with pip
   ```shell
   $ pip install ./path/to/package.whl
   ```
4. Run `wallhavend` command
   ```shell
   $ wallhavend
   ```
