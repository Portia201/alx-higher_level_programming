def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Args:
    - obj: The object to which the attribute should be added.
    - attr: The name of the attribute to add.
    - value: The value of the attribute.

Raises:
    - TypeError: If the object does not support adding new attributes.
    """
    if not hasattr(obj, '__dict__') and not hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
