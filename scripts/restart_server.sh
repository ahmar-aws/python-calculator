#!/bin/bash
cd /home/ec2-user/myapp
sudo fuser -k 80/tcp || true
sudo nohup python3 app.py > app.log 2>&1 &
