import googleapiclient.discovery
import json
import pandas as pd

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']


def main(project, zone):
    compute = googleapiclient.discovery.build('compute', 'v1')

    instances = list_instances(compute, project, zone)
    table = []

    for instance in instances:
        #print [m['value'] for m in instance['metadata']['items'] if m['key'] == 'dataproc-bucket']

        key_value = filter(lambda x: x['key'] == 'dataproc-bucket', instance['metadata']['items'])


        table.append({'hostname': instance['name'], 'metadata': key_value[0]['value']})

    json_payload = json.dumps(table, ensure_ascii=False, encoding="utf-8")
    results = pd.read_json(json_payload)
    print results


#my_list = [x for x in my_list if x.attribute == value]


#my_list = filter(lambda x: x.attribute == value, my_list)