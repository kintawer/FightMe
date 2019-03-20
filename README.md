# Проект FightMe!

Django приложение для участия в турнирах и дуэлях в играх жанра файтинги. 

## О проекте

Суть данного проекта заключается в создании такого веб-приложения,
 в котором игроки в игры жанра файтинги могли бы соревноваться друг
 с другом, забивать друг другу дуэли, участвовать в турнирах, иметь 
 рейтинг, возможно, какой-либо еще функционал, который появится по мере
 развития проекта
 
## Используемый стек
+ Пишем на последней релизной на данный момент версии **Python 3.6**.
+ Backend на **Django**, хотелось бы прикрутить **async.io** дабы 
не отходить от тренда асинхронности.
+ Естественно придерживаемся **REST** архитектуры с помощью **restframework**.
+ База данных **PostgreSQL**.
+ Хотелось бы прикрутить **ElasticSearch**.
+ Frontend пишем на **React**, т.к. появилась русская дока и довольно распространенная вещь.
+ Поначалу разработка будет в локальном venv, но в дальнейшем будет 
**Docker** (надеюсь).

Список выбранных технологий основан чисто на текущих трендах в мире веб-разработки. 
*Данный стек будет пополняться*.

## Основные фичи
+ Приоритетная задача - поиск/вызов соперника на поединок при определенных игроками условиями,
 результат которого, при несогласии сторон, будет решаться судьей, данный процесс еще требует доработки.
+ Ведение рейтинга игрока по результатом сыграных игр.
+ Регистрация и проведение турниров.
+ Игры на деньги / инвентарь стима / %вещьнейм%.
+ Авторизация с помощью всех социальных сетей, стима, google.

## Участие в проекте
Используем доску в [trello](https://trello.com/b/mf1f92L4). Доска публичная, 
но чтобы в ней работать нужно добавиться в команду, для этого напишите
мне в [Telegram](https://t.me/murakami2).