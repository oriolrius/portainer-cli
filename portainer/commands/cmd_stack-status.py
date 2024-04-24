from portainer.cli import pass_environment

import click


@click.command("stack-status", short_help="Shows Portainer stack status.")
@click.option("-s", "--stack-id", envvar='STACK_ID', required=True, type=click.INT, help="Portainer Stack ID")
@pass_environment
def cli(ctx, stack_id):
    status = ctx.portainer_client.stack_status(stack_id)
    ctx.logger.info(f"Name: {status['Name']} - Status: {status['Status']}")
