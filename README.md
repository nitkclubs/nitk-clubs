*codes in mysql*

`create database nitk_clubs;`

`create user nitclubs_user@localhost IDENTIFIED By 'nitclubs_password';`

`grant all privileges on nitclubs.* to nitk_clubs_user@localhost;`

`flush privileges;`

*codes in termial after mysql*

```
python manage.py makepigrations;
python manage.py migrate;

python manage.py runserver;
```

*references*
