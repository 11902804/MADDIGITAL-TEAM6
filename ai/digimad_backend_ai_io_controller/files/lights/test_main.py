from fastapi.testclient import TestClient
from main import app
from phue import Bridge


client = TestClient(app)
bridge = Bridge('192.168.0.41')
bridge.connect()
bridge.get_api()

status_code_200_error = \
    'Should receive a 200 response code, but got {} as response'
expected_json_error = 'Should receive {} as response'


def test_read_main():
    response = client.get("/")

    expected = bridge.get_api()

    assert response.status_code == 200, \
        status_code_200_error.format(response.status_code)

    assert expected == response.json()


def test_lights():
    response = client.get("/getAllLights")

    statuslights = []
    lights = bridge.get_light_objects('id')
    for light in lights:
        statuslights.append([light, bridge.get_light(light, 'on')])

    assert response.status_code == 200, \
        status_code_200_error.format(response.status_code)

    assert response.json() == statuslights, \
        expected_json_error.format(statuslights)

# Testing on the state function within the app


def test_state_on():
    message_on = {"id": "1", "on": True, "bri": 0, "hue": 0, "sat": 0}
    message_off = {"id": "1", "on": False, "bri": 0, "hue": 0, "sat": 0}

    expected_on = bridge.set_light(1, 'on', True)
    expected_off = bridge.set_light(1, 'on', False)

    response_on = client.put(
        "/changeState/",
        json=message_on,
    )

    response_off = client.put(
        "/changeState/",
        json=message_off,
    )

    assert response_on.status_code == 200, \
        status_code_200_error.format(response_on.status_code)

    assert response_on.json() == expected_on, \
        expected_json_error.format(expected_on)

    assert response_off.status_code == 200, \
        status_code_200_error.format(response_off.status_code)

    assert response_off.json() == expected_off, \
        expected_json_error.format(expected_off)


def test_color():
    color_change = {"id": "1", "on": True, "bri": 0, "hue": 255, "sat": 0}

    expected = bridge.set_light(1, 'hue', 255)

    response = client.put(
        "/changeColor/",
        json=color_change,
    )

    assert response.status_code == 200, \
        status_code_200_error.format(response.status_code)

    assert response.json() == expected, \
        expected_json_error.format(expected)


def test_brightness():
    brightness_change = {"id": "1", "on": True, "bri": 255, "hue": 0, "sat": 0}

    expected = bridge.set_light(1, 'bri', 255)

    response = client.put(
        "/changeBrightness/",
        json=brightness_change,
    )

    assert response.status_code == 200, \
        status_code_200_error.format(response.status_code)

    assert response.json() == expected, \
        expected_json_error.format(expected)


def test_saturation():
    saturation_change = {"id": "1", "on": True, "bri": 0, "hue": 0, "sat": 255}

    expected = bridge.set_light(1, 'sat', 255)

    response = client.put(
        "/changeSaturation/",
        json=saturation_change,
    )

    assert response.status_code == 200, \
        status_code_200_error.format(response.status_code)

    assert response.json() == expected, \
        expected_json_error.format(expected)
