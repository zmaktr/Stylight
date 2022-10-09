# Stylight Assignment

This is a prescreening assesment test for intrested candidates applying for development job at stylight.

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

This CLI command will result in implementing newly developed functionality for this assignment

```bash
  py manage.py commands
```

## Assumptions

- Stylight will be running this script multiple time in any particular month or day to update shop clients about their shop status.
- In the database we have to look for the latest month data and only do operations on it.
- Shops that are currently `offline` for the latest month due to full budget consumption need not to be notified.

## Tech Stack

**DB Connection:** Django ORM

**CLI:** Django custom commands

**Database:** MySQL

## Change in DB (migrations.sql)

Some change were made in the DB structure to adjust it to limitations of Django ORM. Django doesnt support composite primary keys. So the `t_budgets` pk was droped and a new column for auto-increment pk was created named `a_id`.

A constraint for `t_budget` table was added because pk was dropped. This is done to ensuring composite unique values for `a_shop_id` and `a_month`.

A new column inside `t_budgets` named `a_notify_at_half` is included to avoid duplicate notifications send to shop clients each time the script is run for a particular month.

## Questions

### Does your solution avoid sending duplicate notifications?

For notifications when budget exceeds more than 50% assigned for the current month i have added an additional column inside the `t_budget` table named `a_notify_at_half` to deal with this issue. Once the notification is sent for the current month the shop is marked `True`. If the script is run again it it will check for previous status and wont send duplicate notifications.

For the second part when budget exceeds 100% the shop client is notified and shop status in set to `offline` inside the `t_shops` table \. So if the script is run again it will check the the shop status if `offline` no duplicate notification is sent.

### How does your solution handle a budget change after a notification has already been sent?

If the budget is changed it would be best to run a script along with it taking care of two things

- Check the shop status if the total budget is > than expenditure set the shop status to `online`
- If the expenditure to date as a percentage of total budget is < 50 set `a_notify_at_half` status to `False`

If the above is done correctly my functionality will adopt to the system change perfectly.

## Some resourses utilized over the internet

- https://medium.com/@mrjohnkilonzi/using-django-orm-as-a-standalone-ffed6e15bee1

- https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

- https://docs.djangoproject.com/en/4.1/topics/db/queries/

- https://github.com/biammsilva/cli-shops-app

## Author

- [@github](https://www.github.com/zmaktr)
- [@portfolio](https://www.zaeemakhtar.site)
