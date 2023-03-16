# Selenium Automation Test #

## :page_facing_up: About ##
Este es un proyecto con el objetivo de automatizar test Juice Shop con Seleniun.

## :hammer_and_wrench: Project Setup ##
Antes de correr el proyecto asegúrate de tener los siguientes paquetes:

```shell
    #Windows
    pip install pipenv
```

Después de agregar el enviroment instala las dependencias siguiendo el siguiente comando.

```shell
    pipenv install -r requirements.txt
```

## Running Project ##

Para correr todos los test, sigue el siguiente comando.
```shell
    pipenv run pytest
```

Para correr todos los test y generar reportes con Allure siga los siguientes pasos:

```shell
    pipenv run pytest --alluredir=allure-results
    allure serve allure-results
```

> Nota: Para verificar el resultado podrás ver los reportes dentro de la carpeta screenshots