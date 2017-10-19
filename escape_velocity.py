""""Efrén Santiago Landeros Hernández"""
"""Calcula la velocidad de escape"""
def escape_velocity(G: float, M: float, r: float )->float:
    return ((2 * (G * M) )/ r) ** (1/2)
