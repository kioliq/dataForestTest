# dataForestTest

Тестове завдання. Інфраструктура через terraform (VPC, Cloudfront, EC2), Web serving через Nginx. Деплоїнг через docker compose, який запускається у user_data. 

## Flow
```
CloudFront -> EC2 -> nginx -> backend (FastAPI) -> postgres
```

EC2 при старті через user_data ставить Docker, клонує репо і піднімає compose.
На сервер коннекшн йде тільки через CloudFront. На сервер SSH закритий, доступ тільки через SSM.

## Структура проекта
- **terraform** - інфраструктура
- **docker** - compose і конфіг nginx
- **app** - backend і frontend
- **.github** - CI, terraform validate і смок тест

## Запуск
Локально: **cd docker && cp .env.example .env && docker compose up -d --build**

В AWS: **cd terraform && terraform init && terraform apply**

## Покращення для проду
- HTTPS між CloudFront і EC2
- remote state в S3
- RDS замість postgres в контейнері
- збирати образи в CI і пушити в registry, а не білдити на сервері
- додати моніторинг і алерти
