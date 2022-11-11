programming_dictionary = {
 "Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "Action of doing something over and over again"

# print(programming_dictionary)

# empty_dictianory = {}

for key in programming_dictionary:
    print(key)  # keys
    print(programming_dictionary[key])  # values

"""Grades"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# print(student_scores)

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    # print(score)
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

   
print(student_grades)


capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested dict in a dict

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Italy": {"cities_visited": ["Rome", "Traviso", "Palermo", "Catania"], "pizzas_eatten": 30}}


# # Nested Dict in a list

travel_log = [

    {"country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12},
    
    {"country": "Italy", 
    "cities_visited": ["Rome", "Traviso", "Palermo", "Catania"], 
    "pizzas_eatten": 30}]



travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_land = {}
    new_land["country"] = country_visited
    new_land['visits'] = times_visited
    new_land["cities"] = cities_visited
    travel_log.append(new_land)




add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Italy", 5, ["Rome", "Traviso", "Palermo", "Catania"])
print(travel_log)


