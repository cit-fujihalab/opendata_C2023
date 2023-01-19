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

```
$ poetry install
```


## VS Code
### Linter
Press "F1" Key -> Type "Python: Select Linter" and select-> flake8