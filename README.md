# qingcloud-util
code collection which is used to operate qingcloud resource automaticlly

### del-nic
This feature mostly could be used to clean the unused nic in k8s cluster.  
User should put his api keys and related zone info into client.yaml, also run `kubectl get pods -o json --all-namespaces` and save output to pods.json(todo: this step could be automated in code).  
This tool will check the nics which are created by hostnic component and only detach/delete the ones which are not consumed by running k8s pods.  
NOTE: currently this tool only call qingcloud iaas command directly and doesn't do return code check, so sometimes the delete job is started but detach job is not done, you may see that some nic is detached successfuflly but failed to delete, running this tool later should solve this issue.