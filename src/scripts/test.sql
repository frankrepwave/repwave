SELECT 
a.firstname,
a.lastname,
c.company_name,
cr.role
FROM accounts as a
LEFT JOIN companies as c
ON a.company_id = c.company_id
LEFT JOIN company_roles as cr
ON a.role_id = cr.role_id;