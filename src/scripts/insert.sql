INSERT INTO accounts (username, password, firstname, lastname, email, company_id, role_id, created_on, last_login)
VALUES  ('frankliang', 'password123', 'Frank', 'Liang', 'frank@repwave.ai', 1, 1, NOW(), NOW()),
        ('edwinsaraccini', 'password345', 'Edwin', 'Saraccini', 'edwin@repwave.ai', 1, 1, NOW(), NOW()),
        ('jamesmorales', 'password567', 'James', 'Morales', 'james@repwave.ai', 1, 2, NOW(), NOW()),
        ('waleedbaig', 'password789', 'Waleed', 'Baig', 'waleed@repwave.ai', 1, 2, NOW(), NOW())
RETURNING accounts.user_id;

INSERT INTO companies (company_name, created_on)
VALUES ('Repwave', NOW())
RETURNING company_id;

INSERT INTO company_roles(company_id, role)
VALUES  (1, 'Sales Manager'), 
        (1, 'Sales Representative')
RETURNING role_id;

INSERT INTO manager_relationships (employee_user_id, manager_user_id, company_id)
VALUES  (7, 5, 1), (8, 6, 1);