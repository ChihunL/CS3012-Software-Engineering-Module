from github import Github
import sqlite3
from sqlite3 import Error
import csv


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_table(conn, project_names):
 
    sql = ''' INSERT INTO projectNames(projectName)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, project_names)
    return cur.lastrowid

def create_repo_list(conn, repo_list):
 
    sql = ''' INSERT INTO projectNames(projectName)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, repo_list)
    return cur.lastrowid

if __name__ == '__main__':

    username = raw_input('Enter in Username: ')
    password = raw_input('Enter in Password: ')

    g = Github(username, password)

    with open('repoNames.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

    
        for repo in g.get_user().get_repos():
            filewriter.writerow([repo.name])
