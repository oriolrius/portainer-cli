from portainer.cli import pass_environment
import click

@click.command("volume-prune", short_help="Deletes all volumes in a Portainer endpoint.")
@click.option("-e", "--endpoint-id", required=True, type=click.INT, help="Portainer Endpoint ID")
@click.option("--dry-mode", type=bool, default=True, help="Set to False to actually remove the volumes.")
@pass_environment
def cli(ctx, endpoint_id, dry_mode):
    """Executes the command to delete all volumes for a given endpoint or just list them if in dry mode."""
    
    # First, list all volumes in the endpoint
    volumes = ctx.portainer_client.get_volumes(endpoint_id)

    if 'Volumes' in volumes and volumes['Volumes']:
        volume_names = [volume['Name'] for volume in volumes['Volumes']]
        
        # If dry_mode is True, just list the volumes that would be deleted
        if dry_mode:
            ctx.logger.info("Volumes that would be deleted (***DRY MODE***):")
            for name in volume_names:
                ctx.logger.info(f"Volume: {name}")
            ctx.logger.info("*** No volumes have been deleted. Use parameter --dry-mode False for actual deletion. ***")
        else:
            # Delete each volume since dry_mode is False
            for volume_name in volume_names:
                response = ctx.portainer_client.delete_volume(endpoint_id, volume_name)
                if response.status_code == 204:
                    ctx.logger.info(f"Volume '{volume_name}' deleted successfully.")
                else:
                    error_message = response.json().get('message', 'Unknown error')
                    ctx.logger.error(f"Failed to delete volume '{volume_name}'. Error: {error_message}")
            ctx.logger.info("*** All selected volumes have been pruned. ***")
    else:
        ctx.logger.info("No volumes found for the specified endpoint.")
