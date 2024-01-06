import json
import psycopg2
import psycopg2.extras


def get_postgres_conn():
    with open('src/certs/db_conn.json') as f:
        config_json = json.load(f)
    conn = psycopg2.connect(database=config_json['database'],
                            host=config_json['host'],
                            user=config_json['user'],
                            password=config_json['password'],
                            port=config_json['port'])
    return conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

def get_all_users_for_manager(company_id: int=None, manager_user_id: int=None):
    db_cursor = get_postgres_conn()
    query = f"""
SELECT
    a.username as username,
    a.firstname as firstname,
    a.lastname as lastname
FROM manager_relationships as mr
LEFT JOIN accounts as a
ON mr.employee_user_id = a.user_id
WHERE mr.company_id = {company_id}
AND mr.manager_user_id = {manager_user_id} 
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    return results
    

get_all_users_for_manager(1, 6)
