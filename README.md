# wallhavend

A modern CLI tool for downloading wallpapers from wallhaven.cc with a clean, modular architecture.

## Features

- 🎨 Search and download wallpapers from Wallhaven.cc
- ⚙️ Configuration file support for persistent settings
- 🔒 NSFW content filtering with config and CLI override options
- 📦 Clean, modular codebase with separation of concerns
- 🚀 Built with modern Python practices

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

- `--query <QUERY>` or `-q` - Search term or tag
- `--pages <LIMIT>` or `-p` - Maximum number of pages to download (24 images per page)
- `--output <DIR>` or `-o` - Output directory for downloaded images (default: ./out)

#### Flags

- `--nsfw` or `-N` - Override config to enable NSFW images in results for this run
- `--help` or `-h` - Display help message

### Examples

```shell
# Search for nature wallpapers
wallhavend -q "nature"

# Download first 5 pages of anime wallpapers
wallhavend -q "anime" -p 5

# Enable NSFW for this search only
wallhavend -q "art" -N

# Specify custom output directory
wallhavend -q "landscape" -o ~/Pictures/Wallpapers
```

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
