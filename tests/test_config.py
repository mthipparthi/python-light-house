from context import reference


def test_config():
    assert reference.config.config_1 == "config_val_1"
