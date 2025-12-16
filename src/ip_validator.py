def is_valid_IPv4_octet(octet: str) -> bool:
    try:
        value = int(octet)
    except ValueError:
        return False
    return 0 <= value <= 255

def is_valid_IPv6_hextet(hextet: str) -> bool:
    if not hextet:
        return False
    try:
        value = int(hextet, 16)
    except ValueError:
        return False
    return 0 <= value <= 0xFFFF

def is_valid_IPv4(address: str) -> bool:
    octets = address.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not is_valid_IPv4_octet(octet):
            return False
    return True

def is_valid_IPv6(address: str) -> bool:
    hextets = address.split(":")
    if len(hextets) != 8:
        return False
    for hextet in hextets:
        if not is_valid_IPv6_hextet(hextet):
            return False
    return True

def get_ip_type(address: str) -> str:
    """
    Returns 'IPv4', 'IPv6' or 'Invalid'.
    """
    if is_valid_IPv4(address):
        return "IPv4"
    elif is_valid_IPv6(address):
        return "IPv6"
    else:
        return "Invalid"