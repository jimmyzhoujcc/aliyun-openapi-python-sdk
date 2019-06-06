# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SetLoadBalancerHTTPSListenerAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2014-05-15', 'SetLoadBalancerHTTPSListenerAttribute','slb')

	def get_access_key_id(self):
		return self.get_query_params().get('access_key_id')

	def set_access_key_id(self,access_key_id):
		self.add_query_param('access_key_id',access_key_id)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_HealthCheckTimeout(self):
		return self.get_query_params().get('HealthCheckTimeout')

	def set_HealthCheckTimeout(self,HealthCheckTimeout):
		self.add_query_param('HealthCheckTimeout',HealthCheckTimeout)

	def get_XForwardedFor(self):
		return self.get_query_params().get('XForwardedFor')

	def set_XForwardedFor(self,XForwardedFor):
		self.add_query_param('XForwardedFor',XForwardedFor)

	def get_HealthCheckURI(self):
		return self.get_query_params().get('HealthCheckURI')

	def set_HealthCheckURI(self,HealthCheckURI):
		self.add_query_param('HealthCheckURI',HealthCheckURI)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_UnhealthyThreshold(self):
		return self.get_query_params().get('UnhealthyThreshold')

	def set_UnhealthyThreshold(self,UnhealthyThreshold):
		self.add_query_param('UnhealthyThreshold',UnhealthyThreshold)

	def get_HealthyThreshold(self):
		return self.get_query_params().get('HealthyThreshold')

	def set_HealthyThreshold(self,HealthyThreshold):
		self.add_query_param('HealthyThreshold',HealthyThreshold)

	def get_AclStatus(self):
		return self.get_query_params().get('AclStatus')

	def set_AclStatus(self,AclStatus):
		self.add_query_param('AclStatus',AclStatus)

	def get_Scheduler(self):
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self,Scheduler):
		self.add_query_param('Scheduler',Scheduler)

	def get_AclType(self):
		return self.get_query_params().get('AclType')

	def set_AclType(self,AclType):
		self.add_query_param('AclType',AclType)

	def get_HealthCheck(self):
		return self.get_query_params().get('HealthCheck')

	def set_HealthCheck(self,HealthCheck):
		self.add_query_param('HealthCheck',HealthCheck)

	def get_MaxConnection(self):
		return self.get_query_params().get('MaxConnection')

	def set_MaxConnection(self,MaxConnection):
		self.add_query_param('MaxConnection',MaxConnection)

	def get_EnableHttp2(self):
		return self.get_query_params().get('EnableHttp2')

	def set_EnableHttp2(self,EnableHttp2):
		self.add_query_param('EnableHttp2',EnableHttp2)

	def get_CookieTimeout(self):
		return self.get_query_params().get('CookieTimeout')

	def set_CookieTimeout(self,CookieTimeout):
		self.add_query_param('CookieTimeout',CookieTimeout)

	def get_StickySessionType(self):
		return self.get_query_params().get('StickySessionType')

	def set_StickySessionType(self,StickySessionType):
		self.add_query_param('StickySessionType',StickySessionType)

	def get_VpcIds(self):
		return self.get_query_params().get('VpcIds')

	def set_VpcIds(self,VpcIds):
		self.add_query_param('VpcIds',VpcIds)

	def get_VServerGroupId(self):
		return self.get_query_params().get('VServerGroupId')

	def set_VServerGroupId(self,VServerGroupId):
		self.add_query_param('VServerGroupId',VServerGroupId)

	def get_AclId(self):
		return self.get_query_params().get('AclId')

	def set_AclId(self,AclId):
		self.add_query_param('AclId',AclId)

	def get_ListenerPort(self):
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self,ListenerPort):
		self.add_query_param('ListenerPort',ListenerPort)

	def get_Cookie(self):
		return self.get_query_params().get('Cookie')

	def set_Cookie(self,Cookie):
		self.add_query_param('Cookie',Cookie)

	def get_HealthCheckType(self):
		return self.get_query_params().get('HealthCheckType')

	def set_HealthCheckType(self,HealthCheckType):
		self.add_query_param('HealthCheckType',HealthCheckType)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_StickySession(self):
		return self.get_query_params().get('StickySession')

	def set_StickySession(self,StickySession):
		self.add_query_param('StickySession',StickySession)

	def get_HealthCheckMethod(self):
		return self.get_query_params().get('HealthCheckMethod')

	def set_HealthCheckMethod(self,HealthCheckMethod):
		self.add_query_param('HealthCheckMethod',HealthCheckMethod)

	def get_HealthCheckDomain(self):
		return self.get_query_params().get('HealthCheckDomain')

	def set_HealthCheckDomain(self,HealthCheckDomain):
		self.add_query_param('HealthCheckDomain',HealthCheckDomain)

	def get_RequestTimeout(self):
		return self.get_query_params().get('RequestTimeout')

	def set_RequestTimeout(self,RequestTimeout):
		self.add_query_param('RequestTimeout',RequestTimeout)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Gzip(self):
		return self.get_query_params().get('Gzip')

	def set_Gzip(self,Gzip):
		self.add_query_param('Gzip',Gzip)

	def get_TLSCipherPolicy(self):
		return self.get_query_params().get('TLSCipherPolicy')

	def set_TLSCipherPolicy(self,TLSCipherPolicy):
		self.add_query_param('TLSCipherPolicy',TLSCipherPolicy)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ServerCertificateId(self):
		return self.get_query_params().get('ServerCertificateId')

	def set_ServerCertificateId(self,ServerCertificateId):
		self.add_query_param('ServerCertificateId',ServerCertificateId)

	def get_CACertificateId(self):
		return self.get_query_params().get('CACertificateId')

	def set_CACertificateId(self,CACertificateId):
		self.add_query_param('CACertificateId',CACertificateId)

	def get_BackendProtocol(self):
		return self.get_query_params().get('BackendProtocol')

	def set_BackendProtocol(self,BackendProtocol):
		self.add_query_param('BackendProtocol',BackendProtocol)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_IdleTimeout(self):
		return self.get_query_params().get('IdleTimeout')

	def set_IdleTimeout(self,IdleTimeout):
		self.add_query_param('IdleTimeout',IdleTimeout)

	def get_LoadBalancerId(self):
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self,LoadBalancerId):
		self.add_query_param('LoadBalancerId',LoadBalancerId)

	def get_XForwardedFor_SLBIP(self):
		return self.get_query_params().get('XForwardedFor_SLBIP')

	def set_XForwardedFor_SLBIP(self,XForwardedFor_SLBIP):
		self.add_query_param('XForwardedFor_SLBIP',XForwardedFor_SLBIP)

	def get_HealthCheckInterval(self):
		return self.get_query_params().get('HealthCheckInterval')

	def set_HealthCheckInterval(self,HealthCheckInterval):
		self.add_query_param('HealthCheckInterval',HealthCheckInterval)

	def get_XForwardedFor_proto(self):
		return self.get_query_params().get('XForwardedFor_proto')

	def set_XForwardedFor_proto(self,XForwardedFor_proto):
		self.add_query_param('XForwardedFor_proto',XForwardedFor_proto)

	def get_XForwardedFor_SLBID(self):
		return self.get_query_params().get('XForwardedFor_SLBID')

	def set_XForwardedFor_SLBID(self,XForwardedFor_SLBID):
		self.add_query_param('XForwardedFor_SLBID',XForwardedFor_SLBID)

	def get_HealthCheckConnectPort(self):
		return self.get_query_params().get('HealthCheckConnectPort')

	def set_HealthCheckConnectPort(self,HealthCheckConnectPort):
		self.add_query_param('HealthCheckConnectPort',HealthCheckConnectPort)

	def get_HealthCheckHttpCode(self):
		return self.get_query_params().get('HealthCheckHttpCode')

	def set_HealthCheckHttpCode(self,HealthCheckHttpCode):
		self.add_query_param('HealthCheckHttpCode',HealthCheckHttpCode)

	def get_VServerGroup(self):
		return self.get_query_params().get('VServerGroup')

	def set_VServerGroup(self,VServerGroup):
		self.add_query_param('VServerGroup',VServerGroup)