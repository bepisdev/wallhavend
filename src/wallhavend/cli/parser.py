"""Command-line argument parser for wallhavend."""

import argparse


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.
    
    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog='wallhavend',
        description='Grab and use wallpapers from wallhaven.cc',
        epilog='wallhavend - VERSION 0.3.0'
    )
    
    # Query and search options
    parser.add_argument(
        '-q', '--query',
        metavar="QUERY",
        help="Search term or tag"
    )
    
    parser.add_argument(
        '-p', '--pages',
        metavar="LIMIT",
        type=int,
        help="Limit on how many pages to download (24 images per page)"
    )
    
    # Content filters
    parser.add_argument(
        '-N', '--nsfw',
        action="store_true",
        help="Override config to allow NSFW images in results"
    )
    
    # Output options
    parser.add_argument(
        '-o', '--output',
        metavar="DIR",
        default="./out",
        help="Output directory for downloaded images (default: ./out)"
    )
    
    return parser


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Returns:
        Parsed arguments namespace
    """
    parser = create_parser()
    return parser.parse_args()
