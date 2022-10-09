# Stylight Assignment

This is a pre screening assessment test for interested candidates applying for development job at stylight.

## Setting up the project

Clone repository

```bash
  git clone https://<token>@github.com/zmaktr/Stylight.git
  cd stylight
```

Setup Environment

```bash
  pip install virtualenv
  python -m venv venv
  source venv/scripts/activate (Mac)
  venv/scripts/activate (Windows)
```

Install dependancies

```bash
  pip install -r requirements.txt
```

## Setting up Database

Connect your MySQL database to Django

- Locate to root directory file `.env`
- Add your MySQL environment variables

Import DB files to MySQL

- Locate to following directories:

  `./mysql/db.sql`

  `./mysql/migrations.sql`

- Initialise a database by running `db.sql` followed by `migration.sql`. This will result in intended database schema.

## Execute CLI command

This CLI command will result in executing newly developed functionality and will update the db accordingly.

```bash
  py manage.py commands
```

## Assumptions

- Stylight will be running this script multiple time in any particular month or day to notify shop clients about their shop status.
- In the database i have to look for latest month data and perform operations on it. 
- Shops that are currently `offline` due to full budget consumption need not to be notified.

## Tech Stack

**DB Connection:** Django ORM

**CLI:** Django custom commands

**Database:** MySQL

## Change in DB (migrations.sql)

Some change were made in the DB structure to adjust it to limitations of Django ORM. Django doesnt support composite primary keys. So the `t_budgets` table primary key was droped and a new column for primary key was created named `a_id`. This is set to auto-increment field.

A constraint for `t_budget` table was added because primary key was dropped. This is done to ensuring composite unique values for `a_shop_id` and `a_month`.

A new column inside `t_budgets` named `a_notify_at_half` is included to avoid duplicate notifications send to shop clients assuming that script has to be run multiple times.

## Questions

### Does your solution avoid sending duplicate notifications?

For notifications when budget exceeds more than 50% assigned for the month i have added an additional column inside the `t_budget` table named `a_notify_at_half` to deal with this issue. Once the notification is sent for the month the `a_notify_at_half` is marked `True`. If the script is run again it it will check for previous status and wont send duplicate notifications.

For the second part when budget exceeds 100% the shop client is notified and shop status in set to `offline`. So if the script is run again it will check the the shop status if `offline` no duplicate notification is sent.

### How does your solution handle a budget change after a notification has already been sent?

If the budget is changed it would be best to run a script along with the change to taking care of two things

- Check the shop status if the total budget is > than expenditure then set the shop status to `online`
- If the expenditure to date as a percentage of total budget is < 50 percent set `a_notify_at_half` status to `False`

If the above is done correctly my functionality will adopt to the new budget change perfectly.

## Some resourses utilized over the internet

- https://medium.com/@mrjohnkilonzi/using-django-orm-as-a-standalone-ffed6e15bee1

- https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

- https://docs.djangoproject.com/en/4.1/topics/db/queries/

- https://github.com/biammsilva/cli-shops-app

## Author

- [@github](https://www.github.com/zmaktr)
- [@portfolio](https://www.zaeemakhtar.site)
