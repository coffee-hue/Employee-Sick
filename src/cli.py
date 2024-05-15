import logging
import daemon
import click
from src.api.main import dev


@click.group()
def cli():
    """Main cli group"""

@cli.command("run", help="Start the api and website")
def run():
    """Runs the main process for the application"""
    ...
    
@cli.command("deve", help="Developer mode mode")
def deve():
    """Runs a dev version for GraphQL and web Debugging"""
    dev()

if __name__ == "__main__":
    cli()