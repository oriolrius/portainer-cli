import os
import sys
import logging
import structlog
import click
from portainer.lib.portainer_api import PortainerAPI

CONTEXT_SETTINGS = dict(auto_envvar_prefix="PORTAINER")
LOG_LEVEL = getattr(logging,
                    os.environ.get("LOG_LEVEL", "INFO").upper())

class Environment:
    def __init__(self):
        self.portainer_client = None
        self.logger = self.setLogLevel(LOG_LEVEL)

    def setLogLevel(self, level):
        structlog.configure(
            wrapper_class=structlog.make_filtering_bound_logger(level)
        )
        return structlog.get_logger()

pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))

class ComplexCLI(click.Group):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, cmd_name):
        try:
            mod = __import__(f"portainer.commands.cmd_{cmd_name}", None, None, ["cli"])
        except ImportError as e:
            print(f"Error: {cmd_name} is not a valid command! - detail: {e}", file=sys.stderr)
            return
        return mod.cli

@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@click.option("-U", "--url", envvar='API_URL', required=True, type=click.STRING, help="Portainer API URL. ex. https://example.tld/api")
@click.option("-u", "--user", envvar='API_USER', required=False, type=click.STRING, help="Portainer API username (not needed if using --token).")
@click.option("-p", "--password", envvar='API_PASSWORD', required=False, type=click.STRING, help="Portainer API password (not needed if using --token).")
@click.option("-t", "--token", envvar='API_TOKEN', required=False, type=click.STRING, help="Portainer API access token (alternative to user/password).")
@pass_environment
def cli(ctx, verbose, url, user, password, token):
    ctx.logger.debug("init cmd")
    if verbose:
        ctx.setLogLevel(logging.DEBUG)

    # Validate authentication options
    if token:
        ctx.portainer_client = PortainerAPI(ctx, url, token=token)
    elif user and password:
        ctx.portainer_client = PortainerAPI(ctx, url, username=user, password=password)
    else:
        raise click.UsageError("Either --token or both --user and --password are required.")
