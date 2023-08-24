# Соцсеть Yatube

Социальная сеть блогеров. 
С такими функционалом как: создание постов, их комментирование и добавление в группы. Так же подписка на авторов и лента с вашими подписками.

## Инструкции по установке
Клонируем репозиторий:
```
git clone git@github.com:nikitaloshch/hw05_final.git
```

Установим и активируем виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```

Установим зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Применим миграции:
```
python manage.py migrate
```

В директории с manage.py выполним команду:
```
python manage.py runserver
```
