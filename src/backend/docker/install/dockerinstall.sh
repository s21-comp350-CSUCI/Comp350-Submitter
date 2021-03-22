#!/bin/bash
# When used in production, whatever thread pulls
# and runs this script should shange its owner to root
# and make a setuid program 
# so we can dump these sudo commands and go straight g
# sudo chown root dockerinstall.sh
# chmod 4755 dockerinstall.sh
# this allows the script to be run with root (owner) privelege
# execute script as $ ./dockerinstall.sh


sudo yum update -y
# installing
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker
# Most likely will need to be restarted but maybe not
#sudo shutdown -r now
