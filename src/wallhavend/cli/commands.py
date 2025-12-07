"""Command execution module for wallhavend CLI."""

from ..core import load_config, WallpaperDownloader
from ..api import WallhavenClient
from .parser import parse_args


def run() -> None:
    """
    Primary console entrypoint. This function is run when `wallhavend`
    is called from the command line.
    """
    # Parse command-line arguments
    args = parse_args()
    
    # Load configuration
    config = load_config()
    
    # Initialize API client
    client = WallhavenClient(api_key=config['api_key'])
    
    # Initialize downloader
    downloader = WallpaperDownloader(
        client=client,
        output_dir=args.output
    )
    
    # Determine NSFW setting (config value or CLI override)
    allow_nsfw = config['allow_nsfw'] or args.nsfw
    
    # Download wallpapers
    try:
        count = downloader.download_search_results(
            query=args.query,
            allow_nsfw=allow_nsfw,
            page_limit=args.pages
        )
        print(f"\n✓ Successfully downloaded {count} wallpapers to {args.output}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        raise
