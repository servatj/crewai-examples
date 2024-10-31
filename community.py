import re
import ast

text = "[ { fuzziness: 0.1, search_profile: '95b01e80-5744-4c72-927e-47672ebd445a', entity_type: 'vessel', tags: { 'Vessel IMO': '8625545' } } ]"

tags = re.compile(r"tags:\s*({.*?})", re.I).search(text).groups()[0]
tags_to_json = ast.literal_eval(tags.replace("'", '"'))
vessel_imo = tags_to_json['Vessel IMO']
vessel_flag = tags_to_json.get('Vessel flag', None)


entity_type = re.compile(r"entity_type:\s*'([^']*)'", re.I).search(text).groups()[0]

print(entity_type)
print(vessel_imo)
