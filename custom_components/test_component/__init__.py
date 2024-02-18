DOMAIN = "test_component"


def setup(hass, config):
    hass.states.set("test_component.world", "Paulus")

    # Return boolean to indicate that initialization was successful.
    return True
