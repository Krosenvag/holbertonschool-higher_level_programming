# SQL_introduction

This project is an introduction to SQL and relational databases using MySQL. It covers the basics of database creation, table manipulation, data insertion, selection, updating, and deletion, as well as more advanced queries involving grouping and aggregation.

## Project Structure

- **0-list_databases.sql**: Lists all databases on the MySQL server.
- **1-create_database_if_missing.sql**: Creates the database `hbtn_0c_0` if it does not exist.
- **2-remove_database.sql**: Deletes the database `hbtn_0c_0` if it exists.
- **3-list_tables.sql**: Lists all tables in a given database.
- **4-first_table.sql**: Creates a table called `first_table` in the current database.
- **5-full_table.sql**: Shows the full description of the table `first_table`.
- **6-list_values.sql**: Lists all rows of the table `first_table`.
- **7-insert_value.sql**: Inserts a new row into the table `first_table`.
- **8-count_89.sql**: Displays the number of records with `id = 89` in `first_table`.
- **9-full_creation.sql**: Creates a table `second_table` and adds multiple rows.
- **10-top_score.sql**: Lists all records of `second_table` ordered by score (descending).
- **11-best_score.sql**: Lists all records with a score >= 10 in `second_table`.
- **12-no_cheating.sql**: Updates the score of a record in `second_table`.
- **13-change_class.sql**: Removes all records with a score <= 5 in `second_table`.
- **14-average.sql**: Computes the average score of all records in `second_table`.
- **15-groups.sql**: Lists the number of records with the same score in `second_table`.
- **16-no_link.sql**: Lists all records of `second_table` where the name is not null.

## Usage

Each `.sql` file contains a single SQL statement or a set of statements that can be executed using the MySQL command line:

```sh
cat [0-list_databases.sql](http://_vscodecontentref_/0) | mysql -u <username> -p
```