# Portainer CLI

CLI tool for managing Portainer stacks, volumes, and endpoints.

## Installation

```bash
uv sync
```

## Authentication

Two authentication methods are supported:

### 1. API Token (Recommended)

```bash
uv run portainer -U https://portainer.example.com/api -t YOUR_API_TOKEN stack-list
```

Or via environment variable:
```bash
export PORTAINER_API_URL=https://portainer.example.com/api
export PORTAINER_API_TOKEN=YOUR_API_TOKEN
uv run portainer stack-list
```

To create an API token: Portainer UI > My account > Access tokens > Add access token

### 2. Username/Password

```bash
uv run portainer -U https://portainer.example.com/api -u admin -p password stack-list
```

Or via environment variables:
```bash
export PORTAINER_API_URL=https://portainer.example.com/api
export PORTAINER_API_USER=admin
export PORTAINER_API_PASSWORD=password
uv run portainer stack-list
```

## Usage

```bash
uv run portainer --help
```

### Available Commands

- `endpoints-list` - List available endpoints
- `stack-list` - List stacks
- `stack-status` - Get stack status
- `stack-create` - Create a new stack from local files
- `stack-create-git` - Create a new stack from Git repository
- `stack-start` - Start a stack
- `stack-stop` - Stop a stack
- `stack-delete` - Delete a stack
- `volume-list` - List volumes
- `volume-create` - Create a volume
- `volume-delete` - Delete a volume
- `volume-prune` - Delete volumes (with dry-mode)

### Create Stack from Git Repository

```bash
# Public repository
uv run portainer stack-create-git -n mystack -e 1 \
  -r https://github.com/user/repo

# Private repository with authentication
uv run portainer stack-create-git -n mystack -e 1 \
  -r https://github.com/user/repo \
  --git-username user --git-token ghp_xxxx

# With environment variables and auto-update
uv run portainer stack-create-git -n mystack -e 1 \
  -r https://github.com/user/repo \
  --env "DB_HOST=localhost" --env "DB_PORT=5432" \
  --env-file .env \
  --auto-update --auto-update-interval 10m
```

## Quick Usage (without cloning)

### Using uvx (recommended)

```bash
# Run directly without installation
uvx --from git+https://github.com/oriolrius/portainer-cli portainer --help

# Run specific version
uvx --from git+https://github.com/oriolrius/portainer-cli@v2.1.0 portainer --help

# Example: list endpoints
uvx --from git+https://github.com/oriolrius/portainer-cli portainer \
  -U https://portainer.example.com/api -t YOUR_API_TOKEN endpoints-list
```

### Using pip

```bash
# Install directly from GitHub
pip install git+https://github.com/oriolrius/portainer-cli.git

# Then run
portainer --help
```

## Docker Usage

```bash
docker run --rm --network host ghcr.io/oriolrius/portainer-cli --help

# With environment variables
docker run --rm --network host \
  -e PORTAINER_API_URL=https://portainer.example.com/api \
  -e PORTAINER_API_TOKEN=YOUR_TOKEN \
  ghcr.io/oriolrius/portainer-cli stack-list
```

## Development

```bash
uv sync
uv run portainer --help
```

## License

MIT
