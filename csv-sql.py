import csv

filename = "companies2.csv"
table_name = "companies"
create_table_query = ""
insert_queries = []

with open(filename, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    # Stripping any whitespace from headers
    headers_sql = [f"`{header.strip()}`" for header in headers]
    column_definitions = [f"`id` INT AUTO_INCREMENT PRIMARY KEY"]
    column_definitions.extend([f"{header_sql} TEXT" for header_sql in headers_sql])
    create_table_query = f"CREATE TABLE {table_name} ({', '.join(column_definitions)});"

    for row in reader:
        values = []
        for item in row:
            if item == "":
                values.append("NULL")
            else:
                # Escape backslashes for SQL
                item_escaped = item.replace("\\", "\\\\")
                # Escape single quotes for SQL
                item_escaped = item_escaped.replace("'", "''")
                values.append(f"'{item_escaped}'")
        query = f"INSERT INTO {table_name} ({', '.join(headers_sql)}) VALUES ({', '.join(values)});"
        insert_queries.append(query)

with open("output.sql", "w", encoding='utf-8') as outfile:
    outfile.write(create_table_query + "\n\n")
    outfile.write("\n".join(insert_queries))

print("SQL file generated as output.sql")
