import sys
import requests

class PortainerAPI(object):
    def __init__(self, ctx, url, username=None, password=None, token=None):
        """Initialize Portainer API client.

        Supports two authentication methods:
        1. Username/Password: Uses /auth endpoint to get JWT token
        2. API Token: Uses X-API-Key header (recommended for automation)

        :param ctx: Context object with logger
        :param url: Portainer API URL (e.g., https://example.tld/api)
        :param username: Portainer username (for username/password auth)
        :param password: Portainer password (for username/password auth)
        :param token: Portainer API access token (alternative to username/password)
        """
        self.ctx = ctx
        self.url = url
        self.username = username
        self.password = password
        self.api_token = token  # API access token (X-API-Key)
        self.jwt_token = None   # JWT token from /auth
        self.timeout = 300

        if not self.api_token:
            self.login()

    def _authz(self):
        """Return authorization headers based on authentication method."""
        if self.api_token:
            return {"X-API-Key": self.api_token}
        return {"Authorization": f"Bearer {self.jwt_token}"}

    def _get(self, url, **headers):
        r = requests.get(
            url,
            headers={**self._authz(), **headers},
            timeout=self.timeout,
        )
        if r.status_code != 200:
            self.ctx.logger.error(f"URL: {url} - {r.status_code} {r.text}")
            sys.exit(1)
        else:
            self.ctx.logger.debug(f"URL: {url} - {r.status_code} {r.text}")

        return r

    def _post(self, url, params, payload, **headers):
        r = requests.post(
            url,
            params=params,
            json=payload,
            headers={**self._authz(), **headers},
            timeout=self.timeout,
        )
        if r.status_code != 200:
            self.ctx.logger.error(f"URL: {url} - {r.status_code} {r.text}")
            sys.exit(1)
        else:
            self.ctx.logger.debug(f"URL: {url} - {r.status_code} {r.text}")

        return r

    def _delete(self, url, params, **headers):
        r = requests.delete(
            url,
            params=params,
            headers={**self._authz(), **headers},
            timeout=self.timeout,
        )
        if r.status_code != 204: # OK and no content returned
            self.ctx.logger.error(f"URL: {url} - {r.status_code} {r.text}")
            sys.exit(1)
        else:
            self.ctx.logger.debug(f"URL: {url} - {r.status_code} {r.text}")

        return r

    def login(self):
        """Authenticate using username/password to obtain JWT token."""
        self.ctx.logger.debug(f"Logging in to {self.url} as {self.username}...")
        response = requests.post(
            f"{self.url}/auth",
            json={"Username": self.username, "Password": self.password},
            timeout=self.timeout,
        )
        if response.status_code != 200:
            self.ctx.logger.error(f"Login failed: {response.status_code} {response.text}")
            sys.exit(1)

        self.ctx.logger.debug(f"Login successful: {response.status_code}")
        self.jwt_token = response.json()["jwt"]

    def stack_status(self, stack_id):
        self.ctx.logger.debug(f"Getting stack status stack_id: {stack_id}")
        response = self._get(f"{self.url}/stacks/{stack_id}")
        self.ctx.logger.debug(f"Stack status: {response.status_code} {response.text}")

        return response.json()

    def stack_stop(self, stack_id, endpoint_id):
        self.ctx.logger.debug(f"Stopping stack stack_id: {stack_id} - endpoint_id: {endpoint_id}")
        payload = {
            "id": stack_id,
            "endpointId": endpoint_id, 
            }
        params = {
            "endpointId": endpoint_id,
        }
        response = self._post(
            f"{self.url}/stacks/{stack_id}/stop",
            params,
            payload
            )
        self.ctx.logger.debug(f"Stack stopped: {response.status_code} {response.text}")

        return response.json()

    def stack_start(self, stack_id, endpoint_id):
        self.ctx.logger.debug(f"Starting stack stack_id: {stack_id} - endpoint_id: {endpoint_id}")
        payload = {
            "id": stack_id,
            "endpointId": endpoint_id, 
            }
        params = {
            "endpointId": endpoint_id,
        }
        response = self._post(
            f"{self.url}/stacks/{stack_id}/start",
            params,
            payload
            )
        self.ctx.logger.debug(f"Stack started: {response.status_code} {response.text}")

        return response.json()

    def stack_create(self, endpoint_id, stack_name, env_vars, stack_file_content):
        self.ctx.logger.debug(f"Creating stack_name: {stack_name} - endpoint_id: {endpoint_id}")
        payload = {
            "method": "string",
            "type": "standalone",
            "Name": stack_name,
            "Env": env_vars,
            "StackFileContent": stack_file_content,
            }
        params = {
            "endpointId": endpoint_id,
        }
        self.ctx.logger.debug(f"payload: {payload}")
        response = self._post(
            f"{self.url}/stacks/create/standalone/string",
            params,
            payload
            )
        self.ctx.logger.debug(f"Stack started: {response.status_code} {response.text}")

        return response.json()

    def stack_delete(self, stack_id, endpoint_id):
        self.ctx.logger.debug(f"Deleting stack stack_id: {stack_id} - endpoint_id: {endpoint_id}")
        params = {
            "endpointId": endpoint_id,
            "external": "false", 
            }
        response = self._delete(
            f"{self.url}/stacks/{stack_id}",
            params
            )
        self.ctx.logger.debug(f"Stack deleted; HTTP response: {response.status_code} - OK with no content returned.")

        return response

    def stack_list(self, endpoint_id):
        self.ctx.logger.debug(f"Getting stack list of the endpoint_id: {endpoint_id}")
        response = self._get(f"{self.url}/stacks")
        if not endpoint_id:
            self.ctx.logger.debug(f"Returning full stack list: {response.status_code} {response.text}")
            return response.json()

        buf = []
        self.ctx.logger.debug(f"Stack list: {response.status_code} {response.text}")
        for stack in response.json():
            if int(stack['EndpointId']) == int(endpoint_id):
                buf.append(stack)
                self.ctx.logger.debug(f"Adding stack {stack['Id']} to the list.")

        return buf

    def endpoints_list(self):
        self.ctx.logger.debug("Getting endpoints list")
        response = self._get(f"{self.url}/endpoints")
        self.ctx.logger.debug(f"Endpoints list: {response.status_code} {response.text}")

        return response.json()

    def get_volumes(self, endpoint_id, volume_name=None, filter={}):
        """Retrieves details of a specific volume or all volumes in an endpoint.

        :param endpoint_id: The ID of the endpoint.
        :param volume_name: The name of the volume to retrieve. If None, retrieves all volumes.
        :param filter: A dictionary of filters to apply to the volume list.
          filter: {
            "name": regex(str),
            "label_name": str,
            "label_value": regex(str),
          }
        :return: JSON response containing volume details.
        """
        if volume_name:
            self.ctx.logger.debug(f"Retrieving details for volume: {volume_name} in endpoint: {endpoint_id}")
            response = self._get(f"{self.url}/endpoints/{endpoint_id}/docker/volumes/{volume_name}")
        else:
            self.ctx.logger.debug(f"Retrieving list of all volumes in endpoint: {endpoint_id}")
            response = self._get(f"{self.url}/endpoints/{endpoint_id}/docker/volumes")

        if response.status_code in [200, 201]:
            self.ctx.logger.debug(f"Volume information retrieved successfully: {response.json()}")
            if (filter):
                self.ctx.logger.debug(f"Applying filters: {filter}")
                volumes = response.json().get("Volumes", [])
                volumes_num = len(volumes)
                import re
                for key, value in filter.items():
                    if key == "name":
                        volumes = [volume for volume in volumes if re.match(value, volume["Name"])]
                    elif key == "label_name":
                        volumes = [volume for volume in volumes if value in volume["Labels"]]
                    elif key == "label_value":
                        volumes = [volume for volume in volumes if re.match(value, volume["Labels"])]
                self.ctx.logger.debug(f"Filtered {volumes_num} volumes to {len(volumes)} volumes.")
                return { "Volumes": volumes }
        else:
            self.ctx.logger.error(f"Failed to retrieve volume information. HTTP response: {response.status_code} - {response.text}")
        
        return response.json()

    def create_volume(self, endpoint_id, volume_name):
        """Creates a new volume with the given name. Only local volumes are supported.
        
        :param endpoint_id: The ID of the endpoint.
        :param volume_name: The name of the volume to create.
        :return: JSON response containing volume details.
        """
        self.ctx.logger.debug(f"Creating volume: {volume_name} in endpoint: {endpoint_id}")
        payload = {
            "Name": volume_name,
            "Driver": "local",
            "DriverOpts": {}
        }
        return self._post(
            f"{self.url}/endpoints/{endpoint_id}/docker/volumes/create",
            params={},
            payload=payload
        )

    def delete_volume(self, endpoint_id, volume_name):
        """Deletes a specified volume.
        
        :param endpoint_id: The ID of the endpoint.
        :param volume_name: The name of the volume to delete.
        :return: JSON response containing volume details.
        """
        self.ctx.logger.debug(f"Deleting volume: {volume_name} in endpoint: {endpoint_id}")
        response = self._delete(
            f"{self.url}/endpoints/{endpoint_id}/docker/volumes/{volume_name}",
            params={}
        )
        if response.status_code == 204:
            self.ctx.logger.debug("Volume deleted successfully.")
        else:
            self.ctx.logger.error(f"Failed to delete volume: {volume_name}. HTTP response: {response.status_code} - {response.text}")
        return response

