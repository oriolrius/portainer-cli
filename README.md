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
- `stack-create` - Create a new stack
- `stack-start` - Start a stack
- `stack-stop` - Stop a stack
- `stack-delete` - Delete a stack
- `volume-list` - List volumes
- `volume-create` - Create a volume
- `volume-delete` - Delete a volume
- `volume-prune` - Delete volumes (with dry-mode)

## Quick Usage (without cloning)

### Using pip with SSH

```bash
# Install directly from repository
pip install git+ssh://git@github.com/YOUR-ORG/portainer-cli.git@v2.0.0

# Then run
portainer --help
```

### Using pipx (isolated environment)

```bash
# Install in isolated environment
pipx install git+ssh://git@github.com/YOUR-ORG/portainer-cli.git@v2.0.0

# Then run
portainer -U https://portainer.example.com/api -t YOUR_API_TOKEN endpoints-list
```

## Docker Usage

```bash
docker run --rm --network host your-registry/portainer-cli --help
```

## Development

```bash
uv sync
uv run portainer --help
```

## License

MIT
