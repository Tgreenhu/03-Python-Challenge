import os
import csv
pyboss = os.path.join("resources", "employee_data.csv")

emp_id = []
full_name = []
first_name = []
last_name = []
dob = []
edited_dob = []
ssn = []
edited_ssn = []
state = []

us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK',
                   'Arizona': 'AZ', 'Arkansas': 'AR',
                   'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE',
                   'Florida': 'FL', 'Georgia': 'GA',
                   'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN',
                   'Iowa': 'IA', 'Kansas': 'KS',
                   'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD',
                   'Massachusetts': 'MA', 'Michigan': 'MI',
                   'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT',
                   'Nebraska': 'NE', 'Nevada': 'NV',
                   'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK',
                   'Oregon': 'OR', 'Pennsylvania': 'PA',
                   'Rhode Island': 'RI', 'South Carolina': 'SC',
                   'South Dakota': 'SD', 'Tennessee': 'TN',
                   'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA',
                   'Washington': 'WA', 'West Virginia': 'WV',
                   'Wisconsin': 'WI', 'Wyoming': 'WY'}

with open(pyboss, "r") as pyboss_file:
    pyboss_reader = csv.reader(pyboss_file, delimiter = ',')
    pyboss_header = next(pyboss_reader)
    for name in pyboss_reader:
        emp_id.append(name[0]) #Get employee IDs
        full_name = name[1].split(" ") #splits names into 2
        first_name.append(full_name[0]) #grabs first name
        last_name.append(full_name[1]) #grabs last name
        dob = name[2].split("-") #split dob to just grab year, month, day
        edited_dob.append(dob[1] + "/" + dob[2] + "/" + dob[0]) #edit our dates accordingly
        ssn = name[3].split("-") #split ssn to just grab numbers
        edited_ssn.append("***-**-" + ssn[2]) #edit ssn to have stars for all but the last 3 numbers
        state.append(us_state_abbrev[name[4]]) #change states to their abbreviations

pyboss_new = zip(emp_id, first_name, last_name, edited_dob, edited_ssn, state) #zip all needed info together

pyboss_conversion = os.path.join("analysis", "pyboss_conversion.csv") #make a new csv
with open(pyboss_conversion, "w") as pyboss_final:
    pyboss_writer = csv.writer(pyboss_final, delimiter = ",")
    header = ['Employee ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    pyboss_writer.writerow(header)
    pyboss_writer.writerows(pyboss_new)