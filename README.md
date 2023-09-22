Python Script Description: SQL Generator from CSV

#Script Purpose:
This script processes a CSV file and generates an SQL file containing statements to create a table and insert the data from the CSV into that table.

#Functional Overview:

    CSV File Input: The script is designed to read from a csv file located in the same directory.

    Table Creation: It begins by reading the headers of the CSV and constructs a CREATE TABLE SQL statement. An additional column, id, is added to the table as an auto-incrementing primary key.

    #Data Insertion:
        Each row of the CSV is read, and an INSERT INTO SQL statement is constructed for it.
        Special characters in the data, such as backslashes (\) and single quotes ('), are properly escaped to ensure the generated SQL is valid.
        If a cell in the CSV is empty, it's represented as NULL in the SQL.

    #SQL File Output:
        The constructed SQL statements are written to an output file named "output.sql".
        The file begins with the CREATE TABLE statement followed by all the INSERT INTO statements.

    Feedback: Upon successful completion, the script prints a message indicating that the SQL file has been generated.

#Usage:
Place the script in the same directory as the "csv" file and run it. After execution, an "output.sql" file will be generated in the same directory, containing the SQL representation of the CSV data.
