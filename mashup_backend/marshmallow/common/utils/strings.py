def get_proxy_address_from_protocol_and_address_and_port(protocol: str, address: str, port: int) -> str:
    address = (protocol + "://" + address + ":" + str(port))
    print(address)
    return address
