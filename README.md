# opendata_C2023

Open data challenge

# Prepare environment

## Docker(optional)

```
$ docker-compose up -d
```

VS Code Docker extension -> Containers -> opendata_c2023-dev-env(Right click) -> Attach Visual Studio Code

## Poetry

Recommend setting

```
$ poetry config virtualenvs.in-project true
```

Install Packages

```
$ poetry install
```

## VPN

Using WireGuard

### Host(Ubuntu)

### Client(Windows)

(Installation page)[https://www.wireguard.com/install/]

On WireGuard window

- Press `Ctrl + N`

```
[Interface]
PrivateKey = ****
ListenPort = 51820
Address = 10.0.0.2/32

[Peer]
PublicKey = ****
AllowedIPs = 10.0.0.1/32
```

# Insert initial data

- Create temp table to import csv
