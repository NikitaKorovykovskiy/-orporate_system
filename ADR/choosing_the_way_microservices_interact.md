# ADR: Выбор структуры проекта

## Контекст и проблема

Я должен выбрать примерную структуру и вид проекта, который будет использовать микросервисы с возможностью функционально маршрутизировать запросы без объединения БД.

## Рассмотренные варианты
1. Аутентификация на каждом микросервисе
![alt text](image.png)
**Проблемы:**
 - Трудности при синхронизации БД
 - Не получится переиспользовать

2.Работа с пользователями в отдельном микросервисе
![alt text](image-1.png)
**Проблемы:**
 - Микросервисы не знаю какие запросы требуют аутентификации
 - Надо будет для всех сервисов реализовать взаимодействие с микросервисом Auth
## Решение
API Gateway
![alt text](image-2.png)
- Все запросы будут маршрутизироваться через nginx
- Запросы на микросервисы требующие авторзицаии будут перенаправлены в Auth, там получат токен и продолжать свой путь уже с необходимыми данными

## Итог
Выбрал реализацию через API Gateway