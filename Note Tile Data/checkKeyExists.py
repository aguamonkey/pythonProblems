#!/usr/bin/env python3


import json

specific_name = "april"
json_dir_name = '/Users/tchdeveloper1/Documents/Coding Practice/Note Tile Data/{}/GamePA3-NoteTileData-{}-Bass.json'.format(specific_name, specific_name)

my_dicts = []

with open(json_dir_name, "r") as file:
    data = json.load(file)


    newDictConcept = {"notes" : [my_dicts]}

print("Checking if frequency key exists in JSON")
for info in data["notes"]:
       # print(info)

         if "frequency" in info:
            print("Key exist in JSON data")
            info["noteName"]= "A"
         #   print(info)
            arrayMy = [info]
            arrayMy.append(info)
          #  print(arrayMy)

            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            print(my_dicts)
            with open(json_dir_name, 'w') as file:
                json.dump(newDictConcept, file)
    #         varTest = ""
        #    print(noteDetails["notes"], "marks is: ", noteDetails["notes"])
         else:
             print("Key doesn't exist in JSON data")

#for pf in noteDetails["notes"]:
  #  print(pf['relativePitch'])
  #  for contato in pf["pessoaFisica"]["contatos"]:
  #      print(contato["valor"])  
