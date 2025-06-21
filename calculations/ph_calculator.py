import math

def calculate_ph_from_h(h_conc):
    return -math.log10(h_conc)

def calculate_h_from_ph(ph):
    return 10 ** (-ph)

def calculate_poh_from_oh(oh_conc):
    return -math.log10(oh_conc)

def calculate_oh_from_poh(poh):
    return 10 ** (-poh)