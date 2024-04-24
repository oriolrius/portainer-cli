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
@click.option("-u", "--user", envvar='API_USER', required=True, type=click.STRING, help="Portainer API username.")
@click.option("-p", "--password", envvar='API_PASSWORD', required=True, type=click.STRING, help="Portainer API password")
@pass_environment
def cli(ctx, verbose, url, user, password):
    ctx.logger.debug("init cmd")
    if verbose:
        ctx.setLogLevel(logging.DEBUG)

    ctx.portainer_client = PortainerAPI(ctx, url, user, password)
