from portainer.cli import pass_environment
import click

@click.command("volume-create", short_help="Creates a new volume in a Portainer endpoint.")
@click.option("-e", "--endpoint-id", required=True, type=click.INT, help="Portainer Endpoint ID")
@click.option("-n", "--volume-name", required=True, type=click.STRING, help="Name of the volume to create.")
@pass_environment
def cli(ctx, endpoint_id, volume_name):
    """Executes the command to create a new volume for a given endpoint."""
    
    # Call the create_volume method with the provided endpoint_id and volume_name
    response = ctx.portainer_client.create_volume(endpoint_id, volume_name)

    # Assuming the create_volume method returns a requests.Response object
    if ( response.status_code == 201 or response.status_code == 200):
        ctx.logger.info(f"Volume '{volume_name}' created successfully.")
    else:
        error_message = response.json().get('message', 'Unknown error')
        ctx.logger.error(f"Failed to create volume '{volume_name}'. Error: {error_message}")
