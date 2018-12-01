import argparse
import json

argParser = argparse.ArgumentParser(description='Parse the exported JSON host list and produce a .CSV file.')
argParser.add_argument('-if', '--inputfile', help='Input JSON File', required=True) 

args = argParser.parse_args()

with open(args.inputfile, 'r') as inputfile:
    host_list_dict = json.load(inputfile)

totalHosts = 0
outputFile = open('servers.csv', 'w')
outputFile.write('Host Name,Address,Notes,Groups\n')
for host in host_list_dict:
    outputFile.write(host['name'] + ',' + host['address'] + ',' + host['notes'])

    for group in host['groups']:
        outputFile.write(group)

    outputFile.write('\n')

    totalHosts += 1 

print('Total Hosts: ' + str(totalHosts))
