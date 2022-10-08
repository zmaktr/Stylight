ALTER TABLE t_budgets DROP PRIMARY KEY;
ALTER TABLE t_budgets ADD a_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE t_budgets ADD CONSTRAINT unique_budget UNIQUE (a_shop_id, a_month);
ALTER TABLE t_budgets ADD a_notify_at_half BOOLEAN;

