from portainer.cli import pass_environment
import click

@click.command("volume-delete", short_help="Deletes a volume in a Portainer endpoint.")
@click.option("-e", "--endpoint-id", required=True, type=click.INT, help="Portainer Endpoint ID")
@click.option("-n", "--volume-name", required=True, type=click.STRING, help="Name of the volume to delete.")
@pass_environment
def cli(ctx, endpoint_id, volume_name):
    """Executes the command to delete a volume for a given endpoint."""

    # Call the delete_volume method with the provided endpoint_id and volume_name
    response = ctx.portainer_client.delete_volume(endpoint_id, volume_name)

    # Check the response status code to determine if the deletion was successful
    if response.status_code == 204:
        ctx.logger.info(f"Volume '{volume_name}' deleted successfully.")
    else:
        # Assuming the delete_volume method returns detailed error messages
        error_message = response.json().get('message', 'Unknown error')
        ctx.logger.error(f"Failed to delete volume '{volume_name}'. Error: {error_message}")
