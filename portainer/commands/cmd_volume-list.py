from portainer.cli import pass_environment
import click
import json

@click.command("volume-list", short_help="Lists volumes in a Portainer endpoint.")
@click.option("-e", "--endpoint-id", envvar='ENDPOINT_ID', required=True, type=click.INT, help="Portainer Endpoint ID")
@click.option("-f", "--filter", default="{}", help="JSON string for filtering volumes based on name, driver, or labels.")
@click.option("-s", "--short", is_flag=True, help="Display only volume names and driver.")
@pass_environment
def cli(ctx, endpoint_id, filter, short):
    """Executes the command to list all volumes for a given endpoint, with optional filters."""
    # Parse the filter JSON string into a Python dictionary
    try:
        filters = json.loads(filter)
    except json.JSONDecodeError:
        ctx.logger.error("Invalid JSON format for filter.")
        return

    volumes = ctx.portainer_client.get_volumes(endpoint_id, filter=filters)

    if 'Volumes' in volumes:
        ctx.logger.info("Listing Volumes:")
        if len(volumes['Volumes']) < 1:
            ctx.logger.info(f">>> No volumes found for endpoint: {endpoint_id}")
        for volume in volumes['Volumes']:
            if short:
                ctx.logger.info(f" {volume['Name']} ({volume['Driver']})")
            else:
              ctx.logger.info(f"Name: {volume['Name']}")
              ctx.logger.info(f"Driver: {volume['Driver']}")
              ctx.logger.info(f"Mountpoint: {volume['Mountpoint']}")
              ctx.logger.info(f"Scope: {volume['Scope']}")
              ctx.logger.info(f"CreatedAt: {volume.get('CreatedAt', 'N/A')}")
              ctx.logger.info(f"ResourceID: {volume.get('ResourceID', 'N/A')}")

              if volume.get('Labels'):
                  labels = "\n " + "\n ".join([f"{k}: {v}" for k, v in volume['Labels'].items()])
                  ctx.logger.info(f"Labels: {labels}")
              else:
                  ctx.logger.info("Labels: None")

              if volume.get('Options'):
                  options = "\n " + "\n ".join([f"{k}: {v}" for k, v in volume['Options'].items()])
                  ctx.logger.info(f"Options: {options}")
              else:
                  ctx.logger.info("Options: None")
              ctx.logger.info("--")
    else:
        ctx.logger.info("No volumes found for the specified endpoint.")
