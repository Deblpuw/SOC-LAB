import subprocess

print('Lancement du lab SOC...')
subprocess.run(['docker','compose','-f','docker/splunk/docker-compose.yml','up','-d'])
subprocess.run(['docker','compose','-f','docker/elk/docker-compose.yml','up','-d'])
print('Lab SOC démarré ! Splunk: http://localhost:8000 Kibana: http://localhost:5601')
