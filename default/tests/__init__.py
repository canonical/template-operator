# Copyright {{ year }} {{ author }}
# See LICENSE file for licensing details.

import ops.testing

# Enable more accurate simulation of container networking.
# For more information, see https://juju.is/docs/sdk/testing#heading--simulate-can-connect.
ops.testing.SIMULATE_CAN_CONNECT = True
