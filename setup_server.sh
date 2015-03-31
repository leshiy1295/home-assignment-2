#!/usr/bin/env bash

java -jar selenium-server-standalone-2.45.0.jar \
     -role node \
     -hub http://127.0.0.1:4444/grid/register \
     -Dwebdriver.chrome.driver="./chromedriver" \
     -browser browserName=chrome,maxInstances=1 \
     -browser browserName=firefox,maxInstances=1
