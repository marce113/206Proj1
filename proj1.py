# Your name: Marcela Passos
# Your student id:32478548
# Your email: marcelap@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): worked with Carolina Janicke and asked chat gpt for help writing test cases and fixing bugs in code
# If you worked with generative AI also add a statement for how you used it.  
# e.g.:
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import csv
import unittest



def csv_loader(filename):

    """

    Load employee data from a CSV file.



    Args:

        filename (str): The name of the CSV file containing employee data.



    Returns:

        dict: A dictionary where each key is an employee ID and each value is another dictionary

        containing demographic categories ('gender', 'race', and 'hire_year') as keys and their corresponding data as row.

        The 'hire_year' is converted into an integer.


    Reminder: use encoding='utf-8-sig' when opening the file.
    """

    inFile = open(filename, encoding = 'utf-8-sig')
    csv_file = csv.reader(inFile)
    next(csv_file)

    outer_d = {} #outer dict
    for row in csv_file:
        gender = row[1] 
        race = row[2]
        hire_year = row[3]
        id = row[0]

        inner_d = {"gender": gender, "race": race, "hire_year": hire_year}
        outer_d[id]= inner_d
    return outer_d


    



def layoff_risk_level_group(employees, dict_risk_framework):

    """

    Split employee data into five different layoff-risk groups based on their hire years.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'hire_year'.

        dict_risk_framework (dict): A dictionary where each key is a layoff risk level and each value is a
        
        tuple containing the earliest hire year associated with that fire risk level and the latest hire year associated with that layoff risk level.


    Returns:

        dict: A dictionary where each key is a layoff risk level and each value is another dictionary containing employee data associated with that layoff risk level.


    """
    
    result= {key: {} for key in dict_risk_framework} #new dict

    for employee_id, employee_data in employees.items(): #iterate through each employee and each set of data
        hire_year= employee_data['hire_year']
        for risk_level, (min_year, max_year) in dict_risk_framework.items(): 
            min_year = int(min_year)
            max_year =int(max_year)
            hire_year = int(hire_year)
            if min_year <= hire_year <= max_year:
                result[risk_level][employee_id] = employee_data
                break

    return result 

    



def race_or_gender_counter(employees):

    """

    Count the number of employees belonging to each race and gender category.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.



    Returns:

        dict: A dictionary containing two keys: 'race' and 'gender'. Each key maps to a sub-dictionary

        with race or gender categories as keys and their corresponding counts as row.



    """
    #race or gender counter

    result= {'race': {}, 'gender': {}} #new dict

    for employee_id, employee_data in employees.items(): #iterate through each employee and each set of data
        #count race
        race_value = employee_data['race']
        if race_value in result['race']:
            result['race'][race_value] += 1
        else:
            result['race'][race_value] = 1

         #count gender
        gender_value = employee_data['gender']
        if gender_value in result['gender']:
            result['gender'][gender_value] += 1
        else:
            result['gender'][gender_value] = 1

    return result 






def race_and_gender_counter(employees):

    """

    Count the number of employees within each combination of race and gender.

    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.

    Returns:

        dict: A dictionary where keys represent combinations of race and gender in the format "Race_Gender",

        and row represent the count of employees within each combination.

    """
    
    result= {} #new dict

    for employee_id, employee_data in employees.items(): #iterate through each employee and each set of data
        #count race gender combos
        race_gender = employee_data['race'] + '_' + employee_data['gender']
        if race_gender in result:
            result[race_gender] += 1
        else:
            result[race_gender] = 1

    return result 





def csv_writer(data, filename):

    """

    Write data to a CSV file.



    Args:

        data (dict): A dictionary containing data to be written to the CSV file.

        filename (str): The name of the CSV file to be created.


    Reminder: use encoding='utf-8-sig' when writing the file.
    """
    with open(filename, mode='w',encoding='utf-8-sig', newline ='')as file:
        writer = csv.writer(file)

        #hard code header
        writer.writerow(['race_and_gender','amount'])

        for race_gender, count in data.items():
            writer.writerow([race_gender, count])
        


#EXTRA CREDIT
def count_employees_by_years_worked(employees):

    """

    Count the number of employees of different years they worked based on each gender and each race.

    

    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.

    Returns:

        dict: A collection of nested dictionaries where the sequential keys are a working year (1976-hiring year), a race, and a gender in that order

        and the innermost row represent the count of employees whose information matches the hire year, race, and gender keys.



    """

    pass




class TestEmployeeDataAnalysis(unittest.TestCase):

    def setUp(self):
       
        #Set up any variables you will need for your test cases
        
        #Feel free to use smaller_dataset.csv for your test cases so that you can verify the correct output

        # pass reoccurig variables as self.blank and then call them using the self. name
        self.inFile = open("smaller_dataset.csv")
        self.csv_file = csv.reader(self.inFile)
        self.my_csvFile = csv_loader("smaller_dataset.csv")
        self.employees = {'employee_1': {'gender': 'Female', 'race': 'White', 'hire_year': 1974},
                    'employee_2': {'gender': 'Male', 'race': 'Black', 'hire_year': 1976},
                    'employee_10': {'gender': 'Male', 'race': 'White', 'hire_year': 1950},
                    'employee_9': {'gender': 'Female', 'race': 'White', 'hire_year': 1953},
                    'employee_8': {'gender': 'Male', 'race': 'White', 'hire_year': 1957},
                    'employee_7': {'gender': 'Female', 'race': 'White', 'hire_year': 1954},
                    'employee_6': {'gender': 'Male', 'race': 'White', 'hire_year': 1963},
                    'employee_5': {'gender': 'Female', 'race': 'White', 'hire_year': 1958},
                    'employee_4': {'gender': 'Male', 'race': 'Black', 'hire_year': 1964},
                    'employee_3': {'gender': 'Female', 'race': 'Black', 'hire_year': 1968}}        



    def test_csv_loader(self):

        # Your test code for csv_loader goes here

        length = len(self.inFile.readlines())-1
    
        
        self.assertEqual(length, 10)
        self.assertEqual(len(self.my_csvFile), 10)
        self.assertEqual(len(self.my_csvFile["employee_1"]), 3)


        # Write a test case that checks for the length of the outer dictionary.

        
        # Write a test case that checks for the length of the inner dictionary value of the first (key, value) pair.



    def test_layoff_risk_level_group(self):
        self.inFile
        self.csv_file
        # Set up the dictionary for the layoff risk level
        layoff_risk_dict = {'Very High': (1970, 1976), 'High': (1964, 1969), 'Medium': (1958, 1963), 'Low': (1954, 1957), 'Very Low': (1950, 1953)}


        result = layoff_risk_level_group(self.employees, layoff_risk_dict)
        # Your test code for layoff_risk_level_group goes here
        #Test that the function correctly puts employees into different layoff risk level groups based on their hire year.

        #checks that employees are grouped evenly
        self.assertEqual(len(result['Very High']), 2)
        self.assertEqual(len(result['High']), 2)
        self.assertEqual(len(result['Medium']), 2)
        self.assertEqual(len(result['Low']), 2)
        self.assertEqual(len(result['Very Low']), 2)

        #checks that example data is correctly grouped
        self.assertIn('employee_2', result['Very High'])
        self.assertIn('employee_3', result['High'])
        self.assertIn('employee_5', result['Medium'])
        self.assertIn('employee_8', result['Low'])
        self.assertIn('employee_10', result['Very Low'])



    def test_race_or_gender_counter(self):

        # Your test code for race_or_gender_counter goes here
        result = race_or_gender_counter(self.employees)
        #Test that there are only two keys in the returned dictionary
        self.assertEqual(len(result), 2)
        #Test that the function accurately counts the number of employees belonging to each race and gender category.
        expected_result = {
            'race' : {'White': 7, 'Black': 3},
            'gender' : {'Female': 5, 'Male': 5}
        }
        self.assertEqual(result, expected_result)


    def test_race_and_gender_counter(self):

        # Your test code for race_and_gender_counter goes here
        result = race_and_gender_counter(self.employees)
        #Test that there are the correct number of keys in the dictionary representing each combination of race and gender in this dataset.
        self.assertEqual(len(result), 4)
        
        # Test that the function correctly counts the number of employees within each combination of race and gender.
        expected_result = {
            'White_Female' : 4,
            'Black_Male' : 2,
            'White_Male' : 3,
            'Black_Female' : 1,
        }
        self.assertEqual(result, expected_result)







#You do not need to change anything in the main() function

def main():

    # Load employee data from the CSV file

    employee_data = csv_loader('GM_employee_data.csv')


    # Task 1: Put employees into different layoff risk level groups based on their hire year
    layoff_risk_level = {'Very High': (1970, 1976), 'High': (1964, 1969), 'Medium': (1958, 1963), 'Low': (1954, 1957), 'Very Low': (1950, 1953)}
    dict_layoff_risk_level = layoff_risk_level_group(employee_data, layoff_risk_level)



    # Task 2: Count employees by race or gender for all employees and for employees whose layoff risk level is "Medium", "Low" or "Very Low"
    employees_not_high_risk = {**dict_layoff_risk_level["Medium"], **dict_layoff_risk_level["Low"], **dict_layoff_risk_level["Very Low"]} 
    race_gender_counts_total = race_or_gender_counter(employee_data)

    
    race_gender_counts_not_high_risk = race_or_gender_counter(employees_not_high_risk)



    # Task 3: Count employees by race and gender combinations for all employees and for employees whose layoff risk level is "Medium", "Low" or "Very Low"

    gendered_race_counts_total = race_and_gender_counter(employee_data)

    gendered_race_counts_not_high_risk = race_and_gender_counter(employees_not_high_risk)



    # Print and interpret the results

    print("Analysis Results:")

    print("--------------------------------------------------------")



    # Task 1: Putting employees into different layoff risk level groups based on their hire year

    print("Task 1: Group Employees by Hire Year")

    print(f"Number of employees hired total: {len(employee_data)}")

    print(f"Number of employees with medium, low or very low risk: {len(employees_not_high_risk)}")

    print("--------------------------------------------------------")



    # Task 2: Comparing race or gender of all employees and employees with medium, low or very low risk

    print("Task 2: Comparing Race and Gender of All Employees and Employees with Medium, Low or Very Low Risk")

    print("Category: All Employees ---> Employees with Medium, Low or Very Low Risk")

    print("Race:")

    for category, count_all in race_gender_counts_total['race'].items():

        count_not_high_risk = race_gender_counts_not_high_risk['race'].get(category, 0)

        print(f"\t{category}: {count_all} ---> {count_not_high_risk}")



    print("Gender:")

    for category, count_all in race_gender_counts_total['gender'].items():

        count_not_high_risk = race_gender_counts_not_high_risk['gender'].get(category, 0)

        print(f"\t{category}: {count_all} ---> {count_not_high_risk}")



    print("--------------------------------------------------------")



    # Task 3: Comparing race and gender combinations for all employees and employees with medium, low or very low risk

    print("Task 3: Comparing Gendered Race Combinations for All Employees and Employees with Medium, Low or Very Low Risk")

    print("Category: All Employees ---> Employees with Medium, Low or Very Low Risk")

    print("Gendered races:")

    for category, count_all in gendered_race_counts_total.items():

        count_not_high_risk = gendered_race_counts_not_high_risk.get(category, 0)

        print(f"\t{category}: {count_all} ---> {count_not_high_risk}")



    print("--------------------------------------------------------")



    csv_writer(gendered_race_counts_total, "GM_employee_data_all_before_layoffs.csv")

    csv_writer(gendered_race_counts_not_high_risk, "GM_employee_data_not_high_risk.csv")






if __name__ == "__main__":

    unittest.main(verbosity=2)
    main()



