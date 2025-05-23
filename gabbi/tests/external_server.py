#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys
from wsgiref import simple_server

from gabbi.tests import simple_wsgi


def run(host, port):
    server = simple_server.make_server(
        host,
        int(port),
        simple_wsgi.SimpleWsgi(),
    )
    server.serve_forever()


if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]
    run(host, port)
