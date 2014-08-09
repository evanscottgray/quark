region=$1

echo "drop database neutron; create database neutron" | mysql -u root
mysql -u root neutron < ~/rackerlabs/db/prod_${region}_neutron_global/databases/MySQL/neutron.sql

git checkout master
quark-db-manage  --config-file ~/etc/neutron.conf upgrade head
time python bin/ip_availability_fixed_master --config-file ~/etc/neutron.conf > master.$region

git checkout ip_policy_size
quark-db-manage  --config-file ~/etc/neutron.conf upgrade head
time python bin/ip_availability_fixed --config-file ~/etc/neutron.conf > RM7212.$region

diff master.$region RM7212.$region
