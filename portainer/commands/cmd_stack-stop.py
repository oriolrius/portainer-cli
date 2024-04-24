from portainer.cli import pass_environment

import click


@click.command("stack-stop", short_help="Stop Portainer stack.")
@click.option("-e", "--endpoint-id", envvar='ENDPOINT_ID', required=True, type=click.INT, help="Portainer Endpoint ID")
@click.option("-s", "--stack-id", envvar='STACK_ID', required=True, type=click.INT, help="Portainer Stack ID")
@pass_environment
def cli(ctx, endpoint_id, stack_id):
    status = ctx.portainer_client.stack_stop(stack_id, endpoint_id)
    ctx.logger.info(f"Name: {status['Name']} - Status: {status['Status']}")
