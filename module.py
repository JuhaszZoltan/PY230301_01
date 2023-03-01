def teglalap_kerulete(a_oldal:float, b_oldal:float) -> float:
    kerulet =  2 * (a_oldal + b_oldal)
    return kerulet


def teglalap_terulete(a_oldal:float, b_oldal:float) -> float:
    return a_oldal * b_oldal


def koszon(nev:str, napszak:str) -> None:
    print(f'Jó {napszak}t kívánok {nev}!')