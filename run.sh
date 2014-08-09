region=$1

echo "drop database neutron; create database neutron" | mysql -u root
mysql -u root neutron < ~/rackerlabs/db/prod_${region}_neutron_global/databases/MySQL/neutron.sql

git checkout master
quark-db-manage  --config-file ~/etc/neutron.conf upgrade head
python bin/print_all_subnets_ip_policies --config-file ~/etc/neutron.conf > master.$region

git checkout ip_policy_default_policy_two
quark-db-manage  --config-file ~/etc/neutron.conf upgrade head
python bin/print_all_subnets_ip_policies --config-file ~/etc/neutron.conf > RM7212.$region

diff master.$region RM7212.$region
