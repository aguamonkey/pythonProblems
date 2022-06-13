#!/usr/bin/env python3


import json

specific_name = "amazing-grace"
vocal_type = "Tenor"
json_dir_name = '/Users/tchdeveloper1/Documents/Coding Practice/pythonProblems/Note Tile Data/{}/GamePA3-NoteTileData-{}-{}.json'.format(specific_name, specific_name, vocal_type)

my_dicts = []

with open(json_dir_name, "r") as file:
    data = json.load(file)


    newDictConcept = {"notes" : [my_dicts]}

print("Checking if frequency key exists in JSON")
#Wellerman relative pitch.


def save_json():
  with open(json_dir_name, 'w') as file:
                json.dump(newDictConcept, file)

for info in data["notes"]:
       # print(info)
        #once you know the associated note value to the relative pitch you can likely append them all
    
          if "relativePitch" in info:
            info["frequency"]= 0.0
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          else:
            print("Nothing else to attach.")
                

#for pf in noteDetails["notes"]:
  #  print(pf['relativePitch'])
  #  for contato in pf["pessoaFisica"]["contatos"]:
  #      print(contato["valor"])  
