# Portainer CLI

CLI tool for managing Portainer stacks, volumes, and endpoints.

## Installation

```bash
pip install --editable .
```

## Authentication

Two authentication methods are supported:

### 1. API Token (Recommended)

```bash
portainer -U https://portainer.example.io/api -t YOUR_API_TOKEN stack-list
```

Or via environment variable:
```bash
export PORTAINER_API_URL=https://portainer.example.io/api
export PORTAINER_API_TOKEN=YOUR_API_TOKEN
portainer stack-list
```

To create an API token: Portainer UI > My account > Access tokens > Add access token

### 2. Username/Password

```bash
portainer -U https://portainer.example.io/api -u admin -p password stack-list
```

Or via environment variables:
```bash
export PORTAINER_API_URL=https://portainer.example.io/api
export PORTAINER_API_USER=admin
export PORTAINER_API_PASSWORD=password
portainer stack-list
```

## Usage

```bash
portainer --help
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

## Docker Usage

```bash
docker run --rm --network host registry.nexiona.io/internal/portainer-cli --help
```

## Development

```bash
pipreqs . --force
pip install --editable .
```
