CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
    firstname VARCHAR ( 50 ) NOT NULL,
    lastname VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
    company_id INT NOT NULL,
    role_id INT NOT NULL,
	created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP,
    FOREIGN KEY (company_id)
        REFERENCES companies (company_id),
    FOREIGN KEY (role_id)
        REFERENCES company_roles (role_id)
);

CREATE TABLE companies (
	company_id serial PRIMARY KEY,
	company_name VARCHAR ( 50 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL
);

CREATE TABLE company_roles (
    role_id serial PRIMARY KEY,
    company_id INT NOT NULL,
    role VARCHAR (50) NOT NULL,
    FOREIGN KEY (company_id)
      REFERENCES companies (company_id)
);

CREATE TABLE manager_relationships (
    employee_user_id INT NOT NULL,
    manager_user_id INT NOT NULL,
    company_id INT NOT NULL,
    FOREIGN KEY (employee_user_id)
        REFERENCES accounts (user_id),
    FOREIGN KEY (manager_user_id)
        REFERENCES accounts (user_id),
    FOREIGN KEY (company_id)
      REFERENCES companies (company_id)
);