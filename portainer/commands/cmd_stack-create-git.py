from portainer.cli import pass_environment
from portainer.libs import read_env_file
import click


@click.command("stack-create-git", short_help="Create a Portainer stack from a Git repository.")
@click.option("-n", "--name", "stack_name", envvar='STACK_NAME', required=True, type=click.STRING,
              help="Stack name")
@click.option("-e", "--endpoint-id", envvar='ENDPOINT_ID', required=True, type=click.INT,
              help="Portainer Endpoint ID")
@click.option("-r", "--repo-url", envvar='REPO_URL', required=True, type=click.STRING,
              help="Git repository URL (HTTPS)")
@click.option("-b", "--branch", envvar='REPO_BRANCH', default="refs/heads/main", type=click.STRING,
              help="Git branch/tag reference (default: refs/heads/main)")
@click.option("-c", "--compose-path", envvar='COMPOSE_PATH', default="docker-compose.yml", type=click.STRING,
              help="Path to docker-compose.yml in repository (default: docker-compose.yml)")
@click.option("--env-file", envvar='ENV_FILE', type=click.STRING,
              help="Path to .env file for stack environment variables")
@click.option("--env", "env_vars", multiple=True, type=click.STRING,
              help="Environment variable in KEY=VALUE format (can be used multiple times)")
@click.option("--git-username", envvar='GIT_USERNAME', type=click.STRING,
              help="Git username for private repository authentication")
@click.option("--git-token", envvar='GIT_TOKEN', type=click.STRING,
              help="Git password/token for private repository authentication")
@click.option("--auto-update", is_flag=True, default=False,
              help="Enable GitOps auto-update via polling")
@click.option("--auto-update-interval", default="5m", type=click.STRING,
              help="Auto-update polling interval (default: 5m)")
@click.option("--webhook", is_flag=True, default=False,
              help="Enable webhook-based updates")
@click.option("--tls-skip-verify", is_flag=True, default=False,
              help="Skip TLS certificate verification for Git")
@pass_environment
def cli(ctx, stack_name, endpoint_id, repo_url, branch, compose_path, env_file,
        env_vars, git_username, git_token, auto_update, auto_update_interval,
        webhook, tls_skip_verify):
    """Create a Portainer stack from a Git repository.

    Examples:

    \b
    # Create stack from public repo
    portainer stack-create-git -n mystack -e 1 -r https://github.com/user/repo

    \b
    # Create stack from private repo with authentication
    portainer stack-create-git -n mystack -e 1 -r https://github.com/user/repo \\
        --git-username user --git-token ghp_xxx

    \b
    # Create stack with environment variables
    portainer stack-create-git -n mystack -e 1 -r https://github.com/user/repo \\
        --env "DB_HOST=localhost" --env "DB_PORT=5432"

    \b
    # Create stack with .env file and auto-update enabled
    portainer stack-create-git -n mystack -e 1 -r https://github.com/user/repo \\
        --env-file .env --auto-update --auto-update-interval 10m
    """
    # Build environment variables list
    env_list = []

    # Load from .env file if provided
    if env_file:
        file_env_vars = read_env_file(env_file)
        env_list.extend(file_env_vars)
        ctx.logger.debug(f"Loaded {len(file_env_vars)} env vars from {env_file}")

    # Add inline environment variables
    for env_var in env_vars:
        if "=" in env_var:
            key, value = env_var.split("=", 1)
            env_list.append({"name": key, "value": value})
        else:
            ctx.logger.warning(f"Skipping invalid env var (missing '='): {env_var}")

    ctx.logger.debug(f"Total env vars: {len(env_list)}")

    # Create the stack
    status = ctx.portainer_client.stack_create_git(
        endpoint_id=endpoint_id,
        stack_name=stack_name,
        repo_url=repo_url,
        repo_ref=branch,
        compose_path=compose_path,
        env_vars=env_list,
        repo_username=git_username,
        repo_password=git_token,
        auto_update=auto_update,
        auto_update_interval=auto_update_interval,
        auto_update_webhook=webhook,
        tls_skip_verify=tls_skip_verify,
    )

    ctx.logger.info(f"Stack created - Name: {status['Name']} - Status: {status['Status']} - Id: {status['Id']}")

    # Show webhook URL if enabled
    if webhook and status.get('AutoUpdate', {}).get('Webhook'):
        ctx.logger.info(f"Webhook URL: {status['AutoUpdate']['Webhook']}")
