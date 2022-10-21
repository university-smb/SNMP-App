

class Config:
    

    def __init__(self, equipements):
        self.equipements = equipements




    # Fonction pour ajouter nouveau equipement
    def add_device(self, constructeur, type_de_material, IP, DNS, description):

        # check if equipement is empty
        if len(self.equipements == 0):
            self.equipements =  {"equipement": []}

        new_device = {
            "constructeur": constructeur,
            "type_de_material": type_de_material,
            "IP": IP,
            "DNS": DNS,
            "description": description
        }

        self.equipements['equipement'].append(new_device)



    # verifier si l'equipement existe déjà
    def device_existe(self, ip):

        # 
        for equipement in self.equipements['equipement']:
            if ip == equipement['IP']:
                return True
        return False




