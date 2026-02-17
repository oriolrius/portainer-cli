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
uv run portainer -U https://portainer.example.io/api -t YOUR_API_TOKEN stack-list
```

Or via environment variable:
```bash
export PORTAINER_API_URL=https://portainer.example.io/api
export PORTAINER_API_TOKEN=YOUR_API_TOKEN
uv run portainer stack-list
```

To create an API token: Portainer UI > My account > Access tokens > Add access token

### 2. Username/Password

```bash
uv run portainer -U https://portainer.example.io/api -u admin -p password stack-list
```

Or via environment variables:
```bash
export PORTAINER_API_URL=https://portainer.example.io/api
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

## Quick Usage with uvx

Run directly without installation using `uvx`:

```bash
# From GitLab (latest)
uvx --from git+https://gitlab.com/nexiona/infrastructre/portainer-cli portainer --help

# From specific tag
uvx --from git+https://gitlab.com/nexiona/infrastructre/portainer-cli@v2.0.0 portainer --help

# Example: list endpoints
uvx --from git+https://gitlab.com/nexiona/infrastructre/portainer-cli portainer \
  -U https://portainer.example.io/api -t YOUR_API_TOKEN endpoints-list
```

## Docker Usage

```bash
docker run --rm --network host registry.nexiona.io/internal/portainer-cli --help
```

## Development

```bash
uv sync
uv run portainer --help
```
