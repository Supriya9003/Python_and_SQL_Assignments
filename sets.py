# ==========================================
# Task 1: Student Enrollment Analysis
# ==========================================

python_students = {"Ravi", "Anu", "Sai", "Kiran", "Teja"}
sql_students = {"Sai", "Teja", "Rahul", "Anu", "Priya"}

# 1. Find students enrolled in both courses.
both_courses = python_students & sql_students
print("Students enrolled in both courses:", both_courses)

# 2. Find students enrolled only in Python.
only_python = python_students - sql_students
print("Students enrolled only in Python:", only_python)

# 3. Find students enrolled only in SQL.
only_sql = sql_students - python_students
print("Students enrolled only in SQL:", only_sql)

# 4. Find all students enrolled in either course.
either_course = python_students | sql_students
print("Students enrolled in either course:", either_course)

# 5. Find students enrolled in exactly one course.
exactly_one_course = python_students ^ sql_students
print("Students enrolled in exactly one course:", exactly_one_course)


# ==========================================
# Task 2: Employee Skills Management
# ==========================================

team_a_skills = {"Python", "SQL", "Git", "Docker"}
team_b_skills = {"Java", "SQL", "AWS", "Git"}

# 1. Find common skills between the teams.
common_skills = team_a_skills & team_b_skills
print("\nCommon skills between the teams:", common_skills)

# 2. Find skills available only in Team A.
only_team_a = team_a_skills - team_b_skills
print("Skills available only in Team A:", only_team_a)

# 3. Find skills available only in Team B.
only_team_b = team_b_skills - team_a_skills
print("Skills available only in Team B:", only_team_b)

# 4. Find all skills available in the organization.
all_skills = team_a_skills | team_b_skills
print("All skills available in the organization:", all_skills)

# Additional requirement: Add Linux to Team A and remove Java from Team B.
team_a_skills.add("Linux")
team_b_skills.discard("Java")
print("Team A after adding Linux:", team_a_skills)
print("Team B after removing Java:", team_b_skills)

#================================================
# Task 3: Online Store Customers
# ===============================================

amazon_customers = {"Ravi", "Anu", "Kiran", "Sai", "Teja"}
flipkart_customers = {"Sai", "Teja", "Rahul", "Priya", "Anu"}

# 1. Customers who purchased from both stores.
both_stores = amazon_customers & flipkart_customers
print("\nCustomers who purchased from both stores:", both_stores)

# 2. Customers who purchased only from Amazon.
only_amazon = amazon_customers - flipkart_customers
print("Customers who purchased only from Amazon:", only_amazon)

# 3. Customers who purchased only from Flipkart.
only_flipkart = flipkart_customers - amazon_customers
print("Customers who purchased only from Flipkart:", only_flipkart)

# 4. All unique customers.
all_unique_customers = amazon_customers | flipkart_customers
print("All unique customers:", all_unique_customers)

# 5. Customers who purchased from exactly one store.
exactly_one_store = amazon_customers ^ flipkart_customers
print("Customers who purchased from exactly one store:", exactly_one_store)

# =======================================
# 4. Programming Languages Survey
# =======================================

Batch_1 = {"Python", "Java", "C", "SQL"}
Batch_2 = {"Python", "Java", "React", "JavaScript"}

# 1. Languages known by both the batches (Intersection)
both_batches = Batch_1 & Batch_2
print("Known by both the batches:", both_batches)

# 2. Languages known only by Batch 1 (Difference)
only_batch_1 = Batch_1 - Batch_2
print("Known only by batch 1:", only_batch_1)

# 3. Languages known only by Batch 2 (Difference)
only_batch_2 = Batch_2 - Batch_1  
print("Known only by Batch 2:", only_batch_2)

# 4. Check whether Batch 1 is a subset of Batch 2
is_subset = Batch_1.issubset(Batch_2)
print("Is Batch 1 a subset of Batch 2:", is_subset)

# 5. Check whether Batch 2 is a superset of Batch 1
is_superset = Batch_2.issuperset(Batch_1)
print("Is Batch 2 a superset of Batch 1:", is_superset)

# ===================================
# 5. Website visitor analysis
# ===================================

day1_visitors = {"user1", "user2", "user3", "user4", "user5"}
day2_visitors = {"user3", "user4", "user5", "user6", "user7"}

# 1. Returning visitors (Intersection)
returning_visitors = day1_visitors & day2_visitors
print("Returning visitors:", returning_visitors)

# 2. Visitors who visited only on Day 1 (Difference)
only_day1 = day1_visitors - day2_visitors
print("Only Day 1 visitors:", only_day1)

# 3. Visitors who visited only on Day 2 (Difference)
only_day2 = day2_visitors - day1_visitors
print("Only Day 2 visitors:", only_day2)

# 4. All unique visitors across both days (Union)
all_visitors = day1_visitors | day2_visitors
print("All unique visitors:", all_visitors)

# 5. Visitors who visited on exactly one day (Symmetric Difference)
exactly_one_day = day1_visitors ^ day2_visitors
print("Exactly one day visitors:", exactly_one_day)
