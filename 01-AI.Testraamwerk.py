#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

(c) 2025 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""
import sys
import inspect


naam = "Hadassah Murczak"
klas = "V1B"
studentnummer = 1909536

"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die deze
        lijst aanneemt bij álle tussenstappen bij toepassing van
        bovenstaand sorteeralgoritme.
"""
#       Antwoord 1a:
#       Ronde 1
#                            [4, 3, 1, 2]
#       4 > 3, dus wisselen: [3, 4, 1, 2]
#       4 > 1, dus wisselen: [3, 1, 4, 2]
#       4 > 2, dus wisselen: [3, 1, 2, 4]
#
#       Ronde 2
#       3 > 1, dus wisselen: [1, 3, 2, 4]
#       3 > 2, dus wisselen: [1, 2, 3, 4]
#       3 < 4, niks veranderen
#
#       Ronde 3
#       Vergelijk 1 en 2  -> goed.
#       Vergelijk 2 en 3  -> goed.
#       Vergelijk 3 en 4  -> goed.
#
#       Tussenstappen zonder uitleg:
#       [4, 3, 1, 2]
#       [3, 4, 1, 2]
#       [3, 1, 4, 2]
#       [3, 1, 2, 4]
#       [1, 3, 2, 4]
#       [1, 2, 3, 4]
"""

    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie
        hieronder genaamd my_sort(lst).
        Let op: je *moet* de pseudocode volgen!
"""

def my_sort(lst):

    # kopie maken
    lst_sorted = lst.copy()

    # Herhaling:
    swapped = True
    while swapped:
        swapped = False  # elke ronde staat deze op False

        for i in range(len(lst_sorted) - 1):
            # Vergelijkt elkaar
            if lst_sorted[i] > lst_sorted[i + 1]:
                # Is het linkse element groter? Dan moet deze gewisseld worden
                temp = lst_sorted[i]
                lst_sorted[i] = lst_sorted[i + 1]
                lst_sorted[i + 1] = temp
                swapped = True
                # Door True is er verwisseld in deze ronde.

    return lst_sorted

"""
    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke
            volgorde van de waarden in de lijst is het sorteeralgoritme
            het snelste klaar (best-case scenario)?
            Hoeveel vergelijkingen (zoals beschreven in stap 1. van de
            pseudocode) zijn nodig geweest?
"""
#           Best case scenario is dat de lijst al staat op volgorde, dus: [1, 2, 3]
#           Het algoritme vergelijkt dit dan voor 1 ronde, dus:
#           1 en 2 vergelijken en 2 en 3 vergelijken
#           Deze staan op de juiste plek dus er hoeft niks verwisseld te worden.
#           En dan zijn er maar 2 vergelijkingen geweest.

"""

        -   Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het minst snel klaar (worst-case scenario)?
            Hoeveel vergelijkingen zijn nodig geweest?
"""
#           Worst-case is wanneer de lijst omgekeerd staat en 'aftelt', dus: [3, 2, 1]
#           Dit worden dan drie ronden en elk heeft twee vergelijkingen,
#           dus dan 6 vergelijkingen. (3*2=6)

"""

        -   Stel je hebt een lijst met de waarden 1 tot en met 4.
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
#           Best-case is hetzelfde als de vorige vraag. Dat de lijst al op volgoorste is [1, 2, 3, 4]
#           Dit zijn drie vergelijkingen en maar 1 ronde.
#
#           Worst-case is hier ook weer dat de lijst omgekeerd staat [4, 3, 2, 1]
#           Dit zijn in totaal vier rondes, waarvan elke ronde drie vergelijkingen
#           3*4=12 vergelijkingen


"""

        -   (Optioneel) Stel je hebt een lijst met de waarden 1 tot en met n
            (je weet nu dus niet precies hoeveel waarden er in de lijst
            zitten, het zijn er 'n').
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
#           TODO: [geef hier je antwoord]
"""
"""

def linear_search_recursive(lst, target):
    """
    Recursieve lineaire zoekfunctie.
    Van links naar rechts wordt er gezocht of het element in de lijst staat.

    Recursie: de functie roept zichzelf opnieuw aan met een kleine lijst.
    """

    # Lijst is leeg? Dan kan er niks gevonden worden en is er ook element.
    if len(lst) == 0:
        return False

    # Dit kijkt naar eerste element. Element = gezocht element --> True     Gezocht element = target
    if lst[0] == target:
        return True

    # Als eerste element niet het gezochte element is dan wordt er verder gezocht
    return linear_search_recursive(lst[1:], target)
    #lst[1:] er wordt een andere lijst gemaakt zonder het eerste element (target). --> kortere lijst.

"""
(Optioneel)
3.  Sorteeralgoritme 2

    Hieronder staat de pseudocode van nog een sorteeralgoritme voor een lijst `lst` van natuurlijke getallen:
    1. Bepaal het grootste getal k in de lijst.
    2. Maak een nieuwe lijst van lengte k+1, waarbij elk element in deze tweede lijst begint met de waarde 0.
    3. Tel het aantal voorkomens van elk getal in de originele lijst en sla deze frequentie op in de tweede lijst.
    4. Maak een derde, lege lijst
    5. Voeg elke index van de tweede lijst zo vaak toe aan de derde lijst als zij geteld is in stap 3.
    6. Retourneer de derde lijst: zij is een gesorteerde versie van de originele lijst.

    Implementeer het sorteeralgoritme in Python in een functie
    hieronder genaamd my_sort_2(lst).
    Let op: je *moet* de pseudocode volgen!
"""

def my_sort_2(lst):
    """
    Sorteer gegeven lijst volgens het algoritme zoals beschreven in de pseudocode hierboven.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    sorted_lst = []

    return sorted_lst


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_my_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"

def test_linear_search_recursive():
    for _ in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = linear_search_recursive(lst_test, target)
        assert lst_copy == lst_test, "Fout: linear_search_recursive(lst, target) verandert de inhoud van lijst lst"
        assert outcome == found, \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"

def test_test_linear_search_recursive_recursiveness():
    limit = sys.getrecursionlimit()
    sys.setrecursionlimit(50)
    try:
        linear_search_recursive(list(range(100)), 100)
        assert False, "Fout: linear_search_recursive werkt niet recursief"
    except RecursionError:
        return
    finally:
        sys.setrecursionlimit(limit)

def test_my_sort_2():
    lst_test = [random.choice(range(10)) for _ in range(10)]
    lst_copy = lst_test.copy()
    lst_output = my_sort_2(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort_2(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort_2({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        test_test_linear_search_recursive_recursiveness()
        print("Je functie linear_search_recursive() werkt goed!")

        test_my_sort_2()
        print("(Optioneel) Je functie test_my_sort_2() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("\x1b[38;5;208m")
        print("Echter, test dit testframework niet of je de pseudocode goed gevolgd hebt.")
        print("Ook test dit testframework niet of de juiste antwoorden  bij 1a en 1c hebt gegeven.\x1b[0m")
        print("Controleer die dus nog, en lever dan pas je werk in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
