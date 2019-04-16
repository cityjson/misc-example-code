import os
import sys
import json
import jsonschema
import jsonref


def findadd(n):
    if ( (type(n) is dict) or (type(n) is jsonref.JsonRef) ):
        # print (n)
        if "attributes" in n:
            print("YESSSS")
        for p in n:
            if ( (type(n[p]) is list) or (type(n[p]) is dict) ):
                findadd(n[p])
            # else:
                # print("---", n[p])
    elif (type(n) is list):
        for each in n:
            if ( (type(each) is dict) or (type(each) is jsonref.JsonRef) or (type(each) is list) ):
                # print(each)
                # sys.exit()
                findadd(each)
            # else:
                # print("-->", each)
    # else:
        # print("***", type(n), n)

        # if "attributes" in n:
        #     print(n)
        # else:


root_schema = '/Users/hugo/projects/cityjson/schemas/cityjson.schema.json'
fins = open(root_schema)

abs_path = os.path.abspath(os.path.dirname(root_schema))
base_uri = 'file://{}/'.format(abs_path)

js = jsonref.loads(fins.read(), jsonschema=True, base_uri=base_uri)
findadd(js)


# print (type(js))
# print (type(js["properties"]["CityObjects"]["additionalProperties"]["oneOf"]))
# print(js)

# -- output stitched_schema
json_str = json.dumps(js, indent=2)
f = open('/Users/hugo/temp/out.json', "w")
f.write(json_str)