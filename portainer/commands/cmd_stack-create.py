from portainer.cli import pass_environment
from portainer.libs import read_env_file, read_file_content
import click

@click.command("stack-create", short_help="Create a Portainer stack.")
@click.option("-m", "--stack_name", envvar='STACK_NAME', required=True, type=click.STRING, help="Portainer Stack Name")
@click.option("-e", "--endpoint-id", envvar='ENDPOINT_ID', required=True, type=click.INT, help="Portainer Endpoint ID")
@click.option("-n", "--env-file", envvar='ENV_FILE', required=True, type=click.STRING, help=".env file for docker-compose.yml")
@click.option("-s", "--stack-file", envvar='STACK_FILE', required=True, type=click.STRING, help="docker-compose.yml file")
@pass_environment
def cli(ctx, stack_name, endpoint_id, env_file, stack_file):
    env_vars = read_env_file(env_file)
    ctx.logger.debug(f"env_vars: {env_vars}")
    stack_file_content = read_file_content(stack_file)
    ctx.logger.debug(f"stack_file_content: {stack_file_content}")
    status = ctx.portainer_client.stack_create(
        endpoint_id,
        stack_name,
        env_vars,
        stack_file_content
        )
    ctx.logger.info(f"Name: {status['Name']} - Status: {status['Status']} - Id: {status['Id']}")
