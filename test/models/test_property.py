from models.property import Property


def test_must_create_property():
    property = Property.create_property()
    assert property.sale_value is not None
    assert property.rent_value is not None
    assert property.player is None


def test_must_create_game_board_properties():
    properties = Property.create_game_board_properties()
    assert len(properties) == 20
    for property in properties:
        assert property.sale_value is not None
        assert property.rent_value is not None
        assert property.player is None
