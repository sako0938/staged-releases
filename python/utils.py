from balena import Balena
from balena.exceptions import RequestError
from pprint import pprint
import sys

import requests


balena = Balena()



def selectAppList():
	apps = balena.models.application.get_all()
	# Print all application names, and allow selection
	print("List of Indexes To Select Target Application: ")
	for i in range(0,len(apps)):
		print("{}: {}".format(i,apps[i]['app_name']))

	selection = int(input("Enter Index:  "))
	target_app = apps[selection]
	print("\n\n")

	target_details = balena.models.application.get_by_id(target_app['id'])
	pprint(target_details)
	return target_app['id']


def getDeviceList(app_id):
	device_list = balena.models.device.get_all_by_application_id(app_id)
	pprint(device_list)
	uuid_list = []
	for dev in device_list:
		# print(dev['uuid'])
		uuid_list.append(dev['uuid'])

	return uuid_list

def getSerialNumbers(device_list):
	for uuid in device_list:
		env_vars = balena.models.environment_variables.device_service_environment_variable.get_all(uuid)
		# pprint(env_vars)
		for env in env_vars:
			if env['name'] == "SERIAL_NUM":
				print("%s\t%s" % (uuid,env['value']) )

if __name__ == '__main__':
	app_id = selectAppList()
	dev_list = getDeviceList(app_id)
	getSerialNumbers(dev_list)