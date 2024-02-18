import logging
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
import threading
from . import rcswitch

DOMAIN = "test_component"

_LOGGER = logging.getLogger(__name__)

DOMAIN = "open433"

CONF_COMPORT = "port"
CONF_COMSPEED = "speed"

REQ_LOCK = threading.Lock()
CONFIG_SCHEMA = vol.Schema(
	{
		DOMAIN: vol.Schema({
			vol.Required(CONF_COMPORT): cv.string,
			vol.Optional(CONF_COMSPEED, default=9600): cv.positive_int,
		})
	},
	extra=vol.ALLOW_EXTRA,
)

def setup(hass, config):
    hass.states.set("test_component.world", "Paulus")
	
    # Return boolean to indicate that initialization was successful.
    return True
