#########
# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.

from flask_securest.authorization_providers.role_loaders.abstract_role_loader\
    import AbstractRoleLoader

class PredefinedRoleLoader(AbstractRoleLoader):

    def __init__(self, role_name):
        self.role_name = role_name

    def get_roles(self):
        return self.role_name
