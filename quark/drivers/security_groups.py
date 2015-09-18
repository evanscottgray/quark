# Copyright 2014 Openstack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#

from oslo_log import log as logging

from quark.cache import security_groups_client as sg_client
from quark import environment as env

LOG = logging.getLogger(__name__)


class SecurityGroupDriver(object):
    @env.has_capability(env.Capabilities.SECURITY_GROUPS)
    def update_port(self, **kwargs):
        client = sg_client.SecurityGroupsClient()
        if "security_groups" in kwargs:
            if kwargs["security_groups"]:
                payload = client.serialize_groups(
                    kwargs["security_groups"])
                client.apply_rules(kwargs["device_id"],
                                   kwargs["mac_address"],
                                   payload)
            else:
                client.delete_vif_rules(kwargs["device_id"],
                                        kwargs["mac_address"])

    @env.has_capability(env.Capabilities.SECURITY_GROUPS)
    def delete_port(self, **kwargs):
        client = sg_client.SecurityGroupsClient()
        try:
            client.delete_vif(kwargs["device_id"],
                              kwargs["mac_address"])
        except Exception:
            LOG.exception("Failed to reach the security groups backend")