from typing import Any, Dict, List, Set, Tuple, Union


def dot_notation_search(
    object_to_search: Union[Dict, Set], dot_delimited_key: str
) -> Any:
    """Given an object to search (dict) and a dot_delimited_target_key, find a value inside of a
    nested dictionary.

    Args:
        dictionary_to_search (t.Dict): The dictionary to search (can be nested)
        dot_delimited_key (str): The target key to search.
        Nested object keys / indexes are delimited by a '.'

    Example:
            data = {"map": {"inner": [{"cow": 1}]}}
            # should output 1
            output = dot_notation_search(data, "map.inner.0.cow")

    Returns:
        The nested value located inside of a dictionary.
    """
    explored_depth = []
    supported_index_based_access_data_structures = (List, Tuple)
    for key in dot_delimited_key.split("."):
        explored_depth.append(key)
        if isinstance(object_to_search, (Dict, Set)):
            if key not in object_to_search:
                raise KeyError(
                    f"key: {key} not found. Search depth: {'.'.join(explored_depth)}"
                )
            object_to_search = object_to_search[key]
        # List, tuple
        elif isinstance(object_to_search, supported_index_based_access_data_structures):
            # this may raise ValueError if not convertible
            try:
                index = int(key)
                # this may raise IndexError if out of bounds
                # Such as -2 in a list of length 1
                object_to_search = object_to_search[index]
            except ValueError as e:
                raise ValueError(
                    f"currently at \"{'.'.join(explored_depth)}, "
                    f"examining object of type: {type(object_to_search)}. "
                    f"index: {key} is not an integer and "
                    f"cannot be used to access: {object_to_search}"
                ) from e
            except IndexError as e:
                raise IndexError(
                    f"index: {index} is out of bounds. "
                    f"Search depth: {'.'.join(explored_depth)}"
                ) from e

        else:
            raise TypeError(
                f"current object at \"{'.'.join(explored_depth)}\": "
                f"{object_to_search} is not a dictionary "
                f"or {supported_index_based_access_data_structures}"
            )
    # We should have rearched our target destination
    return object_to_search
