from pysnmp import hlapi


class Snmp_server:

    # On n'a pas besoin la fun de __init__ pour le moment.
    """
    def __init__(self, client_ip, list_of_oids):
        self.client_ip = client_ip
        self.list_of_oids = list_of_oids
    """


    def construct_object_types(self, list_of_oids):
        object_types = []
        for oid in list_of_oids:
            object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
        return object_types

    def construct_value_pairs(self, list_of_pairs):
        pairs = []
        for key, value in list_of_pairs.items():
            pairs.append(hlapi.ObjectType(hlapi.ObjectIdentity(key), value))
        return pairs

    def cast(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                try:
                    return str(value)
                except (ValueError, TypeError):
                    pass
        return value

    def fetch(self, handler, count):
        result = []
        for i in range(count):
            try:
                error_indication, error_status, error_index, var_binds = next(handler)
                if not error_indication and not error_status:
                    items = {}
                    for var_bind in var_binds:
                        items[str(var_bind[0])] = self.cast(var_bind[1])
                    result.append(items)
                else:
                    raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
            except StopIteration:
                break
        return result

    def get(self, target, oids, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
        handler = hlapi.nextCmd(
            engine,
            hlapi.CommunityData('public'),
            hlapi.UdpTransportTarget((target, port)),
            context,
            *self.construct_object_types(oids)
        )
        return self.fetch(handler, 1)[0]




#server = Snmp_server()
#print(server.get("192.168.56.210",["1.3.6.1.2.1.1.1.0","1.3.6.1.2.1.1.6.0"]))


