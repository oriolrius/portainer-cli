from portainer.cli import pass_environment

import click


@click.command("stack-delete", short_help="Delete Portainer stack.")
@click.option("-e", "--endpoint-id", envvar='ENDPOINT_ID', required=True, type=click.INT, help="Portainer Endpoint ID")
@click.option("-s", "--stack-id", envvar='STACK_ID', required=True, type=click.INT, help="Portainer Stack ID")
@pass_environment
def cli(ctx, endpoint_id, stack_id):
    ctx.portainer_client.stack_delete(
        stack_id,
        endpoint_id
        )
    ctx.logger.info(f"Stack ID: {stack_id} deleted")
