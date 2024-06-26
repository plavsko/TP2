# Elvis Basic
# Exercice 1

import json
import csv

with open('data.json', 'r') as fichier_json:
    data = json.load(fichier_json)

with open('num_complexes.csv', 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)

    writer.writerow(['reel', 'imaginaire'])

    for num_complexe in data:
        writer.writerow(num_complexe)
