employee_list = [ {"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12456, "name": "Paul", "department": "House Floor"}, {"id": 12478, "name": "Sarah", "department": "Management"}, {"id": 12434, "name": "Lisa", "department": "Cold Storage"}, {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"}, {"id": 12419, "name": "Gill", "department": "Cashier"} ]  
  
def mod(employee):  
  temp = employee['name'] + "_" + employee["department"]  
  return temp  
  
def to_mod_list(employee_list):  
  return list(map(mod, employee_list))  
  
def generate_usernames(mod_list):  
  return [item.replace(" ", "_") for item in mod_list]  
  
def map_id_to_initial(employee_list):
    initials_dict = {}
    for employee in employee_list:
        name = employee["name"]
        first_initial = name[0] 
        initials_dict[first_initial] = employee["id"]
    return initials_dict

  
def main():  
  mod_emp_list = to_mod_list(employee_list)  
  print("Modified employee list: " + str(mod_emp_list) + "\n")  
  print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")  
  print(f"Initials : {map_id_to_initial(employee_list)}")  
  
if __name__ == "__main__":  
  main()
