#!/usr/bin/python3

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description with simple data structure.
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Dictionary to store the serializable attributes
    serializable_attributes = {}

    # Iterate over each attribute
    for key, value in attributes.items():
        # Check if the value is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value

    return serializable_attributes

if __name__ == "__main__":
    # Example usage
    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

