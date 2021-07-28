import json
import os
import csv

folderPath = "C:\\Users\\Janam\\Desktop\\j\\folder"

jsonFiles = os.listdir(folderPath)
jsonFiles = [jsonFile for jsonFile in jsonFiles if ".json" in jsonFile]

with open('mycsv.csv', 'w', newline='') as f:
    colNames = ['Repo', 'file_name_column', 'line_column', 'expected_value_column', 'actual_value_column', 'severity_column']
    writer = csv.DictWriter(f, fieldnames=colNames)
    writer.writeheader()

    for jsonFile in jsonFiles:
        readJsonFile = open(folderPath + '\\' + jsonFile, 'r')
        jsonData = readJsonFile.read()

        mainDict = json.loads(jsonData)
        queries = mainDict['queries']
        for queryDictionary in queries:

            files = queryDictionary['files']

            for filesDictionary in files:
                writer.writerow({'Repo': str(jsonFile.replace('.json', '')), 'file_name_column': str(filesDictionary['file_name']), 'line_column': str(filesDictionary['line']), 'expected_value_column': str(filesDictionary['expected_value']), 'actual_value_column': str(filesDictionary['actual_value']), 'severity_column': str(queryDictionary['severity'])})
