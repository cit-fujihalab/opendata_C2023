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

## pip

pycaret が poetry だとうまく入らないので，pycaret は pip で．  
Windows + Docker でかろうじて動作しているが，インタラクティブウィンドウの表示が一部おかしい．

pip でのパッケージのインストールはこのコマンド．

```shell
$ pip install -r requirements.txt
```
