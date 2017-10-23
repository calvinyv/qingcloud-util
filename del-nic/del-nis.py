import json
import subprocess

k8s_ips = []
k8s_nodes = []
with open('pods.json') as json_file:
    data = json.load(json_file)
    for pods in data['items']:
      #print(pods['status']['hostIP'])
      k8s_ips.append(pods['status']['hostIP'])
      #print(pods['status']['podIP'])
      k8s_ips.append(pods['status']['podIP'])
      k8s_nodes.append(pods['spec']['nodeName'])
k8s_ips = set(k8s_ips)
for ip in k8s_ips:
    print("k8s is using: " + ip)
for node in set(k8s_nodes):
    nic_json = json.loads(subprocess.check_output("qingcloud iaas describe-nics -f client.yaml -N hostnic_" + node + "|jq ''", shell=True))
    for nic in nic_json['nic_set']:
        if nic['private_ip'] not in k8s_ips:
            print("detaching " + nic['nic_id'] + "----" + nic['private_ip'] + " on node " + nic['instance_id'])
            subprocess.call("qingcloud iaas detach-nics -f client.yaml -n " + nic['nic_id'], shell=True)
            print("deleting " + nic['nic_id'] + "----" + nic['private_ip'] + " on node " + nic['instance_id'])
            subprocess.call("qingcloud iaas delete-nics -f client.yaml -n " + nic['nic_id'], shell=True)





