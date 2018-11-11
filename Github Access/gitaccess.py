from github import Github
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()



if __name__ == '__main__':

    username = raw_input('Enter in Username: ')
    password = raw_input('Enter in Password: ')

    g = Github(username, password)

    create_connection("RepositoriesNames.db")
    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)