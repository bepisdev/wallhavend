"""Core downloader module for handling wallpaper downloads."""

from pathlib import Path
from typing import Optional

from rich.progress import track

from ..api import WallhavenClient, ImageInfo
from ..utils import save_binary_file, get_output_directory


class WallpaperDownloader:
    """Handles downloading wallpapers from Wallhaven."""
    
    def __init__(
        self,
        client: WallhavenClient,
        output_dir: str | Path = "./out"
    ):
        """
        Initialize the downloader.
        
        Args:
            client: Wallhaven API client
            output_dir: Directory to save downloaded images
        """
        self.client = client
        self.output_dir = get_output_directory(str(output_dir))
    
    def download_image(self, image_info: ImageInfo) -> Path:
        """
        Download a single image.
        
        Args:
            image_info: Information about the image to download
        
        Returns:
            Path to the downloaded file
        """
        image_data = self.client.download_image(image_info.path)
        filepath = self.output_dir / image_info.filename
        save_binary_file(filepath, image_data)
        return filepath
    
    def download_search_results(
        self,
        query: Optional[str] = None,
        allow_nsfw: bool = False,
        page_limit: Optional[int] = None
    ) -> int:
        """
        Download wallpapers from search results.
        
        Args:
            query: Search term or tag
            allow_nsfw: Whether to include NSFW content
            page_limit: Maximum number of pages to download (None for all)
        
        Returns:
            Number of images downloaded
        """
        # Determine purity filter
        purity = "111" if allow_nsfw else "100"
        
        # Get metadata to determine total pages
        metadata = self.client.get_metadata(query=query, purity=purity)
        total_pages = metadata.get("last_page", 1)
        
        # Set page limit
        max_pages: int
        if page_limit is None:
            max_pages = total_pages
        else:
            max_pages = min(int(page_limit), total_pages)
        
        downloaded_count = 0
        
        # Download images from each page
        for page_num in range(1, max_pages + 1):
            results = self.client.search(
                query=query,
                purity=purity,
                page=page_num
            )
            
            images = results.get("data", [])
            
            # Download each image with progress bar
            for image_data in track(
                images,
                description=f'[green]Processing page {page_num}/{max_pages}'
            ):
                image_info = ImageInfo(image_data)
                self.download_image(image_info)
                downloaded_count += 1
        
        return downloaded_count
