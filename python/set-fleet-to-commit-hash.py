# import balena
from balena import Balena
from pprint import pprint
balena = Balena()

apps = balena.models.application.get_all()

# Print all application names, and allow selection
print("List of Indexes To Select Target Application: ")
for i in range(0,len(apps)):
	print("{}: {}".format(i,apps[i]['app_name']))

selection = int(input("Enter Index:  "))
target_app = apps[selection]
print("Selected Application: {} with app_id: {}".format(target_app['app_name'],target_app['id']))

print("\n\n")

balena.models.application.get_by_id(target_app['id'])

commit_hash = input("Enter Target Commit Hash For {}'s Fleet:  ".format(target_app['app_name']))
print(commit_hash)
# balena.models.application.set_to_release('5685', '7dba4e0c461215374edad74a5b78f470b894b5b7')