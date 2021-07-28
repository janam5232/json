import json
import os
import csv

rows = []
repo = []
file_name_column = []
line_column = []
expected_value_column = []
actual_value_column = []
severity_column = []

folderPath = "C:\\Users\\Janam\\Desktop\\j\\folder"

jsonFiles = os.listdir(folderPath)
jsonFiles = [jsonFile for jsonFile in jsonFiles if ".json" in jsonFile]

for jsonFile in jsonFiles:
    readJsonFile = open(folderPath + '\\' + jsonFile, 'r')
    jsonData = readJsonFile.read()

    mainDict = json.loads(jsonData)
    queries = mainDict['queries']
    for queryDictionary in queries:
        severity_column.append(queryDictionary['severity'])

        files = queryDictionary['files']

        for filesDictionary in files:
            file_name_column.append(str(filesDictionary['file_name']))
            line_column.append(str(filesDictionary['line']))
            expected_value_column.append(str(filesDictionary['expected_value']))
            actual_value_column.append(str(filesDictionary['actual_value']))
            repo.append(str(jsonFile.replace('.json', '')))
        severity_column.append(str(queryDictionary['severity']))

with open('mycsv.csv', 'w', newline='') as f:
    colNames = ['Repo', 'file_name_column', 'line_column', 'expected_value_column', 'actual_value_column', 'severity_column']
    writer = csv.DictWriter(f, fieldnames=colNames)

    writer.writeheader()
    for rowValues in range(0, len(file_name_column)):
        writer.writerow({'Repo': repo[rowValues], 'file_name_column': file_name_column[rowValues], 'line_column': line_column[rowValues], 'expected_value_column': expected_value_column[rowValues], 'actual_value_column': actual_value_column[rowValues], 'severity_column': severity_column[rowValues]})
f.close()
