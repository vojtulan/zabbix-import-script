import json
import copy

print("Script has started")

with open("./host_templates/template.json", "r") as f:
     hostTemplate = json.load(f)

with open("full_template.json", "r") as e:
     import_template = json.load(e)

with open("names.txt") as g:
     names =  g.read().splitlines()

with open("descriptions.txt") as h:
     descriptions = h.read().splitlines()

with open("ips.txt") as j:
     ips = j.read().splitlines()





numHost = sum(1 for line in open('names.txt'))
numDesc = sum(1 for line in open('descriptions.txt'))
numIp = sum(1 for line in open('ips.txt'))

print("Number of names: ", numHost)
print("Number of descriptions: ", numDesc)
print("Number of ips: ", numIp)

result = ""
output = ""
i = 0
for line in names:
   temp = copy.deepcopy(hostTemplate)
   host = names[i]
   desc = descriptions[i]
   ip = ips[i]
   temp['host'] = host
   temp['name'] = host
   temp['interfaces'][0]['ip'] = ip
   temp['description'] = desc
   result = result + json.dumps(temp) + ", "
   i = i + 1

result = result[:-2]
with open("import.json", "w") as json_out:
   json_out.write(result)

print("Done")