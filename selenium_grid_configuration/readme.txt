In Mac terminal execute the following command lines
1. to start the hub:
java -jar selenium-server-standalone-3.141.59.jar -role hub -hubConfig gridHubConfig.json

2. to start the nodes:
java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig nodeConfig.json
