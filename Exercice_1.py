# Elvis Basic
# Exercice 1
import json
import csv
with open('data.json', 'r') as fichier_json
data = json.load(json_file)
with open('num_complexes.csv', 'w', newline='') as fichier_csv
writer = csv.writer(fichier_csv)
<<<<<<< HEAD
<<<<<<< HEAD
=======
data = json.load(fichier_json)
>>>>>>> 9bc0328f0dcc385eab2c61fcc64971ef752bf197
writer = csv.writer(fichier_csv)
with open('num_complexes.csv', 'w', newline='') as fichier_csv
writer = csv.writer(fichier_csv)
 writer.writerow(['reel', 'imaginaire'])
=======

>>>>>>> b2b396e37e995e0dcfa83f9672219291794d93f5
 writer.writerow(['reel', 'imaginaire'])
for num_complexe in data:
        writer.writerow(num_complexe)
=======
writer.writerow(['reel', 'imaginaire'])
>>>>>>> 036ceff6fd68945ec5d40d31e251f61bf512dc11
for num_complexe in data:
        writer.writerow(num_complexe)
