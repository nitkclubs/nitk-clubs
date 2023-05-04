*codes in mysql*

`create database nitk_clubs;`

`create user nitk_clubs_user@localhost IDENTIFIED By 'nitk_clubs_password';`

`grant all privileges on nitk_clubs.* to nitk_clubs_user@localhost;`

`flush privileges;`

*codes in termial after mysql*

```
cd club_management;
python manage.py makepigrations;
python manage.py migrate;

python manage.py runserver;
```

*references*
