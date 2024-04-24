from portainer.cli import pass_environment

import click


@click.command("stack-list", short_help="Shows Portainer stack status.")
@click.option("-e", "--endpoint-id", envvar='ENDPOINT_ID', required=False, type=click.INT, help="Portainer Endpoint ID")
@pass_environment
def cli(ctx, endpoint_id):
    stacks = ctx.portainer_client.stack_list(endpoint_id)
    
    ctx.logger.info("StackId,Name,Status,EndpointId")

    for stack in stacks:
        ctx.logger.info(f"{stack['Id']},{stack['Name']},{stack['Status']},{stack['EndpointId']}")
