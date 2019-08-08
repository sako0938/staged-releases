# import balena
from balena import Balena
from balena.exceptions import RequestError
from pprint import pprint
import sys
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

target_details = balena.models.application.get_by_id(target_app['id'])

pprint(target_details)

if target_details['should_track_latest_release'] == True:
	print("This application fleet is tracking the latest release, please disable this before continuing!")
	sys.exit(0)
else:
	target_hash = balena.models.application.get_target_release_hash(target_app['id'])
	print("This application's fleet is currently following commit: {}".format(target_hash) )

commit_hash = input("Enter Target Commit Hash For {}'s Fleet:  ".format(target_app['app_name']))
print(commit_hash)
try:
	balena.models.application.set_to_release(target_app['id'], commit_hash)
except RequestError:
	print("Error Setting Release, Double-Check Commit Hash!")
target_hash = balena.models.application.get_target_release_hash(target_app['id'])
print("This application's fleet is now following commit: {}".format(target_hash) )