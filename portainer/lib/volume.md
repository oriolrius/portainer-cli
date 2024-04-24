how to create a table of contents for this document


# get volumes

```bash
curl 'https://portainer.nexiona.io/api/endpoints/30/docker/volumes?filters=%7B%22dangling%22:%5B%22true%22%5D%7D' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'cookie: portainer_api_key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQsInVzZXJuYW1lIjoib3Jpb2wucml1cyIsInJvbGUiOjEsInNjb3BlIjoiZGVmYXVsdCIsImZvcmNlQ2hhbmdlUGFzc3dvcmQiOmZhbHNlLCJleHAiOjE3MTI2NzgxOTMsImlhdCI6MTcxMjY0OTM5M30.57qC57MMV0cZ-rpcrrJ7vuoD7AwmvvO-fsm3dJGIRpI; _gorilla_csrf=MTcxMjY0OTM5M3xJblp4YTA1RFQxbENUMVJFT1ZBNVZ6TmtUekk0VW1kQmNGWm5hWEI2V0ZWUmJraFRVR1ozWlZBMFVHczlJZ289fJAfz_iWdO5PZ3UmQ9Gxe5MwHam-cd7_fHtCRzwpSb6D' \
  -H 'pragma: no-cache' \
  -H 'referer: https://portainer.nexiona.io/' \
  -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  -H 'x-csrf-token: u7CLt6YsBKuaEFSCiGaWF7hqeauF2WsQ7Hn15ZdgH+AFGYa/QC09m2cvgTX8iypRuEMvoywUHgBwDXqakO//GQ=='
```

```json
{
    "Volumes": [
        {
            "CreatedAt": "2023-09-28T11:43:01+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/8d4b323fac1048ddeb52214ecfeb12c802deac1df81f2a9435920687fc6b4434/_data",
            "Name": "8d4b323fac1048ddeb52214ecfeb12c802deac1df81f2a9435920687fc6b4434",
            "Options": null,
            "ResourceID": "8d4b323fac1048ddeb52214ecfeb12c802deac1df81f2a9435920687fc6b4434_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-06-22T17:02:13+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_database-data/_data",
            "Name": "miimetiq_database-data",
            "Options": null,
            "ResourceID": "miimetiq_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:27:51+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_03",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_03_message-broker-data/_data",
            "Name": "miimetiq_test_03_message-broker-data",
            "Options": null,
            "ResourceID": "miimetiq_test_03_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:24:20+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04env",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04env_message-broker-data/_data",
            "Name": "miimetiq_test_04env_message-broker-data",
            "Options": null,
            "ResourceID": "miimetiq_test_04env_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:27:51+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_03",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_03_traefik-certificates/_data",
            "Name": "miimetiq_test_03_traefik-certificates",
            "Options": null,
            "ResourceID": "miimetiq_test_03_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:22:17+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_2",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_2_traefik-certificates/_data",
            "Name": "testing_server_2_traefik-certificates",
            "Options": null,
            "ResourceID": "testing_server_2_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T17:42:11+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/7cfd9d9703934330cfd6101131e41507c655ad0e0aa137ae8e5cbd0a26f9e579/_data",
            "Name": "7cfd9d9703934330cfd6101131e41507c655ad0e0aa137ae8e5cbd0a26f9e579",
            "Options": null,
            "ResourceID": "7cfd9d9703934330cfd6101131e41507c655ad0e0aa137ae8e5cbd0a26f9e579_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-04T15:36:18+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/937a4401d81fb826b91edacd42656427f4c37b5a50798b9f46c277d9583781de/_data",
            "Name": "937a4401d81fb826b91edacd42656427f4c37b5a50798b9f46c277d9583781de",
            "Options": null,
            "ResourceID": "937a4401d81fb826b91edacd42656427f4c37b5a50798b9f46c277d9583781de_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:12+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-master",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-master_message-broker-data/_data",
            "Name": "miimetiq-master_message-broker-data",
            "Options": null,
            "ResourceID": "miimetiq-master_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-06-22T17:02:13+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_miimetiq-schemas/_data",
            "Name": "miimetiq_miimetiq-schemas",
            "Options": null,
            "ResourceID": "miimetiq_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T18:07:22+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_4",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_4_traefik-certificates/_data",
            "Name": "testing_server_4_traefik-certificates",
            "Options": null,
            "ResourceID": "testing_server_4_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-04-04T16:22:56+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/913b421df18f98ac637c50cb0c0e29502884ec261e04a3eab8463aa24ed3656c/_data",
            "Name": "913b421df18f98ac637c50cb0c0e29502884ec261e04a3eab8463aa24ed3656c",
            "Options": null,
            "ResourceID": "913b421df18f98ac637c50cb0c0e29502884ec261e04a3eab8463aa24ed3656c_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:01:49+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-test01",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-test01_miimetiq-schemas/_data",
            "Name": "miimetiq-test01_miimetiq-schemas",
            "Options": null,
            "ResourceID": "miimetiq-test01_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:31:10+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/e5de9d855d3ebd1e520da466c519ed8fe30612141d125788aa606ff73297b392/_data",
            "Name": "e5de9d855d3ebd1e520da466c519ed8fe30612141d125788aa606ff73297b392",
            "Options": null,
            "ResourceID": "e5de9d855d3ebd1e520da466c519ed8fe30612141d125788aa606ff73297b392_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T12:25:27+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/9c7addf1c34d0f91a59af1345ad5c44eaa0741154539944422d8c236b49162ba/_data",
            "Name": "9c7addf1c34d0f91a59af1345ad5c44eaa0741154539944422d8c236b49162ba",
            "Options": null,
            "ResourceID": "9c7addf1c34d0f91a59af1345ad5c44eaa0741154539944422d8c236b49162ba_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:22:16+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_2",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_2_influx-database-data/_data",
            "Name": "testing_server_2_influx-database-data",
            "Options": null,
            "ResourceID": "testing_server_2_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:52+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-2_7rc",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-2_7rc_traefik-certificates/_data",
            "Name": "miimetiq-2_7rc_traefik-certificates",
            "Options": null,
            "ResourceID": "miimetiq-2_7rc_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:44:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04_influx-database-data/_data",
            "Name": "miimetiq_test_04_influx-database-data",
            "Options": null,
            "ResourceID": "miimetiq_test_04_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:44:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04_message-broker-data/_data",
            "Name": "miimetiq_test_04_message-broker-data",
            "Options": null,
            "ResourceID": "miimetiq_test_04_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T18:07:22+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_4",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_4_database-data/_data",
            "Name": "testing_server_4_database-data",
            "Options": null,
            "ResourceID": "testing_server_4_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:57:20+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/a77bdc41ce3d241cf004624fe243d651ed57413565727b2c692f9f12b4c2b75b/_data",
            "Name": "a77bdc41ce3d241cf004624fe243d651ed57413565727b2c692f9f12b4c2b75b",
            "Options": null,
            "ResourceID": "a77bdc41ce3d241cf004624fe243d651ed57413565727b2c692f9f12b4c2b75b_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T13:00:05+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/950e059c4fe36f36701bd86f60be5e8361c98497ce2a3fdf4373abcfa9d9bb7b/_data",
            "Name": "950e059c4fe36f36701bd86f60be5e8361c98497ce2a3fdf4373abcfa9d9bb7b",
            "Options": null,
            "ResourceID": "950e059c4fe36f36701bd86f60be5e8361c98497ce2a3fdf4373abcfa9d9bb7b_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T17:52:35+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/4892b564e0f496519d425d2470af2579a808b19f7fa239e09406d312cadd2564/_data",
            "Name": "4892b564e0f496519d425d2470af2579a808b19f7fa239e09406d312cadd2564",
            "Options": null,
            "ResourceID": "4892b564e0f496519d425d2470af2579a808b19f7fa239e09406d312cadd2564_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-04T15:43:43+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/f3edd660e3c27ffaeac3afc85113dbd130700bc4ccebb70f2e02f3a4e2c5646f/_data",
            "Name": "f3edd660e3c27ffaeac3afc85113dbd130700bc4ccebb70f2e02f3a4e2c5646f",
            "Options": null,
            "ResourceID": "f3edd660e3c27ffaeac3afc85113dbd130700bc4ccebb70f2e02f3a4e2c5646f_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T16:29:50+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-2_7rc",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "graphite-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-2_7rc_graphite-database-data/_data",
            "Name": "miimetiq-2_7rc_graphite-database-data",
            "Options": null,
            "ResourceID": "miimetiq-2_7rc_graphite-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:01:49+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-test01",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-test01_miimetiq-crt/_data",
            "Name": "miimetiq-test01_miimetiq-crt",
            "Options": null,
            "ResourceID": "miimetiq-test01_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-06-22T17:02:13+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_miimetiq-crt/_data",
            "Name": "miimetiq_miimetiq-crt",
            "Options": null,
            "ResourceID": "miimetiq_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T17:52:19+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_1",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_1_database-data/_data",
            "Name": "testing_server_1_database-data",
            "Options": null,
            "ResourceID": "testing_server_1_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:53+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/6416a174dfeefef55f410de1c012a138727cde18a27171cc4f57e4d11fa57082/_data",
            "Name": "6416a174dfeefef55f410de1c012a138727cde18a27171cc4f57e4d11fa57082",
            "Options": null,
            "ResourceID": "6416a174dfeefef55f410de1c012a138727cde18a27171cc4f57e4d11fa57082_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T11:21:00+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/6f62a85e94bdc8e23626b10fbe0a0b22bfe6c671bfbefef75b8168ed6519c8c8/_data",
            "Name": "6f62a85e94bdc8e23626b10fbe0a0b22bfe6c671bfbefef75b8168ed6519c8c8",
            "Options": null,
            "ResourceID": "6f62a85e94bdc8e23626b10fbe0a0b22bfe6c671bfbefef75b8168ed6519c8c8_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T10:19:42+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/ed86f115f5f8bc4eaeae91b4dc41ceb25d1fc4e739c2f56db00d9cd3a1e6250f/_data",
            "Name": "ed86f115f5f8bc4eaeae91b4dc41ceb25d1fc4e739c2f56db00d9cd3a1e6250f",
            "Options": null,
            "ResourceID": "ed86f115f5f8bc4eaeae91b4dc41ceb25d1fc4e739c2f56db00d9cd3a1e6250f_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-09-21T11:39:21+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/f9b4ddf6c772bbc9b8d0d5f70b99872741fb351a5667f964f2e0f86fd658ec2d/_data",
            "Name": "f9b4ddf6c772bbc9b8d0d5f70b99872741fb351a5667f964f2e0f86fd658ec2d",
            "Options": null,
            "ResourceID": "f9b4ddf6c772bbc9b8d0d5f70b99872741fb351a5667f964f2e0f86fd658ec2d_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:27:51+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/ff0f51f0b76641975b6914f8b91f2db07103f568076f97ace76eb3b1ad9bd924/_data",
            "Name": "ff0f51f0b76641975b6914f8b91f2db07103f568076f97ace76eb3b1ad9bd924",
            "Options": null,
            "ResourceID": "ff0f51f0b76641975b6914f8b91f2db07103f568076f97ace76eb3b1ad9bd924_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:12+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-master",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-master_database-data/_data",
            "Name": "miimetiq-master_database-data",
            "Options": null,
            "ResourceID": "miimetiq-master_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:24:20+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04env",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04env_database-data/_data",
            "Name": "miimetiq_test_04env_database-data",
            "Options": null,
            "ResourceID": "miimetiq_test_04env_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:41:14+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/00ce5549acb5d6413d32b7d0aae5ddd4a886769f7aa870f1cda04d0f2f3aa9b2/_data",
            "Name": "00ce5549acb5d6413d32b7d0aae5ddd4a886769f7aa870f1cda04d0f2f3aa9b2",
            "Options": null,
            "ResourceID": "00ce5549acb5d6413d32b7d0aae5ddd4a886769f7aa870f1cda04d0f2f3aa9b2_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:28:40+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_3",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_3_influx-database-data/_data",
            "Name": "testing_server_3_influx-database-data",
            "Options": null,
            "ResourceID": "testing_server_3_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T12:27:07+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/31837528e46a32e4907b93441677c1edb5c8d6343be4929d2af3b7e65f1e00fe/_data",
            "Name": "31837528e46a32e4907b93441677c1edb5c8d6343be4929d2af3b7e65f1e00fe",
            "Options": null,
            "ResourceID": "31837528e46a32e4907b93441677c1edb5c8d6343be4929d2af3b7e65f1e00fe_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:24:20+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/c695bcceb9bf401f24dec0a9a9f616768c133c6873d46508f6871d85e4a9d6ac/_data",
            "Name": "c695bcceb9bf401f24dec0a9a9f616768c133c6873d46508f6871d85e4a9d6ac",
            "Options": null,
            "ResourceID": "c695bcceb9bf401f24dec0a9a9f616768c133c6873d46508f6871d85e4a9d6ac_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:28:14+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/7aa1fa66aea1dac04cf528660e8b58161a89721b919d1bb7c98dffbf9786f9cf/_data",
            "Name": "7aa1fa66aea1dac04cf528660e8b58161a89721b919d1bb7c98dffbf9786f9cf",
            "Options": null,
            "ResourceID": "7aa1fa66aea1dac04cf528660e8b58161a89721b919d1bb7c98dffbf9786f9cf_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:44:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04_miimetiq-schemas/_data",
            "Name": "miimetiq_test_04_miimetiq-schemas",
            "Options": null,
            "ResourceID": "miimetiq_test_04_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T12:25:26+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "test03-web",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/test03-web_miimetiq-schemas/_data",
            "Name": "test03-web_miimetiq-schemas",
            "Options": null,
            "ResourceID": "test03-web_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T17:52:19+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_1",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_1_influx-database-data/_data",
            "Name": "testing_server_1_influx-database-data",
            "Options": null,
            "ResourceID": "testing_server_1_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:55:27+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/88c2dd246a2a28bcf0a4fc051af662eaf2cc1ab38eb2c548a9c57c2a025e38db/_data",
            "Name": "88c2dd246a2a28bcf0a4fc051af662eaf2cc1ab38eb2c548a9c57c2a025e38db",
            "Options": null,
            "ResourceID": "88c2dd246a2a28bcf0a4fc051af662eaf2cc1ab38eb2c548a9c57c2a025e38db_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-04-04T12:43:45+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/afe1cd51a773787407c282a6e4ae4964d2395a12ea36fa16b7b4f64b1f70ca7c/_data",
            "Name": "afe1cd51a773787407c282a6e4ae4964d2395a12ea36fa16b7b4f64b1f70ca7c",
            "Options": null,
            "ResourceID": "afe1cd51a773787407c282a6e4ae4964d2395a12ea36fa16b7b4f64b1f70ca7c_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-09-13T13:35:47+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/0d4d1f649161c6d3ec8b8ee0b0b3ab50fecde3061d9ce59e1871e355ffe029f0/_data",
            "Name": "0d4d1f649161c6d3ec8b8ee0b0b3ab50fecde3061d9ce59e1871e355ffe029f0",
            "Options": null,
            "ResourceID": "0d4d1f649161c6d3ec8b8ee0b0b3ab50fecde3061d9ce59e1871e355ffe029f0_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-09-28T13:27:10+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/5fe2df522c8a189e259503eadb65e4343d4dae816dd16c170fdee8f2ac6a0e8d/_data",
            "Name": "5fe2df522c8a189e259503eadb65e4343d4dae816dd16c170fdee8f2ac6a0e8d",
            "Options": null,
            "ResourceID": "5fe2df522c8a189e259503eadb65e4343d4dae816dd16c170fdee8f2ac6a0e8d_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-09-28T11:36:12+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/a59de8f443af61f2c8e0f6475d93a02db96d6b3ddaa082fbf09e218d1d133809/_data",
            "Name": "a59de8f443af61f2c8e0f6475d93a02db96d6b3ddaa082fbf09e218d1d133809",
            "Options": null,
            "ResourceID": "a59de8f443af61f2c8e0f6475d93a02db96d6b3ddaa082fbf09e218d1d133809_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:01:49+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-test01",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-test01_message-broker-data/_data",
            "Name": "miimetiq-test01_message-broker-data",
            "Options": null,
            "ResourceID": "miimetiq-test01_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:01:49+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-test01",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-test01_traefik-certificates/_data",
            "Name": "miimetiq-test01_traefik-certificates",
            "Options": null,
            "ResourceID": "miimetiq-test01_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T17:52:19+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_1",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_1_miimetiq-schemas/_data",
            "Name": "testing_server_1_miimetiq-schemas",
            "Options": null,
            "ResourceID": "testing_server_1_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T10:53:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/e70f08697100274abe0b3573b2adf05ab6157fe4b2acda2c773cc09aef3153e5/_data",
            "Name": "e70f08697100274abe0b3573b2adf05ab6157fe4b2acda2c773cc09aef3153e5",
            "Options": null,
            "ResourceID": "e70f08697100274abe0b3573b2adf05ab6157fe4b2acda2c773cc09aef3153e5_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:28:40+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_3",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_3_traefik-certificates/_data",
            "Name": "testing_server_3_traefik-certificates",
            "Options": null,
            "ResourceID": "testing_server_3_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T15:49:32+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/492936628c4b42c71d1f941a14d4541e611849097b203c58322649fa1b57a39c/_data",
            "Name": "492936628c4b42c71d1f941a14d4541e611849097b203c58322649fa1b57a39c",
            "Options": null,
            "ResourceID": "492936628c4b42c71d1f941a14d4541e611849097b203c58322649fa1b57a39c_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:22:17+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/0e1c0be144d14383d7bf76f4ecc4ebd9bf5fde516aef020c67545f523dfae9cf/_data",
            "Name": "0e1c0be144d14383d7bf76f4ecc4ebd9bf5fde516aef020c67545f523dfae9cf",
            "Options": null,
            "ResourceID": "0e1c0be144d14383d7bf76f4ecc4ebd9bf5fde516aef020c67545f523dfae9cf_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T16:39:39+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/19aa5333d89386846b8cf131ccafa5f23e11f4c7c7a8dd0a4a2d15e9da5b518b/_data",
            "Name": "19aa5333d89386846b8cf131ccafa5f23e11f4c7c7a8dd0a4a2d15e9da5b518b",
            "Options": null,
            "ResourceID": "19aa5333d89386846b8cf131ccafa5f23e11f4c7c7a8dd0a4a2d15e9da5b518b_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T17:00:16+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/b4a805a4b43dc61ed1bdf68f867dc2aabbd6ff26afa47c55d8687709f494c28d/_data",
            "Name": "b4a805a4b43dc61ed1bdf68f867dc2aabbd6ff26afa47c55d8687709f494c28d",
            "Options": null,
            "ResourceID": "b4a805a4b43dc61ed1bdf68f867dc2aabbd6ff26afa47c55d8687709f494c28d_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:03:42+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/a60b220c97f6d676f76a5f278066c1ef9c751b18c91b2628cff6c38824b44fe4/_data",
            "Name": "a60b220c97f6d676f76a5f278066c1ef9c751b18c91b2628cff6c38824b44fe4",
            "Options": null,
            "ResourceID": "a60b220c97f6d676f76a5f278066c1ef9c751b18c91b2628cff6c38824b44fe4_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:12+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-master",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-master_miimetiq-schemas/_data",
            "Name": "miimetiq-master_miimetiq-schemas",
            "Options": null,
            "ResourceID": "miimetiq-master_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T18:07:22+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_4",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_4_miimetiq-crt/_data",
            "Name": "testing_server_4_miimetiq-crt",
            "Options": null,
            "ResourceID": "testing_server_4_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:28:40+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_3",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_3_message-broker-data/_data",
            "Name": "testing_server_3_message-broker-data",
            "Options": null,
            "ResourceID": "testing_server_3_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-04-04T12:37:53+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/ff28fdc80a33c035d76501c87f2868d635077789a5e217e14203bbc89766401a/_data",
            "Name": "ff28fdc80a33c035d76501c87f2868d635077789a5e217e14203bbc89766401a",
            "Options": null,
            "ResourceID": "ff28fdc80a33c035d76501c87f2868d635077789a5e217e14203bbc89766401a_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-09-28T12:52:34+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/547d4fdb77a9c74b71108adbc8327eb93d0e4b3c93cead00fcba7b4c660ba977/_data",
            "Name": "547d4fdb77a9c74b71108adbc8327eb93d0e4b3c93cead00fcba7b4c660ba977",
            "Options": null,
            "ResourceID": "547d4fdb77a9c74b71108adbc8327eb93d0e4b3c93cead00fcba7b4c660ba977_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:01:49+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-test01",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-test01_influx-database-data/_data",
            "Name": "miimetiq-test01_influx-database-data",
            "Options": null,
            "ResourceID": "miimetiq-test01_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:27:51+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_03",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_03_miimetiq-schemas/_data",
            "Name": "miimetiq_test_03_miimetiq-schemas",
            "Options": null,
            "ResourceID": "miimetiq_test_03_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-21T19:18:37+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/dbcb24db6f9b356cd0069bb3a17fd1fc2bda2989120b652f69da447659a64109/_data",
            "Name": "dbcb24db6f9b356cd0069bb3a17fd1fc2bda2989120b652f69da447659a64109",
            "Options": null,
            "ResourceID": "dbcb24db6f9b356cd0069bb3a17fd1fc2bda2989120b652f69da447659a64109_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:54:44+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/e377602636d5fe59adf16d951d8be9ba8370291847457952e9c03b057c5a7119/_data",
            "Name": "e377602636d5fe59adf16d951d8be9ba8370291847457952e9c03b057c5a7119",
            "Options": null,
            "ResourceID": "e377602636d5fe59adf16d951d8be9ba8370291847457952e9c03b057c5a7119_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T17:09:52+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/0ab59e080b68781fafd23c7dd0b7b303190aec033095d6be6d24f23d4fa7f4ea/_data",
            "Name": "0ab59e080b68781fafd23c7dd0b7b303190aec033095d6be6d24f23d4fa7f4ea",
            "Options": null,
            "ResourceID": "0ab59e080b68781fafd23c7dd0b7b303190aec033095d6be6d24f23d4fa7f4ea_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-18T13:03:39+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/4304ac3047decbf1ab8d7109a6355dcbdea304d8d49d2063c37cf616ae5638ce/_data",
            "Name": "4304ac3047decbf1ab8d7109a6355dcbdea304d8d49d2063c37cf616ae5638ce",
            "Options": null,
            "ResourceID": "4304ac3047decbf1ab8d7109a6355dcbdea304d8d49d2063c37cf616ae5638ce_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T16:29:50+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-2_7rc",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-2_7rc_influx-database-data/_data",
            "Name": "miimetiq-2_7rc_influx-database-data",
            "Options": null,
            "ResourceID": "miimetiq-2_7rc_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-06-22T17:02:13+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_message-broker-data/_data",
            "Name": "miimetiq_message-broker-data",
            "Options": null,
            "ResourceID": "miimetiq_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:27:51+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_03",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_03_database-data/_data",
            "Name": "miimetiq_test_03_database-data",
            "Options": null,
            "ResourceID": "miimetiq_test_03_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T12:25:27+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "test03-web",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/test03-web_influx-database-data/_data",
            "Name": "test03-web_influx-database-data",
            "Options": null,
            "ResourceID": "test03-web_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:22:16+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_2",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_2_miimetiq-crt/_data",
            "Name": "testing_server_2_miimetiq-crt",
            "Options": null,
            "ResourceID": "testing_server_2_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-04-04T13:37:56+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/95f8c7c6aaef952b84739f9791bec708cd59c31bd1c754f899b257f0cf2577df/_data",
            "Name": "95f8c7c6aaef952b84739f9791bec708cd59c31bd1c754f899b257f0cf2577df",
            "Options": null,
            "ResourceID": "95f8c7c6aaef952b84739f9791bec708cd59c31bd1c754f899b257f0cf2577df_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:24:20+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04env",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04env_traefik-certificates/_data",
            "Name": "miimetiq_test_04env_traefik-certificates",
            "Options": null,
            "ResourceID": "miimetiq_test_04env_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:52:25+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/d5db6f4248669952c1cb9c31716cb2b7b3e370cbfe119f49f87f166a5d27ecff/_data",
            "Name": "d5db6f4248669952c1cb9c31716cb2b7b3e370cbfe119f49f87f166a5d27ecff",
            "Options": null,
            "ResourceID": "d5db6f4248669952c1cb9c31716cb2b7b3e370cbfe119f49f87f166a5d27ecff_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T17:06:41+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/b1a76ab9096be3c7aca2662ee410f130c19b3e6188ab778c93151f86f16ef88d/_data",
            "Name": "b1a76ab9096be3c7aca2662ee410f130c19b3e6188ab778c93151f86f16ef88d",
            "Options": null,
            "ResourceID": "b1a76ab9096be3c7aca2662ee410f130c19b3e6188ab778c93151f86f16ef88d_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-09-28T13:23:33+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/035fa17700a737d48a3c668e8ccd52340ae0a78367bdbd49b93c4e9e47cfe114/_data",
            "Name": "035fa17700a737d48a3c668e8ccd52340ae0a78367bdbd49b93c4e9e47cfe114",
            "Options": null,
            "ResourceID": "035fa17700a737d48a3c668e8ccd52340ae0a78367bdbd49b93c4e9e47cfe114_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:46:56+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/e5148608422bb22bb070b472898dfc033c0fc3075877debc244da790706e55b8/_data",
            "Name": "e5148608422bb22bb070b472898dfc033c0fc3075877debc244da790706e55b8",
            "Options": null,
            "ResourceID": "e5148608422bb22bb070b472898dfc033c0fc3075877debc244da790706e55b8_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:44:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04_database-data/_data",
            "Name": "miimetiq_test_04_database-data",
            "Options": null,
            "ResourceID": "miimetiq_test_04_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:24:19+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04env",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04env_miimetiq-crt/_data",
            "Name": "miimetiq_test_04env_miimetiq-crt",
            "Options": null,
            "ResourceID": "miimetiq_test_04env_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:22:16+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_2",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_2_miimetiq-schemas/_data",
            "Name": "testing_server_2_miimetiq-schemas",
            "Options": null,
            "ResourceID": "testing_server_2_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:34:43+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/18b925bf9441bce11554cf42019922aa825d23ecb85f672958ab0646e6d7b86f/_data",
            "Name": "18b925bf9441bce11554cf42019922aa825d23ecb85f672958ab0646e6d7b86f",
            "Options": null,
            "ResourceID": "18b925bf9441bce11554cf42019922aa825d23ecb85f672958ab0646e6d7b86f_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T18:07:22+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/1f4663b12f339878d7d731ac9bc5029917fa6eba365f8f329c3653fdb77361dd/_data",
            "Name": "1f4663b12f339878d7d731ac9bc5029917fa6eba365f8f329c3653fdb77361dd",
            "Options": null,
            "ResourceID": "1f4663b12f339878d7d731ac9bc5029917fa6eba365f8f329c3653fdb77361dd_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T18:07:22+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_4",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_4_miimetiq-schemas/_data",
            "Name": "testing_server_4_miimetiq-schemas",
            "Options": null,
            "ResourceID": "testing_server_4_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:28:40+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_3",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_3_miimetiq-crt/_data",
            "Name": "testing_server_3_miimetiq-crt",
            "Options": null,
            "ResourceID": "testing_server_3_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T15:47:30+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/e3761060eabc23ae2e44ee896ce9b801271b712390f561f5d0e492c8a90b3476/_data",
            "Name": "e3761060eabc23ae2e44ee896ce9b801271b712390f561f5d0e492c8a90b3476",
            "Options": null,
            "ResourceID": "e3761060eabc23ae2e44ee896ce9b801271b712390f561f5d0e492c8a90b3476_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T16:06:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/d4367a27965d759ac1b69494261592c9b410e3273272c01ebd70b6b7572decbb/_data",
            "Name": "d4367a27965d759ac1b69494261592c9b410e3273272c01ebd70b6b7572decbb",
            "Options": null,
            "ResourceID": "d4367a27965d759ac1b69494261592c9b410e3273272c01ebd70b6b7572decbb_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-09-13T13:12:28+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/62ab07f95ad57f3eafb2bf01c3e3be7b7a8a5734816e880fd9b52b463a711906/_data",
            "Name": "62ab07f95ad57f3eafb2bf01c3e3be7b7a8a5734816e880fd9b52b463a711906",
            "Options": null,
            "ResourceID": "62ab07f95ad57f3eafb2bf01c3e3be7b7a8a5734816e880fd9b52b463a711906_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T16:29:50+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-2_7rc",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-2_7rc_miimetiq-crt/_data",
            "Name": "miimetiq-2_7rc_miimetiq-crt",
            "Options": null,
            "ResourceID": "miimetiq-2_7rc_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:12+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-master",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-master_miimetiq-crt/_data",
            "Name": "miimetiq-master_miimetiq-crt",
            "Options": null,
            "ResourceID": "miimetiq-master_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T17:52:18+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_1",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_1_miimetiq-crt/_data",
            "Name": "testing_server_1_miimetiq-crt",
            "Options": null,
            "ResourceID": "testing_server_1_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T16:29:50+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-2_7rc",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-2_7rc_miimetiq-schemas/_data",
            "Name": "miimetiq-2_7rc_miimetiq-schemas",
            "Options": null,
            "ResourceID": "miimetiq-2_7rc_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-06-20T15:13:14+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/portainer_agent_data/_data",
            "Name": "portainer_agent_data",
            "Options": null,
            "ResourceID": "portainer_agent_data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:28:40+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_3",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_3_database-data/_data",
            "Name": "testing_server_3_database-data",
            "Options": null,
            "ResourceID": "testing_server_3_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-04T10:51:15+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/2a15900a328d34c2db5556c3e7fb9cd03b6c7e82a933164415f8faa638dd7eac/_data",
            "Name": "2a15900a328d34c2db5556c3e7fb9cd03b6c7e82a933164415f8faa638dd7eac",
            "Options": null,
            "ResourceID": "2a15900a328d34c2db5556c3e7fb9cd03b6c7e82a933164415f8faa638dd7eac_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:44:32+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/59d7ef6497797562b6c85b7341eb52299232ae89878ef58e8576abb6a054db93/_data",
            "Name": "59d7ef6497797562b6c85b7341eb52299232ae89878ef58e8576abb6a054db93",
            "Options": null,
            "ResourceID": "59d7ef6497797562b6c85b7341eb52299232ae89878ef58e8576abb6a054db93_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T17:52:19+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/9f48946e8b4f727dcc403da1ab75e1acccf7eaaf123c380e18ee259fb2f50afc/_data",
            "Name": "9f48946e8b4f727dcc403da1ab75e1acccf7eaaf123c380e18ee259fb2f50afc",
            "Options": null,
            "ResourceID": "9f48946e8b4f727dcc403da1ab75e1acccf7eaaf123c380e18ee259fb2f50afc_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T16:29:50+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-2_7rc",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-2_7rc_message-broker-data/_data",
            "Name": "miimetiq-2_7rc_message-broker-data",
            "Options": null,
            "ResourceID": "miimetiq-2_7rc_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T12:25:26+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "test03-web",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/test03-web_message-broker-data/_data",
            "Name": "test03-web_message-broker-data",
            "Options": null,
            "ResourceID": "test03-web_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-04T10:28:25+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/232245477b2021647b8a6dbce2266f0cceab51136d7d314c72937115ce029539/_data",
            "Name": "232245477b2021647b8a6dbce2266f0cceab51136d7d314c72937115ce029539",
            "Options": null,
            "ResourceID": "232245477b2021647b8a6dbce2266f0cceab51136d7d314c72937115ce029539_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T15:52:04+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/2097e7cca6749fba385b8c9b766ef0cfcdf480614c2268be53d1686d7b7db05d/_data",
            "Name": "2097e7cca6749fba385b8c9b766ef0cfcdf480614c2268be53d1686d7b7db05d",
            "Options": null,
            "ResourceID": "2097e7cca6749fba385b8c9b766ef0cfcdf480614c2268be53d1686d7b7db05d_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-06-22T17:02:13+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "graphite-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_graphite-database-data/_data",
            "Name": "miimetiq_graphite-database-data",
            "Options": null,
            "ResourceID": "miimetiq_graphite-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:27:51+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_03",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_03_miimetiq-crt/_data",
            "Name": "miimetiq_test_03_miimetiq-crt",
            "Options": null,
            "ResourceID": "miimetiq_test_03_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T17:52:19+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_1",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_1_traefik-certificates/_data",
            "Name": "testing_server_1_traefik-certificates",
            "Options": null,
            "ResourceID": "testing_server_1_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T10:02:28+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/d98a81f2fc76560e589275230feee801a657aa2c5855455aaf59c57bfdb38f59/_data",
            "Name": "d98a81f2fc76560e589275230feee801a657aa2c5855455aaf59c57bfdb38f59",
            "Options": null,
            "ResourceID": "d98a81f2fc76560e589275230feee801a657aa2c5855455aaf59c57bfdb38f59_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:51:43+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/643b79cac3c6f6dada7ff750afdefc5388c62e0eedf983d4fe54aacadcd8f206/_data",
            "Name": "643b79cac3c6f6dada7ff750afdefc5388c62e0eedf983d4fe54aacadcd8f206",
            "Options": null,
            "ResourceID": "643b79cac3c6f6dada7ff750afdefc5388c62e0eedf983d4fe54aacadcd8f206_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:01:50+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/d0218abd751c9a5b58f3bb15bad9e76155801866856caed8fba97a617adf88e7/_data",
            "Name": "d0218abd751c9a5b58f3bb15bad9e76155801866856caed8fba97a617adf88e7",
            "Options": null,
            "ResourceID": "d0218abd751c9a5b58f3bb15bad9e76155801866856caed8fba97a617adf88e7_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:01:49+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-test01",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-test01_database-data/_data",
            "Name": "miimetiq-test01_database-data",
            "Options": null,
            "ResourceID": "miimetiq-test01_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T16:58:07+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/52517dc1d696bfa2e7158fa7f0da74025b6f62ecd3be112ee817e1fc11521752/_data",
            "Name": "52517dc1d696bfa2e7158fa7f0da74025b6f62ecd3be112ee817e1fc11521752",
            "Options": null,
            "ResourceID": "52517dc1d696bfa2e7158fa7f0da74025b6f62ecd3be112ee817e1fc11521752_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T16:29:50+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-2_7rc",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-2_7rc_database-data/_data",
            "Name": "miimetiq-2_7rc_database-data",
            "Options": null,
            "ResourceID": "miimetiq-2_7rc_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:27:51+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_03",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_03_influx-database-data/_data",
            "Name": "miimetiq_test_03_influx-database-data",
            "Options": null,
            "ResourceID": "miimetiq_test_03_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-04-04T11:06:36+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/b9ad942a690722778c51ea02e419e10fe9812f778e9782d783ad9d29166760e6/_data",
            "Name": "b9ad942a690722778c51ea02e419e10fe9812f778e9782d783ad9d29166760e6",
            "Options": null,
            "ResourceID": "b9ad942a690722778c51ea02e419e10fe9812f778e9782d783ad9d29166760e6_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T12:25:26+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "test03-web",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/test03-web_traefik-certificates/_data",
            "Name": "test03-web_traefik-certificates",
            "Options": null,
            "ResourceID": "test03-web_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T16:50:15+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/3b80800754523b5d794b584c0fbc5f71cc4c26b45a1502b3753f09a81f677388/_data",
            "Name": "3b80800754523b5d794b584c0fbc5f71cc4c26b45a1502b3753f09a81f677388",
            "Options": null,
            "ResourceID": "3b80800754523b5d794b584c0fbc5f71cc4c26b45a1502b3753f09a81f677388_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T16:29:51+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/83e007bf00ac4846293d61d3cbe638a3cb042a5580b4de7c3704647300d28b8a/_data",
            "Name": "83e007bf00ac4846293d61d3cbe638a3cb042a5580b4de7c3704647300d28b8a",
            "Options": null,
            "ResourceID": "83e007bf00ac4846293d61d3cbe638a3cb042a5580b4de7c3704647300d28b8a_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:12+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-master",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-master_influx-database-data/_data",
            "Name": "miimetiq-master_influx-database-data",
            "Options": null,
            "ResourceID": "miimetiq-master_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:24:20+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04env",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04env_miimetiq-schemas/_data",
            "Name": "miimetiq_test_04env_miimetiq-schemas",
            "Options": null,
            "ResourceID": "miimetiq_test_04env_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T17:52:18+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_1",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_1_message-broker-data/_data",
            "Name": "testing_server_1_message-broker-data",
            "Options": null,
            "ResourceID": "testing_server_1_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T18:07:22+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_4",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_4_influx-database-data/_data",
            "Name": "testing_server_4_influx-database-data",
            "Options": null,
            "ResourceID": "testing_server_4_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T16:36:17+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/38a72f28c91ab380a14041b57ec826d496ed9892c86c41c5148091f79822d082/_data",
            "Name": "38a72f28c91ab380a14041b57ec826d496ed9892c86c41c5148091f79822d082",
            "Options": null,
            "ResourceID": "38a72f28c91ab380a14041b57ec826d496ed9892c86c41c5148091f79822d082_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T17:44:19+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/ea1fc4e01aa44e75906bcc396ac3e7227a41de3aea111fbc49627d94c0a12d82/_data",
            "Name": "ea1fc4e01aa44e75906bcc396ac3e7227a41de3aea111fbc49627d94c0a12d82",
            "Options": null,
            "ResourceID": "ea1fc4e01aa44e75906bcc396ac3e7227a41de3aea111fbc49627d94c0a12d82_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-04-04T15:21:14+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/55f8f38129503a442d19cc3188ae1b68cbb00a55c8aaa9a58cd4429ff123acb3/_data",
            "Name": "55f8f38129503a442d19cc3188ae1b68cbb00a55c8aaa9a58cd4429ff123acb3",
            "Options": null,
            "ResourceID": "55f8f38129503a442d19cc3188ae1b68cbb00a55c8aaa9a58cd4429ff123acb3_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T11:45:22+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/9d2d4fb0ec1bbdf9ce36779e54767af92706ee84b16b5a9b315cae9c4c77867f/_data",
            "Name": "9d2d4fb0ec1bbdf9ce36779e54767af92706ee84b16b5a9b315cae9c4c77867f",
            "Options": null,
            "ResourceID": "9d2d4fb0ec1bbdf9ce36779e54767af92706ee84b16b5a9b315cae9c4c77867f_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-04T11:27:17+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/9ffbf2db82a77b921376d21df9bdec7953ee13df63b0ed086e612b1d4cc55179/_data",
            "Name": "9ffbf2db82a77b921376d21df9bdec7953ee13df63b0ed086e612b1d4cc55179",
            "Options": null,
            "ResourceID": "9ffbf2db82a77b921376d21df9bdec7953ee13df63b0ed086e612b1d4cc55179_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-09-28T13:45:21+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/a6ee507f0fc05443332f3c0bfb48ef0c58ebcc3818e6b49a5c135c6789c16612/_data",
            "Name": "a6ee507f0fc05443332f3c0bfb48ef0c58ebcc3818e6b49a5c135c6789c16612",
            "Options": null,
            "ResourceID": "a6ee507f0fc05443332f3c0bfb48ef0c58ebcc3818e6b49a5c135c6789c16612_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:12+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq-master",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq-master_traefik-certificates/_data",
            "Name": "miimetiq-master_traefik-certificates",
            "Options": null,
            "ResourceID": "miimetiq-master_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:44:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04_miimetiq-crt/_data",
            "Name": "miimetiq_test_04_miimetiq-crt",
            "Options": null,
            "ResourceID": "miimetiq_test_04_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:28:40+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/750aaa2b490a2c76bd93ecc10b6c5bba103300aee8cbc5fc27384b899fc003cc/_data",
            "Name": "750aaa2b490a2c76bd93ecc10b6c5bba103300aee8cbc5fc27384b899fc003cc",
            "Options": null,
            "ResourceID": "750aaa2b490a2c76bd93ecc10b6c5bba103300aee8cbc5fc27384b899fc003cc_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:49:45+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/49d3d3d7c4e5cd2bcb871cca375cdf4ad98b03ded7283441d79ce1c11d8609a2/_data",
            "Name": "49d3d3d7c4e5cd2bcb871cca375cdf4ad98b03ded7283441d79ce1c11d8609a2",
            "Options": null,
            "ResourceID": "49d3d3d7c4e5cd2bcb871cca375cdf4ad98b03ded7283441d79ce1c11d8609a2_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T17:40:25+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/069c998c74353da0de040391e53f9ef6e274d3ef8c622d460a5ad96c7d79887c/_data",
            "Name": "069c998c74353da0de040391e53f9ef6e274d3ef8c622d460a5ad96c7d79887c",
            "Options": null,
            "ResourceID": "069c998c74353da0de040391e53f9ef6e274d3ef8c622d460a5ad96c7d79887c_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-04-04T16:04:46+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/fe75c058631a9d2b435171bd96c05973aef41b259621910ab7dea2d0c419c89e/_data",
            "Name": "fe75c058631a9d2b435171bd96c05973aef41b259621910ab7dea2d0c419c89e",
            "Options": null,
            "ResourceID": "fe75c058631a9d2b435171bd96c05973aef41b259621910ab7dea2d0c419c89e_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T13:05:05+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/4b7328f1ce214ea609a6653350539479113e12b5dd7ba0640c20058455b48225/_data",
            "Name": "4b7328f1ce214ea609a6653350539479113e12b5dd7ba0640c20058455b48225",
            "Options": null,
            "ResourceID": "4b7328f1ce214ea609a6653350539479113e12b5dd7ba0640c20058455b48225_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-20T18:07:22+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_4",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_4_message-broker-data/_data",
            "Name": "testing_server_4_message-broker-data",
            "Options": null,
            "ResourceID": "testing_server_4_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T16:34:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/af30959c8f67a0218182a903f72e90eeeb6b3706ecead565343b02fb69107261/_data",
            "Name": "af30959c8f67a0218182a903f72e90eeeb6b3706ecead565343b02fb69107261",
            "Options": null,
            "ResourceID": "af30959c8f67a0218182a903f72e90eeeb6b3706ecead565343b02fb69107261_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-04-04T16:44:25+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/4030b37fa5a20d1b8889afa481257a9d55e72ca13d09db032bcb61dae610e048/_data",
            "Name": "4030b37fa5a20d1b8889afa481257a9d55e72ca13d09db032bcb61dae610e048",
            "Options": null,
            "ResourceID": "4030b37fa5a20d1b8889afa481257a9d55e72ca13d09db032bcb61dae610e048_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-03T13:03:13+01:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/59812e0100bb24965dd050ccc61aca487500ef43854736518295c112e999aac0/_data",
            "Name": "59812e0100bb24965dd050ccc61aca487500ef43854736518295c112e999aac0",
            "Options": null,
            "ResourceID": "59812e0100bb24965dd050ccc61aca487500ef43854736518295c112e999aac0_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T12:25:26+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "test03-web",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/test03-web_database-data/_data",
            "Name": "test03-web_database-data",
            "Options": null,
            "ResourceID": "test03-web_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:22:16+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_2",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_2_database-data/_data",
            "Name": "testing_server_2_database-data",
            "Options": null,
            "ResourceID": "testing_server_2_database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T17:39:41+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/042acc9b5da1eb5fe4cae6dd2a6581e21049ad66456c465a07cd1e8a8edc3ff0/_data",
            "Name": "042acc9b5da1eb5fe4cae6dd2a6581e21049ad66456c465a07cd1e8a8edc3ff0",
            "Options": null,
            "ResourceID": "042acc9b5da1eb5fe4cae6dd2a6581e21049ad66456c465a07cd1e8a8edc3ff0_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-06-22T17:02:13+02:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq",
                "com.docker.compose.version": "2.17.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_influx-database-data/_data",
            "Name": "miimetiq_influx-database-data",
            "Options": null,
            "ResourceID": "miimetiq_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:44:31+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "traefik-certificates"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04_traefik-certificates/_data",
            "Name": "miimetiq_test_04_traefik-certificates",
            "Options": null,
            "ResourceID": "miimetiq_test_04_traefik-certificates_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T18:24:19+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "miimetiq_test_04env",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "influx-database-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/miimetiq_test_04env_influx-database-data/_data",
            "Name": "miimetiq_test_04env_influx-database-data",
            "Options": null,
            "ResourceID": "miimetiq_test_04env_influx-database-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-01-25T12:25:26+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "test03-web",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-crt"
            },
            "Mountpoint": "/var/lib/docker/volumes/test03-web_miimetiq-crt/_data",
            "Name": "test03-web_miimetiq-crt",
            "Options": null,
            "ResourceID": "test03-web_miimetiq-crt_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T11:28:40+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_3",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "miimetiq-schemas"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_3_miimetiq-schemas/_data",
            "Name": "testing_server_3_miimetiq-schemas",
            "Options": null,
            "ResourceID": "testing_server_3_miimetiq-schemas_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T16:28:35+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/6d7d494df7adf05a17fea3dedc4c6142740df6db6fae53d1f111c05b0b521f7c/_data",
            "Name": "6d7d494df7adf05a17fea3dedc4c6142740df6db6fae53d1f111c05b0b521f7c",
            "Options": null,
            "ResourceID": "6d7d494df7adf05a17fea3dedc4c6142740df6db6fae53d1f111c05b0b521f7c_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T19:06:25+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/83e71845a6255428fca32f1215315faa5294a5e6c01dd9a293a418ed31e9effb/_data",
            "Name": "83e71845a6255428fca32f1215315faa5294a5e6c01dd9a293a418ed31e9effb",
            "Options": null,
            "ResourceID": "83e71845a6255428fca32f1215315faa5294a5e6c01dd9a293a418ed31e9effb_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-08-17T18:22:58+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/01e24dc8b6f6fa4bc1c3ab90cb5ae18969d5e92ed784ffe92386e5ad2a35a90f/_data",
            "Name": "01e24dc8b6f6fa4bc1c3ab90cb5ae18969d5e92ed784ffe92386e5ad2a35a90f",
            "Options": null,
            "ResourceID": "01e24dc8b6f6fa4bc1c3ab90cb5ae18969d5e92ed784ffe92386e5ad2a35a90f_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2023-06-22T17:02:14+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/5e2880882641da3558122167cff386146de0012f04065cfd81f1c40378d0b83d/_data",
            "Name": "5e2880882641da3558122167cff386146de0012f04065cfd81f1c40378d0b83d",
            "Options": null,
            "ResourceID": "5e2880882641da3558122167cff386146de0012f04065cfd81f1c40378d0b83d_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-22T12:22:16+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "testing_server_2",
                "com.docker.compose.version": "2.20.2",
                "com.docker.compose.volume": "message-broker-data"
            },
            "Mountpoint": "/var/lib/docker/volumes/testing_server_2_message-broker-data/_data",
            "Name": "testing_server_2_message-broker-data",
            "Options": null,
            "ResourceID": "testing_server_2_message-broker-data_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        },
        {
            "CreatedAt": "2024-02-27T17:54:20+01:00",
            "Driver": "local",
            "Labels": {
                "com.docker.volume.anonymous": ""
            },
            "Mountpoint": "/var/lib/docker/volumes/9fff4288903060a4b4ff315ed073913aadfec533fc4332a6142db593343170bd/_data",
            "Name": "9fff4288903060a4b4ff315ed073913aadfec533fc4332a6142db593343170bd",
            "Options": null,
            "ResourceID": "9fff4288903060a4b4ff315ed073913aadfec533fc4332a6142db593343170bd_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "Scope": "local"
        }
    ],
    "Warnings": null
}
```

# delete volume

```bash
curl 'https://portainer.nexiona.io/api/endpoints/30/docker/volumes/test01' \
  -X 'DELETE' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'cookie: portainer_api_key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQsInVzZXJuYW1lIjoib3Jpb2wucml1cyIsInJvbGUiOjEsInNjb3BlIjoiZGVmYXVsdCIsImZvcmNlQ2hhbmdlUGFzc3dvcmQiOmZhbHNlLCJleHAiOjE3MTI2NzgxOTMsImlhdCI6MTcxMjY0OTM5M30.57qC57MMV0cZ-rpcrrJ7vuoD7AwmvvO-fsm3dJGIRpI; _gorilla_csrf=MTcxMjY0OTM5M3xJblp4YTA1RFQxbENUMVJFT1ZBNVZ6TmtUekk0VW1kQmNGWm5hWEI2V0ZWUmJraFRVR1ozWlZBMFVHczlJZ289fJAfz_iWdO5PZ3UmQ9Gxe5MwHam-cd7_fHtCRzwpSb6D' \
  -H 'origin: https://portainer.nexiona.io' \
  -H 'pragma: no-cache' \
  -H 'referer: https://portainer.nexiona.io/' \
  -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  -H 'x-csrf-token: llDuKTDsUHa4lhB+5S6W4yhCvkJGNvfzZgZ94PfPeuko+eMh1u1pRkWpxcmRwyqlKGvoSu/7guP6cvKf8ECaEA=='
```

response:
![Alt text](image.png)

HTTP code: 204 No content


# create volume

```bash
curl 'https://portainer.nexiona.io/api/endpoints/30/docker/volumes/create' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'cookie: portainer_api_key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQsInVzZXJuYW1lIjoib3Jpb2wucml1cyIsInJvbGUiOjEsInNjb3BlIjoiZGVmYXVsdCIsImZvcmNlQ2hhbmdlUGFzc3dvcmQiOmZhbHNlLCJleHAiOjE3MTI2NzgxOTMsImlhdCI6MTcxMjY0OTM5M30.57qC57MMV0cZ-rpcrrJ7vuoD7AwmvvO-fsm3dJGIRpI; _gorilla_csrf=MTcxMjY0OTM5M3xJblp4YTA1RFQxbENUMVJFT1ZBNVZ6TmtUekk0VW1kQmNGWm5hWEI2V0ZWUmJraFRVR1ozWlZBMFVHczlJZ289fJAfz_iWdO5PZ3UmQ9Gxe5MwHam-cd7_fHtCRzwpSb6D' \
  -H 'origin: https://portainer.nexiona.io' \
  -H 'pragma: no-cache' \
  -H 'referer: https://portainer.nexiona.io/' \
  -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  -H 'x-csrf-token: y6Xm96VlDxkkdO5Rhem6HAgndYUP/zOCXFPlDjaVRMZ1DOv/Q2Q2KdlLO+bxBAZaCA4jjaYyRpLAJ2pxMRqkPw==' \
  -H 'x-portainer-volumename: test01' \
  --data-raw '{"Name":"test01","Driver":"local","DriverOpts":{}}'
```

```json
{
    "CreatedAt": "2024-04-09T10:08:38+02:00",
    "Driver": "local",
    "Labels": null,
    "Mountpoint": "/var/lib/docker/volumes/test01/_data",
    "Name": "test01",
    "Options": {},
    "Portainer": {
        "ResourceControl": {
            "Id": 120,
            "ResourceId": "test01_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "SubResourceIds": [],
            "Type": 3,
            "UserAccesses": [
                {
                    "UserId": 14,
                    "AccessLevel": 1
                }
            ],
            "TeamAccesses": [],
            "Public": false,
            "AdministratorsOnly": false,
            "System": false
        }
    },
    "ResourceID": "test01_e34b6cb8-1bed-4531-88e1-82edb35204cb",
    "Scope": "local"
}
```


```json
{
    "CreatedAt": "2024-04-09T10:08:38+02:00",
    "Driver": "local",
    "Labels": null,
    "Mountpoint": "/var/lib/docker/volumes/test01/_data",
    "Name": "test01",
    "Options": {},
    "Portainer": {
        "ResourceControl": {
            "Id": 120,
            "ResourceId": "test01_e34b6cb8-1bed-4531-88e1-82edb35204cb",
            "SubResourceIds": [],
            "Type": 3,
            "UserAccesses": [
                {
                    "UserId": 14,
                    "AccessLevel": 1
                }
            ],
            "TeamAccesses": [],
            "Public": false,
            "AdministratorsOnly": false,
            "System": false
        }
    },
    "ResourceID": "test01_e34b6cb8-1bed-4531-88e1-82edb35204cb",
    "Scope": "local"
}
```