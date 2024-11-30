from mysql import connector 

my_connection= connector.connect(
    host="localhost",
    user="root",
    password="secret_password",
    database="employees")
my_cursor= my_connection.cursor()


# 1. Find the city of the employees in the IT department

my_cursor.execute("""
    SELECT emp.last_name, dep.department_name, loc.city
    FROM employees emp INNER JOIN departments dep ON emp.department_id = dep.department_id
    INNER JOIN locations loc ON dep.location_id = loc.location_id
    WHERE  dep.department_name = 'IT';    
""")

print("{:10} {:10} {:10}".format("Last Name", "Department", "city"),)
for row in my_cursor:
    print(f"{row[0]:40}{row[1]:40}{row[2]:<4}")


# 2. Find the number of employees in each city and order in descending order

my_cursor.execute("""
    SELECT loc.city, COUNT(emp.department_id)
    FROM employees emp INNER JOIN departments dep ON emp.department_id = dep.department_id
    INNER JOIN locations loc ON loc.location_id = dep.location_id
    GROUP BY loc.city
    ORDER BY loc.city DESC;          
""")

print("{:24} {:16}".format("City", "Number of Employees"))
for row in my_cursor:
    print(f"{row[0]:24} {row[1]:<16}")


# 3. Find the number of employees in each job title and order in descending order

my_cursor.execute(""" 
    SELECT job.job_title, COUNT(emp.job_id)
    FROM  jobs job INNER JOIN employees emp ON job.job_id = emp.job_id
    GROUP BY job.job_title
    ORDER BY job.job_title DESC;
""") 

print("{:24} {:16} ".format("Job Title",  "Number employees")) 
for row in my_cursor: 
    print(f"{row[0]:24} {row[1]:<16} ") 


# 4. Find the employees in UK and CANADA only

my_cursor.execute(""" 
    SELECT CONCAT(emp.first_name,' ',emp.last_name),loc.city, coun.country_name 
    FROM employees emp
    INNER JOIN departments dep ON emp.department_id = dep.department_id
    INNER JOIN locations loc ON dep.location_id = loc.location_id
    INNER JOIN countries coun ON loc.country_id = coun.country_id
    WHERE coun.country_name = 'United Kingdom' or coun.country_name = 'Canada'
""")     

print("{:32} {:4} {:100}".format("first name + Last Name", "City", "country")) 
for row in my_cursor: 
    print(f"{row[0]:32} {row[1]:4} {row[2]:<100}") 


# 5. Find and average salary in every City

my_cursor.execute(""" 
    SELECT loc.city, AVG(emp.salary)
    FROM employees emp INNER JOIN departments dep ON emp.department_id = dep.department_id
    INNER JOIN locations loc ON loc.location_id = dep.location_id
    GROUP BY loc.city
    ORDER BY loc.city ASC;    
""") 

print("{:32} {:4}".format("City", "Average Salary")) 
for row in my_cursor: 
    print(f"{row[0]:32} {row[1]:<4}") 
