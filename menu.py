import inquirer
from findsku import fetch_virtual_machine_sku_prices
from tabulate import tabulate

data = fetch_virtual_machine_sku_prices()
software_licenses = data['softwareLicenses']
keys = software_licenses[0].keys()

print(type(software_licenses))
print(type(keys))


# Create a list of software licenses
license_choices = [(sl.get('displayName','Windows'),sl['slug'])  for sl in software_licenses]

license_questions = [
  inquirer.List('selected_os_software',
                    message="Please select the OS/Software",
                    choices=license_choices,
                    ),
]
software_license_answers = inquirer.prompt(license_questions)
print(f"Selected OS/Software: {software_license_answers['selected_os_software']}")


categories= data['dropdown']
# Create a list of software licenses
category_choices = [(ca.get('displayName','all'),ca['slug'])  for ca in categories]

category_questions = [
  inquirer.List('selected_category',
                    message="Please select the Category",
                    choices=category_choices,
                    ),
]
category_answers = inquirer.prompt(category_questions)
print(f"Selected OS/Software: {category_answers['selected_category']}")
selected_category_answer = category_answers['selected_category']


vm_series_info = [c for c in categories if c.get('slug') == selected_category_answer][0]
vm_series = vm_series_info['series']


series= data['dropdown']
# Create a list of software licenses
vm_series_choices = [(vs.get('displayName','all'),vs['slug'])  for vs in vm_series]

vm_series_questions = [
  inquirer.List('selected_vm_series',
                    message="Please VM Series",
                    choices=vm_series_choices,
                    ),
]
vm_series_answers = inquirer.prompt(vm_series_questions)
selected_vm_series_answer = vm_series_answers['selected_vm_series']
print(f"Selected VM Serie: {selected_vm_series_answer}")

vm_serie = [vs for vs in vm_series if vs.get('slug') == selected_vm_series_answer][0]


instances = vm_serie['instances']
table_headers = instances[0].keys()
table_rows = [vs.values() for vs in instances]
print(tabulate(table_rows, headers=table_headers, tablefmt="grid"))
