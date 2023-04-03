# Copyright 2022 IBM, Red Hat
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM  quay.io/opendatahub/notebooks:jupyter-minimal-ubi8-python-3.8-4c8f26e

# Install: torch (v1.12), ray (v2.1.0) and others

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip uninstall pickle5 -y 

# Install codeflare-sdk and other libraries
RUN pip install codeflare-sdk==0.4.0 \
				datasets==2.6.1 \
				transformers==4.23.1 \
				evaluate==0.3.0