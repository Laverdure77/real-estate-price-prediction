
attributes = (
    "Locality", 
    "Type of property", 
    "Subtype of property", 
    "Price", 
    "Type of sale", 
    "Number of rooms", 
    "Living Area", 
    "Fully equipped kitchen",
    "Furnished",
    "Open fire",
    "Terrace",
    "Garden",
    "Surface of the land",
    "Surface area of the plot of land",
    "Number of facades",
    "Swimming pool",
    "State of the building"
)

immoweb_attributes = (
    "Locality",
    "Type of property",
    "Subtype of property",
    "Prix",
    "Type of sale",
    "Chambres",
    "Surface habitable",
    "Type de cuisine",
    "Meublé",
    "Combien de feux ouverts ?",
    "Surface de la terrasse",
    "Surface du jardin",
    "Surface du terrain",
    "Surface area of the plot of land",
    "Nombre de façades",
    "Piscine",
    "État du bâtiment"
)

def immoweb_filter(datas) :
    my_dict = dict()
    for attr, immo_attr in zip(attributes, immoweb_attributes) :
        if(immo_attr in datas.keys()) :
            if(attr in attributes[10:12]) :
                my_dict[attr] = True
                my_dict[attr + " area"] = int(datas[immo_attr].split(" ")[0])
            elif(attr in attributes[8] or attr in attributes[15]) :
                if(datas[immo_attr] == "Oui") :
                    my_dict[attr] = True
                else :
                    my_dict[attr] = False
            elif(attr in attributes[9]):
                if(int(datas[immo_attr]) > 0):
                    my_dict[attr] = True
                else :
                    my_dict[attr] = False
            elif(attr in attributes[3] or attr in attributes[5:7] or attr in attributes[12:15]) :
                my_dict[attr] = int(datas[immo_attr].replace(".","").split(" ")[0])
            elif(attr in attributes[7]) :
                if(datas[immo_attr].find("Pas équipée") > -1) :
                    my_dict[attr] = False
                else :
                    my_dict[attr] = True
            else : 
                my_dict[attr] = datas[immo_attr]
        else :
            if(attr in attributes[10:12]) :
                my_dict[attr] = False
                my_dict[attr + " area"] = None
            elif(attr in attributes[7:10] or attr in attributes[15]) :
                my_dict[attr] = False
            else :
                my_dict[attr] = None
    
    return my_dict


    test = {
    'Locality': 'Deinze', 
    'Type of property': 'maison', 
    'Subtype of property': None, 
    'Price': 353276, 
    'Type of sale': 'a-vendre', 
    'Number of rooms': 3,
    'Living Area': 159,
    'Fully equipped kitchen': False,
    'Furnished': False,
    'Open fire': False,
    'Terrace': True,
    'Terrace area': 12,
    'Garden': False,
    'Garden area': None,
    'Surface of the land': 159,
    'Surface area of the plot of land': 250,
    'Number of facades': 2,
    'Swimming pool': False,
    'State of the building': 'Excellent état'
    }