# wallhavend

Simple daemon to handle retrieve and use wallpapers from wallhaven.cc

## Configuration

wallhavend uses a configuration file located at `~/.config/wallhavend/config.ini`.

On first run, the config file will be created automatically with default values. You can edit it to add your API key and set preferences.

### Example config file

```ini
[wallhaven]
api_key = your_api_key_here
allow_nsfw = false
```

### Configuration Options

- `api_key` - Your Wallhaven.cc API key (required for accessing NSFW content and personal collections)
- `allow_nsfw` - Set to `true` to allow NSFW images in search results, `false` to filter them out

## Usage

```shell
wallhavend [OPTIONS]
```

### Available command-line options

#### Options and Settings

- `--query <QUERY>` or `-q` - Search term or tag.
- `--pages <LIMIT>` or `-p` - How many pages to run over (API Results are paginated).

#### Flags

- `--nsfw` or `-N` - Override config to enable NSFW images in results for this run.
- `--help` or `-h` - Display help message.

## Installation

### From Homebrew

> Coming Soon

### From Source

#### 1. Download source

```console
git clone https://github.com/bepisdev/wallhavend
```

#### 2. Install requirements and setup venv with uv

```console
uv sync
```

#### 3. Build wheel package

```console
uv pip install build
uv run python -m build
```

#### 4. Install package

```console
pip install ./dist/wallhavend-<version>-py3-none-any.whl
```
