

class OidLevel:

    # parametre d'initalisation de class
    def __init__(self, oid_level):
        self.oid_level = oid_level







"""
from low_level_OID import LowLevelOID
from high_level_OID import HighLevelOID

# TEST VALIDE

lo = LowLevelOID("1.3.6.1.4.1.14988.1.1.3.6", "1.3.6.1.2.1.25.2.3.1.5.65536")
ho = HighLevelOID("1.3.6.1.4.1.14988.1.1.3.66666", "1.3.6.1.2.1.25.2.3.1.5.65536", "1.3.6.1.2.1.31.1.1.1.6.1", "1.3.6.1.2.1.31.1.1.1.10.1")

level1 = OidLevel(lo)
level2 = OidLevel(ho)

print(level1.oid_level.cpu)
print(level2.oid_level.cpu)

"""
