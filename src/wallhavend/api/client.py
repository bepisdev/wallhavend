"""Wallhaven API client for interacting with wallhaven.cc API."""

import requests
from typing import Optional, Dict, Any


class WallhavenClient:
    """Client for interacting with the Wallhaven.cc API."""
    
    BASE_URL = "https://wallhaven.cc/api/v1"
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Wallhaven API client.
        
        Args:
            api_key: Optional API key for authenticated requests
        """
        self.api_key = api_key
        self.session = requests.Session()
    
    def _build_search_url(self) -> str:
        """
        Build the search URL with optional API key.
        
        Returns:
            The complete search URL
        """
        url = f"{self.BASE_URL}/search"
        if self.api_key:
            url += f"?apikey={self.api_key}"
        return url
    
    def search(
        self,
        query: Optional[str] = None,
        purity: str = "100",
        categories: str = "111",
        sorting: str = "date_added",
        page: int = 1
    ) -> Dict[str, Any]:
        """
        Search for wallpapers on Wallhaven.
        
        Args:
            query: Search term or tag
            purity: Content filter (100=SFW, 110=SFW+Sketchy, 111=All)
            categories: Categories to search (111=General+Anime+People)
            sorting: Sort order (date_added, relevance, random, views, favorites)
            page: Page number for pagination
        
        Returns:
            JSON response containing search results and metadata
        """
        url = self._build_search_url()
        
        payload = {
            "q": query,
            "purity": purity,
            "categories": categories,
            "sorting": sorting,
            "page": page
        }
        
        response = self.session.get(url, params=payload)
        response.raise_for_status()
        return response.json()
    
    def get_metadata(
        self,
        query: Optional[str] = None,
        purity: str = "100"
    ) -> Dict[str, Any]:
        """
        Get metadata for a search query without downloading images.
        
        Args:
            query: Search term or tag
            purity: Content filter
        
        Returns:
            Metadata dictionary containing total pages, count, etc.
        """
        result = self.search(query=query, purity=purity, page=1)
        return result.get("meta", {})
    
    def download_image(self, url: str) -> bytes:
        """
        Download an image from a given URL.
        
        Args:
            url: The URL of the image to download
        
        Returns:
            Image content as bytes
        """
        response = self.session.get(url, stream=True)
        response.raise_for_status()
        return response.content


class ImageInfo:
    """Data class for wallpaper image information."""
    
    def __init__(self, image_data: Dict[str, Any]):
        """
        Initialize ImageInfo from API response data.
        
        Args:
            image_data: Dictionary containing image information from API
        """
        self.id = image_data.get("id")
        self.url = image_data.get("url")
        self.path = image_data.get("path")
        self.file_type = image_data.get("file_type", "")
        self.resolution = image_data.get("resolution")
        self.colors = image_data.get("colors", [])
        self.views = image_data.get("views", 0)
        self.favorites = image_data.get("favorites", 0)
    
    @property
    def extension(self) -> str:
        """Get the file extension from the file type."""
        return self.file_type.split("/")[-1] if self.file_type else "jpg"
    
    @property
    def filename(self) -> str:
        """Generate a filename for the image."""
        return f"{self.id}.{self.extension}"
