from portainer.cli import pass_environment

import click


@click.command("endpoints-list", short_help="Get Portainer endpoints list.")
@pass_environment
def cli(ctx):
    endpoints = ctx.portainer_client.endpoints_list()
    for endpoint in endpoints:
        ctx.logger.info(f"{endpoint['Id']},{endpoint['Name']}")
