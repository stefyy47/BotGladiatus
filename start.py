import requests
import time
import webbrowser
import sys
import _thread
import threading
from bs4 import BeautifulSoup
millis = int(round(time.time() * 1000))

def buy_right_items_auction2(pret_maxim, item, itemType, itemLVL, quality):
    try:
        res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&ttype=3&sh={secureHash}',
                     data={'doll': 1, 'qry': item, 'itemLevel': itemLVL, 'itemType': itemType, 'itemQuality': quality})
        i = res.text.find('mic pret')
        while i != -1:
            i2 = res.text.find('Lul', i - 150, i)
            while res.text[i] != ':':
                i += 1
            i += 2
            pret = ""
            try:
                while True:
                    pret += res.text[i]
                    i += 1
                    try:
                        int(res.text[i])
                    except:
                        if res.text[i] == '.':
                            i += 1
                        else:
                            break
            except:
                pass
            while res.text[i] != 'n' or res.text[i + 1] != 'F' or res.text[i + 2] != 'o' or res.text[
                i + 3] != 'r' or res.text[i + 4] != 'm':
                i += 1
            i += 5
            id_item = ""
            while res.text[i] != "'":
                id_item += res.text[i]
                i += 1
            pret_int = int(pret)
            print(pret, id_item, i2)
            if pret_maxim >= pret_int and i2 == - 1:
                print("Am pus bid pentru itemul(Gladiator auction)", item)
                s.post(
                    f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&submod=placeBid&ttype=3&rubyAmount=3&sh={secureHash}',
                    data={'auctionid': id_item, 'qry': "", 'itemType': itemType, 'itemLevel': itemLVL, 'itemQuality': quality,
                          'buyouthd': 0, 'bid_amount': pret, 'bid': 'Ofera'})
            i = res.text.find('mic pret', i)
        return 0
    except:
        return 0
        pass
def buy_right_items_auction1(pret_maxim, item, itemType, itemLVL, quality):
    try:
        res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}',
                     data={'doll': 1, 'qry': item, 'itemLevel': itemLVL, 'itemType': itemType, 'itemQuality': quality})
        i = res.text.find('mic pret')
        while i != -1:
            i2 = res.text.find('Lul', i - 150, i)
            while res.text[i] != ':':
                i += 1
            i += 2
            pret = ""
            try:
                while True:
                    pret += res.text[i]
                    i += 1
                    try:
                        int(res.text[i])
                    except:
                        if res.text[i] == '.':
                            i += 1
                        else:
                            break
            except:
                pass
            while res.text[i] != 'n' or res.text[i + 1] != 'F' or res.text[i + 2] != 'o' or res.text[
                i + 3] != 'r' or res.text[i + 4] != 'm':
                i += 1
            i += 5
            id_item = ""
            while res.text[i] != "'":
                id_item += res.text[i]
                i += 1
            pret_int = int(pret)
            print(pret, id_item, i2)
            if pret_maxim >= pret_int and i2 == - 1:
                print("Am pus bid pentru itemul(Gladiator auction)", item)
                s.post(
                    f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&submod=placeBid&ttype=2&rubyAmount=3&sh={secureHash}',
                    data={'auctionid': id_item, 'qry': "", 'itemType': itemType, 'itemLevel': itemLVL, 'itemQuality': quality,
                          'buyouthd': 0, 'bid_amount': pret, 'bid': 'Ofera'})
            i = res.text.find('mic pret', i)
        return 0
    except:
        return 0
        pass
def check_auction1_for_item(pret_maxim, types, itemLVL, quality, *items):
    try:
        print("Sunt in check_auction1")
        for item in items:
            res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}', data = {'doll' : 1, 'qry' : item, 'itemLevel' : 22, 'itemType': 0, 'itemQuality' : -1})
            i = res.text.find("Nici un rezultat")
            if i == -1:
                res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}')
                timp_ramas = res.text.find('description_span_right')
                while res.text[timp_ramas] != '<' or res.text[timp_ramas + 1] != 'b' or res.text[timp_ramas + 2] != '>':
                    timp_ramas += 1
                timp_ramas += 3
                while res.text[timp_ramas] == 'f' and res.text[timp_ramas + 7] == 's':
                    for x in types:
                        buy_right_items_auction1(pret_maxim, item, x, itemLVL, quality)
                    res = s.get(
                        f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}')
                    timp_ramas = res.text.find('description_span_right')
                    while res.text[timp_ramas] != '<' or res.text[timp_ramas + 1] != 'b' or res.text[
                        timp_ramas + 2] != '>':
                        timp_ramas += 1
                    timp_ramas += 3
        return 0
    except:
        return 0
        pass
def check_auction2_for_item(pret_maxim, types, itemLVL, quality, *items):
    try:
        print("Sunt in check auction2")
        for item in items:
            res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&ttype=3&sh={secureHash}', data = {'doll' : 1, 'qry' : item, 'itemLevel' : 22, 'itemType': 0, 'itemQuality' : -1})
            i = res.text.find("Nici un rezultat")
            if i == -1:
                res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&ttype=3&sh={secureHash}')
                timp_ramas = res.text.find('description_span_right')
                while res.text[timp_ramas] != '<' or res.text[timp_ramas + 1] != 'b' or res.text[timp_ramas + 2] != '>':
                    timp_ramas += 1
                timp_ramas += 3
                while res.text[timp_ramas] == 'f' and res.text[timp_ramas + 7] == 's':
                    for x in types:
                        buy_right_items_auction2(pret_maxim, item, x, itemLVL, quality)
                    res = s.get(
                        f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&ttype=3&sh={secureHash}')
                    timp_ramas = res.text.find('description_span_right')
                    while res.text[timp_ramas] != '<' or res.text[timp_ramas + 1] != 'b' or res.text[
                        timp_ramas + 2] != '>':
                        timp_ramas += 1
                    timp_ramas += 3
        return 0
    except:
        return 0
        pass
def check_auction():
    try:
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}')
        timp_ramas = res.text.find('description_span_right')
        while res.text[timp_ramas] != '<' or res.text[timp_ramas + 1] != 'b' or res.text[timp_ramas + 2] != '>':
            timp_ramas += 1
        timp_ramas += 3
        if res.text[timp_ramas] == 'f':
            webbrowser.open("G:/probleme/python/bottravian/venv/alarm_rooster.mp3")
    except:
        pass
def check_mercenary_auction():
    try:
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&ttype=3&sh={secureHash}')
        timp_ramas = res.text.find('description_span_right')
        while res.text[timp_ramas] != '<' or res.text[timp_ramas + 1] != 'b' or res.text[timp_ramas + 2] != '>':
            timp_ramas += 1
        timp_ramas += 3
        if res.text[timp_ramas] == 'f':
            webbrowser.open("G:/probleme/python/bottravian/venv/alarm_rooster.mp3")
    except:
        pass
def place_food_in_inventory():
    try:
        print("Sunt in place_food_in_inv")
        for i in range(1,6):
            for j in range (1,9):
                millis = int(round(time.time() * 1000))
                res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&f=7&fq=-1&qry=&page=1&sh={secureHash}')
                soup = BeautifulSoup(res.text, 'html5lib')
                supa = soup.find('input', attrs={'name' : 'packages[]'})['value']
                s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=-{supa}&fromX=1&fromY=1&to=512&toX={i}&toY={j}&amount=1', data = {'a' : millis, 'sh' : secureHash})
    except:
        pass
def buy_mercenaries(pret_maxim, name, quality, level):
    try:
        print("Sunt in buy_mercenaries")
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}')
        timp_ramas = res.text.find('description_span_right')
        while res.text[timp_ramas] != '<' or res.text[timp_ramas + 1] != 'b' or res.text[timp_ramas + 2] != '>':
            timp_ramas += 1
        timp_ramas += 3
        if res.text[timp_ramas] == 'f' and res.text[timp_ramas + 7] == 's':
            res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}', data = {'doll' : 1, 'qry' : name, 'itemLevel' : level, 'itemType' : 15, 'itemQuality' : quality})
            i = 0
            while i != -1:
                if name == 'samnit' or name == 'murmil':
                    i = res.text.find('Dexteritate', i)
                    if i == -1:
                        return 0
                    i += 13
                    dexteritatea = ''
                    dexteritatea += res.text[i]
                    dexteritatea += res.text[i + 1]
                    dexteritatea += res.text[i + 2]
                    if int(dexteritatea) >= 380:
                        i = res.text.find('mic pret', i)
                        i2 = res.text.find('Lul', i - 150, i)
                        while res.text[i] != ':':
                            i += 1
                        i += 2
                        pret = ""
                        try:
                            while True:
                                pret += res.text[i]
                                i += 1
                                try:
                                    int(res.text[i])
                                except:
                                    if res.text[i] == '.':
                                        i += 1
                                    else:
                                        break
                        except:
                            pass
                        while res.text[i] != 'n' or res.text[i + 1] != 'F' or res.text[i + 2] != 'o' or res.text[i + 3] != 'r' or res.text[i + 4] != 'm':
                            i += 1
                        i += 5
                        id_item = ""
                        while res.text[i] != "'":
                            id_item += res.text[i]
                            i += 1
                        pret_int = int(pret)
                        if pret_maxim >= pret_int and i2 == - 1:
                            print("Am pus bid pe mercenar")
                            s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&submod=placeBid&ttype=2&rubyAmount=3&sh={secureHash}', data = {'auctionid' : {id_item}, 'qry' : name, 'itemType' : 15, 'itemLevel' : level, 'itemQuality' : -1, 'buyouthd' : 0, 'bid_amount': {pret}, 'bid': 'Ofera'})

                elif name == "elita" or name == "maestru":
                    i = res.text.find('Agilitate', i)
                    if i == -1:
                        return 0
                    i += 11
                    agilitatea = ''
                    agilitatea += res.text[i]
                    agilitatea += res.text[i + 1]
                    agilitatea += res.text[i + 2]
                    if int(agilitatea) >= 390:
                        i = res.text.find('mic pret', i)
                        i2 = res.text.find('Lul', i - 150, i)
                        while res.text[i] != ':':
                            i += 1
                        i += 2
                        pret = ""
                        try:
                            while True:
                                pret += res.text[i]
                                i += 1
                                try:
                                    int(res.text[i])
                                except:
                                    if res.text[i] == '.':
                                        i += 1
                                    else:
                                        break
                        except:
                            pass
                        while res.text[i] != 'n' or res.text[i + 1] != 'F' or res.text[i + 2] != 'o' or res.text[
                            i + 3] != 'r' or res.text[i + 4] != 'm':
                            i += 1
                        i += 5
                        id_item = ""
                        while res.text[i] != "'":
                            id_item += res.text[i]
                            i += 1
                        pret_int = int(pret)
                        if pret_maxim >= pret_int and i2 == - 1:
                            print("Am pus bid pe mercenar")
                            s.post(
                                f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&submod=placeBid&ttype=2&rubyAmount=3&sh={secureHash}',
                                data={'auctionid': {id_item}, 'qry': name, 'itemType': 15, 'itemLevel': level,
                                      'itemQuality': -1, 'buyouthd': 0, 'bid_amount': {pret}, 'bid': 'Ofera'})

                else:
                    i = res.text.find('mic pret', i)
                    i2 = res.text.find('Lul', i - 150, i)
                    while res.text[i] != ':':
                        i += 1
                    i += 2
                    pret = ""
                    try:
                        while True:
                            pret += res.text[i]
                            i += 1
                            try:
                                int(res.text[i])
                            except:
                                if res.text[i] == '.':
                                    i += 1
                                else:
                                    break
                    except:
                        pass
                    while res.text[i] != 'n' or res.text[i + 1] != 'F' or res.text[i + 2] != 'o' or res.text[
                        i + 3] != 'r' or res.text[i + 4] != 'm':
                        i += 1
                    i += 5
                    id_item = ""
                    while res.text[i] != "'":
                        id_item += res.text[i]
                        i += 1
                    pret_int = int(pret)
                    if pret_maxim >= pret_int and i2 == - 1:
                        print("Am pus bid pe mercenar")
                        s.post(
                            f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&submod=placeBid&ttype=2&rubyAmount=3&sh={secureHash}',
                            data={'auctionid': {id_item}, 'qry': name, 'itemType': 15, 'itemLevel': level,
                                  'itemQuality': -1, 'buyouthd': 0, 'bid_amount': {pret}, 'bid': 'Ofera'})
    except:
        pass
def buy_food_auction(pret_maxim):
    try:
        print("Sunt in buy_food_auction")
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}')
        timp_ramas = res.text.find('description_span_right')
        while res.text[timp_ramas] != '<' or res.text[timp_ramas + 1] != 'b' or res.text[timp_ramas + 2] != '>':
            timp_ramas += 1
        timp_ramas += 3
        if res.text[timp_ramas] == 'f' and res.text[timp_ramas + 7] == 's':
            res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&sh={secureHash}', data = {'doll' : 1, 'qry' : "", 'itemLevel' : 19, 'itemType' : 7, 'itemQuality' : -1})
            i = res.text.find('mic pret')
            while i != -1:
                i2 = res.text.find('Lul', i - 150, i)
                while res.text[i] != ':':
                    i += 1
                i += 2
                pret = ""
                try:
                    while True:
                        pret += res.text[i]
                        i += 1
                        try:
                            int(res.text[i])
                        except:
                            if res.text[i] == '.':
                                i += 1
                            else:
                                break
                except:
                    pass
                while res.text[i] != 'n' or res.text[i + 1] != 'F' or res.text[i + 2] != 'o' or res.text[i + 3] != 'r' or res.text[i + 4] != 'm':
                    i += 1
                i += 5
                id_item = ""
                while res.text[i] != "'":
                    id_item += res.text[i]
                    i += 1
                pret_int = int(pret)
                if pret_maxim >= pret_int and i2 == - 1:
                    print("Am pus bid pe mancare")
                    s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=auction&submod=placeBid&ttype=2&rubyAmount=3&sh={secureHash}', data = {'auctionid' : {id_item}, 'qry' : "", 'itemType' : 7, 'itemLevel' : 19, 'itemQuality' : -1, 'buyouthd' : 0, 'bid_amount': {pret}, 'bid': 'Ofera'})
                i = res.text.find('mic pret', i)
    except:
        pass
def check_market():
    print("Sunt in check_market")
    try:
        res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=market&sh={secureHash}',
                     data={'qry': '', 'seller': '', 'fl': 0, 'f': 12, 'fq': 3})
        i = res.text.find("Nici un rezultat")
        if i == -1:
            webbrowser.open("G:/probleme/python/bottravian/venv/alarm_rooster.mp3")
        res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=market&sh={secureHash}',
                     data={'qry': '', 'seller': '', 'fl': 0, 'f': 13, 'fq': 3})
        i = res.text.find("Nici un rezultat")
        if i == -1:
            webbrowser.open("G:/probleme/python/bottravian/venv/alarm_rooster.mp3")
        res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=market&sh={secureHash}',
                     data={'qry': '', 'seller': '', 'fl': 0, 'f': 11, 'fq': 3})
        i = res.text.find("Nici un rezultat")
        if i == -1:
            webbrowser.open("G:/probleme/python/bottravian/venv/alarm_rooster.mp3")
        res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=market&sh={secureHash}',
                     data={'qry': '', 'seller': '', 'fl': 0, 'f': 7, 'fq': 3})
        i = res.text.find("Nici un rezultat")
        if i == -1:
            webbrowser.open("G:/probleme/python/bottravian/venv/alarm_rooster.mp3")
    except:
        print("Nu am reusit check_market")

def place_food_for_smelt():
    print("Sunt in place_food_for_smelt")
    try:
        for i in range(1,6):
            for j in range (1,9):
                millis = int(round(time.time() * 1000))
                res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&f=7&fq=-1&qry=&page=1&sh={secureHash}')
                soup = BeautifulSoup(res.text, 'html5lib')
                supa = soup.find('input', attrs={'name' : 'packages[]'})['value']
                s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=-{supa}&fromX=1&fromY=1&to=514&toX={i}&toY={j}&amount=3', data = {'a' : millis, 'sh' : secureHash})
        print("Am terminat place_food_for_smelt")
    except:
        print("Nu am reusit place_food_for_smelt")
def go_smeltery():
    print("Sunt la go_smeltery")
    for x in range(6):
        try:
            millis = int(round(time.time() * 1000))
            s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data = {'mod' : 'forge', 'submod' : 'lootbox', 'mode' : 'smelting', 'slot' : x, 'a' : millis , 'sh' : secureHash})
            res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
                         data={'mod': 'inventory', 'submod': 'loadBag', 'bag': 514, 'shopType': 0, 'a': millis,
                               'sh': secureHash})
            id = res.text.find("data-item-id=")
            while res.text[id] != '"':
                id += 1
            id += 1
            id_item = ""
            while res.text[id] != '"':
                id_item += res.text[id]
                id += 1
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data = {'mod' : 'forge', 'submod' : 'getSmeltingPreview', 'mode' : 'smelting', 'slot' : x, 'iid' : id_item , 'amount' : 2,'a' : millis , 'sh' : secureHash})
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data = {'mod' : 'forge', 'submod' : 'rent', 'mode' : 'smelting', 'slot' : x, 'rent' : 2, 'item' : id_item, 'a' : millis , 'sh' : secureHash})
        except:
            print("Nu am reusit go_smeltery")
            #place_food_for_smelt()
    print("Am terminat go_smeltery")
def money_in_bank():
    try:
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=guildBankingHouse&sh={secureHash}')
        index = res.text.find("gold_val")
        while res.text[index] != '>':
            index += 1
        index += 1
        money_text = ''
        while res.text[index] != '<':
            if res.text[index] != '.':
                money_text += res.text[index]
            index += 1
        money = int(money_text)
        if money > 100000:
            s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=guildBankingHouse&submod=donate&sh={secureHash}', data = {'donation':money, 'doDonation':'Doneaza'})
    except:
        print("Nu am reusit money_in_bank")
def solve_shit(slot, millis):
    global poti
    t = []
    for i in range(40):
        tl = threading.Thread(target=try_lootsmelt, args=(slot, millis))
        t.append(tl)
    for i in range(40):
        t[i].start()
        if i == 39:
            poti = 1
def try_lootsmelt(slot):
    global barrier
    barrier.wait()
    try:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'lootbox', 'mode': 'smelting', 'slot': slot, 'a': millis,
                     'sh': secureHash})
        print("Done")
        return 0
    except:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'lootbox', 'mode': 'smelting', 'slot': slot, 'a': millis,
                     'sh': secureHash})
        print("Done")
        return 0
    return 0
def try_forja(x):
    global barrier
    barrier.wait()

    try:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'cancel', 'mode': 'forging', 'slot': x, 'a': millis,
                     'sh': secureHash})
        print("Done")
        return 0
    except:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'cancel', 'mode': 'forging', 'slot': x, 'a': millis,
                     'sh': secureHash})
        print("Done")
        return 0
    return 0
def try_lootfailforja(x):
    global barrier
    barrier.wait()
    try:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'lootbox', 'mode': 'forging', 'slot': x, 'a': millis, 'sh': secureHash})
        print('Done')
        return 0
    except:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'lootbox', 'mode': 'forging', 'slot': x, 'a': millis, 'sh': secureHash})
        print('Done')
        return 0
    return 0
def try_smelting(x):
    global barrier
    barrier.wait()
    try:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'cancelSmelting', 'mode': 'smelting', 'slot': x, 'a': millis,
                     'sh': secureHash})
        print("Done")
        return 0
    except:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'cancelSmelting', 'mode': 'smelting', 'slot': x, 'a': millis,
                     'sh': secureHash})
        print("Done")
        return 0
    return 0
def try_banclucru(x):
    global barrier
    barrier.wait()
    try:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data={'mod': 'forge', 'submod': 'cancel', 'mode': 'workbench', 'slot': x, 'a': millis,
                         'sh': secureHash})
        print("Done")
        return 0
    except:
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
               data={'mod': 'forge', 'submod': 'cancel', 'mode': 'workbench', 'slot': x, 'a': millis,
                     'sh': secureHash})
        print("Done")
        return 0
    return 0
def go_work(work_url):
    print("SUNT IN go_work")
    try:
        res = s.post(work_url, data = data_work)
        time_left = res.text.find('e-left')
        time_left += 8
        temporal_calcul = ""
        while res.text[time_left] != '"':
            temporal_calcul += res.text[time_left]
            time_left += 1
        timp_ramas_urm_aventura = int(temporal_calcul)
        timp_ramas_urm_aventura /= 1000
        timp_ramas_urm_aventura += 2
        print(timp_ramas_urm_aventura)
        time.sleep(timp_ramas_urm_aventura)
        print("Am terminat go_work")
    except:
        print("Nu am reusit go_work")
        time.sleep(5)
        go_work(work_url)
def go_circus_provinciarum(nivel_cautare):
    try:
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=arena&submod=serverArena&aType=3&sh={secureHash}')
        i2 = 0
        OK = 0
        i2 = res.text.find('Provincie</th')
        print("Sunt in circus_provinciarum")
        try:
            for x in range(5):

                millis = int(round(time.time() * 1000))
                i = res.text.find('<a target="_blank" href="', i2 + 50)
                i2 = res.text.find('<td>', i)
                nivel_oponent_temp = ""
                nivel_oponent_temp += res.text[i2 + 4]
                nivel_oponent_temp += res.text[i2 + 5]
                nivel_oponent = int(nivel_oponent_temp)
                if nivel_oponent < nivel_cautare:
                    OK = 1
                    while res.text[i] != 'h' or res.text[i + 1] != 'r' or res.text [i + 2] != 'e' or res.text[i + 3] != 'f':
                        i += 1
                    i += 6
                    server = ""
                    while res.text[i] != 's' or res.text[i + 1] != ':' or res.text[i + 2] != '/' or res.text[i + 3] != '/' or res.text[i + 4] != 's':
                        i += 1
                    server += res.text[i + 5]

                    try:
                        vezi_daca_e_int = int(res.text[i + 6])
                        server += res.text[i + 6]
                    except:
                        pass
                    id_server = int(server)
                    i += 59
                    while res.text[i] != '=':
                        i += 1
                    i += 1
                    id_player_temp = ""
                    while res.text[i] != '"':
                        id_player_temp += res.text[i]
                        i += 1
                    id_player = int(id_player_temp)
                    s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=arena&submod=doCombat&aType=3&opponentId={id_player}&serverId={id_server}&country=ro&a={millis}&sh={secureHash}')
                    print("Am terminat circus_provinciarum")
            #if OK == 0:
                #print("Am resetat circus_provinciarum")
            s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=arena&submod=getNewOpponents&aType=3&sh={secureHash}', data = {'actionButton' :	'Caută+Oponenţi'})
        except:
            print("Nu am reusit circus_provinciarum")
            time.sleep(5)
            go_circus_provinciarum(nivel_cautare)
    except:
        pass
def go_arena_provinciarum(nivel_cautare):
    try:
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=arena&submod=serverArena&aType=2&sh={secureHash}')
        i2 = 0
        OK = 0
        i2 = res.text.find('Provincie</th')
        print("Sunt in arena_provinciarum")
        try:
            for x in range(5):
                millis = int(round(time.time() * 1000))
                i = res.text.find('<a target="_blank" href="', i2 + 50)
                i2 = res.text.find('<td>', i)
                nivel_oponent_temp = ""
                nivel_oponent_temp += res.text[i2 + 4]
                nivel_oponent_temp += res.text[i2 + 5]
                nivel_oponent = int(nivel_oponent_temp)
                if nivel_oponent < nivel_cautare:
                    OK = 1
                    while res.text[i] != 'h' or res.text[i + 1] != 'r' or res.text [i + 2] != 'e' or res.text[i + 3] != 'f':
                        i += 1
                    i += 6
                    server = ""
                    while res.text[i] != 's' or res.text[i + 1] != ':' or res.text[i + 2] != '/' or res.text[i + 3] != '/' or res.text[i + 4] != 's':
                        i += 1
                    server += res.text[i + 5]
                    try:
                        vezi_daca_e_int = int(res.text[i + 6])
                        server += res.text[i + 6]
                    except:
                        pass
                    id_server = int(server)
                    i += 59
                    while res.text[i] != '=':
                        i += 1
                    i += 1
                    id_player_temp = ""
                    while res.text[i] != '"':
                        id_player_temp += res.text[i]
                        i += 1
                    id_player = int(id_player_temp)
                    s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=arena&submod=doCombat&aType=2&opponentId={id_player}&serverId={id_server}&country=ro&a={millis}&sh={secureHash}')
                    print("Am terminat arena_proviciarum")

            #if OK == 0:
            #print("Am resetat arena_provinciarum")
            s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=arena&submod=getNewOpponents&aType=2&sh={secureHash}', data = {'actionButton' :	'Caută+Oponenţi'})
        except:
            print("Nu am reusit arena_provinciarum")
            time.sleep(5)
            go_arena_provinciarum(nivel_cautare)
    except:
        pass
def go_arena(loc_arena_bataie):
    millis = int(round(time.time() * 1000))
    try:
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=arena&sh={secureHash}')
        if loc_arena_bataie > 0 :
            i2 = res.text.find(f'<th>{loc_arena_bataie}</th>')
            player = ""
            player += res.text[i2 + 93]
            player += res.text[i2 + 94]
            player += res.text[i2 + 95]
            player += res.text[i2 + 96]
            player += res.text[i2 + 97]
            s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doArenaFight.php?did={player}&a={millis}&sh={secureHash}')
            loc_arena_bataie -= 1
            return loc_arena_bataie
    except:
        time.sleep(5)
        go_arena(loc_arena_bataie)
def go_dungeon_Sasama_Last_Journey():
    print("Sunt in go_dungeon_Sasama_Last_Journey")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=4&sh={secureHash}',
               data={'dif2': 'Avansat'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=4&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        for x in range(1, 8):
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={x}&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_Sasama_Last_Journey")
    except:
        print("Nu am reusit go_dungeon_Sasama_Last_Journey")
def go_dungeon_heart_decay():
    print("Sunt in go_dungeon_Heart_Decay")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}',
               data={'dif2': 'Avansat'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        for x in range(1,16):
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={x}&a={millis}&sh={secureHash}')
        print("Am terminat dungeon_Heart_Decay")
    except:
        print("Nu am reusit go_dungeon_Heart_Decay")
def go_dungeon_Gioll_Passage():
    print("Sunt in go_dungeon_Gioll_Passage")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}',
               data={'dif2': 'Avansat'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        for x in range(1, 5):
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={x}&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_Gioll_Passage")
    except:
        print("Nu am reusit go_dungeon_Gioll_Passage")
        pass
def go_dungeon_In_Enemy_Hands():
    print("Sunt in go_dungeon_In_Enemy_Hands")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=5&sh={secureHash}',
               data={'dif1': 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=5&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        for x in range(1,9):
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={x}&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_In_Enemy_Hands")
    except:
        print("Nu am reusit go_dungeon_In_Enemy_Hands")
        pass
def go_dungeon_Mysterious_Laboratory():
    print("Sunt in go_dungeon_Mysterious_Laboratory")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}',
               data={'dif1': 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        for x in range(6, 0, -1):
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={x}&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_Mysterious_Laboratory")
    except:
        print("Nu am reusit go_dungeon_Mysterious_Laboratory")
def go_dungeon_Portul_Pierdut():
    print("Sunt in go_dungeon_Portul_Pierdut")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}',
               data={'dif1': 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        for position in range(1, 10):
            s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={position}&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_Portul_Pierdut")
    except:
        print("Nu am reusit go_dungeon_Portul_Pierdut")
        pass
def go_dungeon_The_Last_Resort():
    print("Sunt in go_dungeon_The_Last_Resort")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=1&sh={secureHash}',
               data={'dif2': 'Avansat'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=1&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        for x in range(1, 8):
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={x}&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_The_Last_Resort")
    except:
        print("Nu am reusit go_dungeon_The_Last_Resort")
        pass
def go_dungeon_Blood_Cavern():
    print("Sunt in go_dungeon_Blood_Cavern")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=2&sh={secureHash}', data = {'dif1' : 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=2&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=1&a={millis}&sh={secureHash}')
        fulfilledOrNot = res.text.find("Gaseste piatra violet")
        fulfilledOrNot = res.text.find("nerealizat", fulfilledOrNot, fulfilledOrNot + 150)
        if fulfilledOrNot != -1:
            s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=2&a={millis}&sh={secureHash}')
        fulfilledOrNot = res.text.find("Gaseste piatra verde")
        fulfilledOrNot = res.text.find("nerealizat", fulfilledOrNot, fulfilledOrNot + 150)
        if fulfilledOrNot != -1:
            s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=3&a={millis}&sh={secureHash}')
        fulfilledOrNot = res.text.find("Gaseste piatra albastra")
        fulfilledOrNot = res.text.find("nerealizat", fulfilledOrNot, fulfilledOrNot + 150)
        if fulfilledOrNot != -1:
            s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=4&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=6&a={millis}&sh={secureHash}')
    except:
        pass
def go_dungeon_Viking_Town():
    print("Sunt in go_dungeon_Viking_Town")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=2&sh={secureHash}', data = {'dif1' : 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=2&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        s.get(
        f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=1&a={millis}&sh={secureHash}')
        s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=2&a={millis}&sh={secureHash}')
        s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=3&a={millis}&sh={secureHash}')
        s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=4&a={millis}&sh={secureHash}')
        s.get(
        f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=5&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_Viking_Town")
    except:
        print("Nu am reusit go_dungeon_Viking_Town")
        pass
def go_dungeon_Dark_Intrigue():
    print("Sunt in go_dungeon_Dark_Intrigue")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}', data = {'dif1' : 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=3&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=1&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=2&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=3&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=4&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_Dark_Intrigue")
    except:
        print("Nu am reusit dungeon_Dark_Intrigue")
def go_dungeon_Dragon_Stronghold():
    print("Sunt in go_dungeon_Dragon_Stronghold")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=2&sh={secureHash}', data = {'dif1' : 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=2&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=1&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=2&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=3&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=4&a={millis}&sh={secureHash}')
        print("Am terminat dungeon_Dragon_Stronghold")
    except:
        print("Nu am reusit dungeon_Dragon_Stronghold")
def go_dungeon_PEFUGA():
    print("Sunt in go_dungeon_PEFUGA")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=1&sh={secureHash}', data = {'dif1' : 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=1&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=8&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=7&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=2&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=1&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=3&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=6&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=5&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=4&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_PEFUGA")
    except:
        print("Nu am reusit go_dungeon_PEFUGA")
        pass
def go_dungeon_Hidden_Grave():
    print("Sunt in go_dungeon_Hidden_Grave")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=4&sh={secureHash}', data = {'dif1' : 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=4&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=1&a={millis}&sh={secureHash}')
        s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=2&a={millis}&sh={secureHash}')
        s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=3&a={millis}&sh={secureHash}')
        s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=4&a={millis}&sh={secureHash}')
        s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=5&a={millis}&sh={secureHash}')
        print("Am terminat go_dungeon_Hidden_Grave")
    except:
        print("Nu am reusit go_dungeon_Hidden_Grave")
        pass
def go_dungeon_The_True_Owner():
    print("Sunt in go_dungeon_The_True_Owner")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=2&sh={secureHash}', data = {'dif2' : 'Avansat'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=2&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        print("Am terminat go_dungeon_The_True_Owner")
        for x in range(1, 5):
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={x}&a={millis}&sh={secureHash}')
    except:
        print("Nu am reusit go_dungeon_The_True_Owner")
        pass
def go_dungeon_Blood_Red_Sky():
    print("SUNT IN go_dungeon_Blood_Red_Sky")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=1&sh={secureHash}',
               data={'dif2': 'Avansat'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=1&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        for x in range(1, 11):
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi={x}&a={millis}&sh={secureHash}')
        print("AM TERMINAT go_dungeon_Blood_Red_Sky")
    except:
        print("Nu am reusit go_dungeon_Blood_Red_Sky")

def go_dungeon_gustavo():
    print("SUNT IN go_dungeon_gustavo")
    millis = int(round(time.time() * 1000))
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=0&sh={secureHash}', data = {'dif1' : 'Normal'})
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=dungeon&loc=0&sh={secureHash}')
        i = res.text.find('dungeonId')
        dungeonID = ""
        dungeonID += res.text[i + 18]
        dungeonID += res.text[i + 19]
        dungeonID += res.text[i + 20]
        dungeonID += res.text[i + 21]
        dungeonID += res.text[i + 22]
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=1&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=3&a={millis}&sh={secureHash}')
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doDungeonFight.php?did={dungeonID}&posi=5&a={millis}&sh={secureHash}')
        print("AM TERMINAT go_dungeon_gustavo")
    except:
        print("Nu am reusit go_dungeon_gustavo")
        time.sleep(5)
        go_dungeon_gustavo()
def repair_items(doll):
    try:
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=overview&doll={doll}&sh={secureHash}')
        if doll == 1:
            i = res.text.find('-number="3"')
            i = res.text.find('-number="3"', i + 1)
            i = res.text.find('ionat', i + 1)
            i += 6
            print(res.text[i])
            if int(res.text[i]) == 0:
                repair_eq_items(doll)
        if doll == 2:
            i = res.text.find('-number="10"')
            i = res.text.find('-number="10"', i + 1)
            i = res.text.find('ionat', i + 1)
            i += 6
            print(res.text[i])
            if int(res.text[i]) == 0:
                repair_eq_items(doll)
    except:
        pass
def repair_eq_items(doll):
    print("Sunt in repair_eq_items ", doll)
    try:
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=3&fromX=1&fromY=1&to=514&toX=1&toY=1&amount=1&doll={doll}', data = {'a':millis,'sh':secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=9&fromX=1&fromY=1&to=514&toX=1&toY=4&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=5&fromX=1&fromY=1&to=514&toX=3&toY=1&amount=1&doll={doll}'
            ,data={'a': millis, 'sh': secureHash})
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=10&fromX=1&fromY=1&to=514&toX=3&toY=4&amount=1&doll={doll}'
            , data={'a': millis, 'sh': secureHash})
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=2&fromX=1&fromY=1&to=514&toX=5&toY=1&amount=1&doll={doll}'
            , data={'a': millis, 'sh': secureHash})
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=4&fromX=1&fromY=1&to=514&toX=5&toY=3&amount=1&doll={doll}'
            , data={'a': millis, 'sh': secureHash})
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=6&fromX=1&fromY=1&to=514&toX=5&toY=5&amount=1&doll={doll}'
            , data={'a': millis, 'sh': secureHash})
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=7&fromX=1&fromY=1&to=514&toX=6&toY=5&amount=1&doll={doll}'
            , data={'a': millis, 'sh': secureHash})
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=11&fromX=1&fromY=1&to=514&toX=7&toY=1&amount=1&doll={doll}'
            , data={'a': millis, 'sh': secureHash})
        res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
                     data={'mod': 'inventory', 'submod': 'loadBag', 'bag': 514, 'shopType': 0, 'a': millis,
                           'sh': secureHash})
        item_ids = []
        x = 0
        while x != -1:
            id = ""
            x = res.text.find('id', x + 1)
            if x != -1:
                x += 4
                for i in range(7):
                    id += res.text[x]
                    x += 1
                item_ids.append(id)
        for i in range(6):
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data = {'mod':'forge','submod':'rent','mode':'workbench','slot':i,'rent':2,'item':int(item_ids[i]),'a':millis,'sh':secureHash})
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data = {'mod':'forge','submod':'storageToWarehouse','mode':'workbench','slot':i,'quality':0,'a':millis,'sh':secureHash})
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data = {'mod':'forge','submod':'start','mode':'workbench','slot':i,'a':millis,'sh':secureHash})

        time.sleep(7)
        for i in range(6):
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data = {'mod':'forge','submod':'lootbox','mode':'workbench','slot':i,'a':millis,'sh':secureHash})

        for i in range(6, 9):
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
                   data={'mod': 'forge', 'submod': 'rent', 'mode': 'workbench', 'slot': i - 6, 'rent': 2, 'item': int(item_ids[i]),
                         'a': millis, 'sh': secureHash})
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
                   data={'mod': 'forge', 'submod': 'storageToWarehouse', 'mode': 'workbench', 'slot': i - 6, 'quality': 0,
                         'a': millis, 'sh': secureHash})
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
                   data={'mod': 'forge', 'submod': 'start', 'mode': 'workbench', 'slot': i - 6, 'a': millis, 'sh': secureHash})
        time.sleep(7)
        for i in range(3):
            s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
                   data={'mod': 'forge', 'submod': 'lootbox', 'mode': 'workbench', 'slot': i, 'a': millis,
                         'sh': secureHash})
        vect_x = [1,1,1,2,4,6,2,4,6]
        vect_y = [1,2,3,1,1,1,3,3,3]
        for i in range(9):
            res = s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&f=0&fq=-1&qry=&page=1&sh={secureHash}')
            soup = BeautifulSoup(res.text, 'html5lib')
            supa = soup.find('input', attrs={'name': 'packages[]'})['value']
            s.post(
                f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=-{supa}&fromX=1&fromY=1&to=514&toX={vect_x[i]}&toY={vect_y[i]}&amount=1',
                data={'a': millis, 'sh': secureHash})
        s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=1&fromY=1&to=11&toX=1&toY=1&amount=1&doll={doll}', data = {'a':millis, 'sh':secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=1&fromY=2&to=6&toX=1&toY=1&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=1&fromY=3&to=7&toX=1&toY=1&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=2&fromY=1&to=4&toX=1&toY=1&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=6&fromY=1&to=10&toX=1&toY=1&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=4&fromY=3&to=9&toX=1&toY=1&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=2&fromY=3&to=5&toX=1&toY=1&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=4&fromY=1&to=2&toX=1&toY=1&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
        s.post(
            f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=514&fromX=6&fromY=3&to=3&toX=1&toY=1&amount=1&doll={doll}',
            data={'a': millis, 'sh': secureHash})
    except:
        print("Nu am reusit repair_eq_items")
        repair_eq_items(doll)
    print("Done repair_eq_items")
    return 0
def get_hp():
    res = s.get(f"https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=location&loc=0&sh={secureHash}")
    soup = BeautifulSoup(res.text, 'html5lib')
    puncte_ramase_hp_calcul1 = soup.select('div#header_values_hp_percent')[0].text
    temporal_calcul = ""
    temporal_calcul += puncte_ramase_hp_calcul1[0]
    if puncte_ramase_hp_calcul1[1] != '%':
        temporal_calcul += puncte_ramase_hp_calcul1[1]
        if puncte_ramase_hp_calcul1[2] != '%':
            temporal_calcul += puncte_ramase_hp_calcul1[2]
    puncte_ramase_hp = int(temporal_calcul)
    return puncte_ramase_hp

def eat():
    print("SUNT IN eat")
    millis = int(round(time.time() * 1000))
    try:
        puncte_ramase_hp = get_hp()
        print(puncte_ramase_hp)
        if puncte_ramase_hp <= 50:
            data_eat['a'] = millis
            res = s.post(load_bag_url, data=load_bag_data)
            i = res.text.find('&quot;Foloseste: Vindeca')
            i2 = res.text.find('position-x', i)
            i3 = res.text.find('position-y', i)
            i2 += 12
            i3 += 12
            print("PUNCTE HP INAINTE DE MANCARE:", puncte_ramase_hp)
            res = s.post(f"https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=512&fromX={res.text[i2]}&fromY={res.text[i3]}&to=8&toX=1&toY=1&amount=1&doll=1", data=data_eat)
            print("Am terminat eat")
    except:
        place_food_in_inventory()
def ataca_pe_edu():
    print("Sunt in ataca_pe_edu")
    millis = int(round(time.time() * 1000))
    try:
        eat()
        if get_hp() >= 70:
            s.get(f'https://s27-ro.gladiatus.gameforge.com/game/ajax/doArenaFight.php?did=16120&a={millis}&sh={secureHash}')
    except:
        print("Nu am reusit Ataca pe edu")
        pass
def accept_quests():
    OK = 0
    names = ['Circus Turma:', 'Arena:', 'inamici in expeditii, temnita sau arena']  # Pasajul Gioll, Mercenar renegat
    try:
        res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=quests&sh={secureHash}')
        i = res.text.find("acceptate")
        i += 11
        if res.text[i] == '5':
            return
        for name in names:
            i = 1
            while i != -1:
                res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=quests&sh={secureHash}')
                i = res.text.find(name, i)
                i = res.text.find("questPos", i)
                if i != -1 and res.text.find("slot_progress", i, i + 300) == -1:
                    i += 9
                    nr = ''
                    nr += res.text[i]
                    try:
                        int(res.text[i + 1])
                        nr += res.text[i + 1]
                    except:
                        pass
                    s.get(
                        f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=quests&submod=startQuest&questPos={nr}&sh={secureHash}')
                    OK = 1
                    #return
                elif i != -1:
                    i += 1

    except:
        print("Nu am reusit accept_quests")
        return
    if OK == 0:
        s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=quests&submod=resetQuests&sh={secureHash}')

def complete_quests():
    i = 1
    try:
        while i != -1:
            res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=quests&sh={secureHash}')
            i = res.text.find('button_finish', i)
            i = res.text.find('questPos', i)
            if i != -1:
                i += 9
            nr = ''
            nr += res.text[i]
            try:
                int(res.text[i + 1])
                nr += res.text[i + 1]
            except:
                pass
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=quests&submod=finishQuest&questPos={nr}&sh={secureHash}')
    except:
        print("Nu am reusit complete_quests")
    print("Am terminat complete_quests")
def restart_quests():
    i = 1
    try:
        while i != -1:
            res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=quests&sh={secureHash}')
            i = res.text.find('button_restart', i)
            i = res.text.find('questPos', i)
            if i != -1:
                i += 9
            nr = ''
            nr += res.text[i]
            try:
                int(res.text[i + 1])
                nr += res.text[i + 1]
            except:
                pass
            s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=quests&submod=restartQuest&questPos={nr}&sh={secureHash}')
    except:
        print("Nu am reusit restart_quests")
    print("Am terminat restart_quests")
def get_xp():
    res = s.get(f"https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&sh={secureHash}")
    index = res.text.find("Experienta")
    index = res.text.find(",&", index + 1)
    while res.text[index] != ';':
        index += 1
    index += 1
    xp = ''
    while res.text[index] != ' ':
        xp += res.text[index]
        index += 1
    index += 1
    while res.text[index] != ' ':
        index += 1
    index += 1
    xp_needed = ''
    while res.text[index] != '&':
        xp_needed += res.text[index]
        index += 1
    print(xp + ' / ' + xp_needed)
    return 0
def do_quests():
    complete_quests()
    restart_quests()
    accept_quests()
def duplicateItems(type = 0, quality = -1, name = ""):
    global x_place
    global y_place
    while True:
        millis1 = int(round(time.time() * 1000))
        res = s.post(f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
                     data={'mod': 'inventory', 'submod': 'loadBag', 'bag': 514, 'shopType': 0, 'a': millis, #bag 514 pt inventar III, 513 pt II
                           'sh': secureHash})
        id = res.text.find("data-item-id=")
        id_item = ""
        if id != -1:
            while res.text[id] != '"':
                id += 1
            id += 1
            while res.text[id] != '"':
                id_item += res.text[id]
                id += 1
        i = 0
        for lol in range(x_place + (y_place - 1) * 8):
            i2 = res.text.find('-amount', i + 1)
            if i2 != -1:
                i = i2
        while res.text[i] != '"':
            i += 1
        i += 1
        print(res.text[i], res.text[i + 1], res.text[i + 2])
        if res.text[i] == '1' and res.text[i + 1] == '0' and res.text[i + 2] == '0':
            x_place += 1
        if x_place == 9 and y_place < 5:
            x_place = 1
            y_place += 1
        elif x_place == 9 and y_place == 5:
            return 0
        s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php', data = {'mod':'forge','submod':'rent','mode':'workbench','slot':0,'rent':2,'item':id_item, 'a':millis, 'sh':secureHash})
        # s.post('https://s27-ro.gladiatus.gameforge.com/game/ajax.php',
        #        data={'mod': 'forge', 'submod': 'rent', 'mode': 'smelting', 'slot': 0, 'rent': 2, 'item': id_item,
        #              'a': millis, 'sh': secureHash})
        for i in range(10):
            tl = threading.Thread(target=try_banclucru, args=(0,))
            t.append(tl)
        for i in range(10):
            t[i].start()
        res = s.get(
            f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&f={type}&fq={quality}&qry={name}&page=1&sh={secureHash}')
        i = res.text.find("nu sunt pachete")
        while i == -1:
            millis2 = int(round(time.time() * 1000))
            if millis2 - millis1 >= 15000:
                break
            res = s.get(
                f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&f={type}&fq={quality}&qry={name}&page=1&sh={secureHash}')
            i = res.text.find("nu sunt pachete")
            if i == -1:
                soup = BeautifulSoup(res.text, 'html5lib')
                supa = soup.find('input', attrs={'name': 'packages[]'})['value']
                s.post(
                    f'https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=-{supa}&fromX=1&fromY=1&to=514&toX={x_place}&toY={y_place}&amount=1',
                    data={'a': millis, 'sh': secureHash})
        t.clear()
        barrier.reset()
def mergi_la_expeditii(loc_arena_bataie):
    millis = int(round(time.time() * 1000))
    try:
        print("Sunt in mergi_la_expeditii")
        do_quests()
        cauta_auction1_names = ['piatra', 'violeta']
        cauta_auction1_types = [[12], [12]]
        cauta_auction1_levels = [100, 100]
        cauta_auction1_quality = [1, 1]
        # cauta_auction2_names = ['ichorus', 'Lucius', 'Marcus', 'Antonius', 'Gaius', 'Virgil', 'Titanus', '']
        # cauta_auction2_types = [[1,2,3,4,5,6,8,9], [1,2,3,4,5,6,8,9], [1,2,3,4,5,8], [1,2,3,4,5,6,8,9], [1,2,3,4,5,6,8,9], [1,2,3,4,5,6,8,9], [1,2,3,4,5,6,8,9], [0]]
        # cauta_auction2_levels = [78, 78, 78, 80, 80, 80, 80, 50]
        # cauta_auction2_quality = [-1, -1, -1, -1, -1, -1, -1, 2]
        #ataca_pe_edu()
        # cauta_auction1_names = ['', 'Lucius', 'ichorus', 'Antonius', 'Gaius', 'Titanus', 'Virgil', 'bezn', 'infernu', 'dragon']
        # cauta_auction1_types = [[0], [7,11,12], [7,11,12], [7,11,12], [7,11,12], [7,11,12], [7,11,12], [7,11,12], [7,11,12], [7]]
        # cauta_auction1_levels = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
        # cauta_auction1_quality = [2, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        # cauta_auction2_names = ['', 'Lucius', 'ichorus', 'Antonius', 'Gaius', 'Titanus', 'Virgil']
        # cauta_auction2_types = [[0], [7,11,12], [7,11,12], [7,11,12], [7,11,12], [7,11,12], [7,11,12]]
        # cauta_auction2_levels = [50, 50, 50, 50, 50, 50, 50]
        # cauta_auction2_quality = [2, -1, -1, -1, -1, -1, -1]
        # for name, types, level, quality in zip(cauta_auction1_names, cauta_auction1_types, cauta_auction1_levels, cauta_auction1_quality):
        #     _thread.start_new_thread(check_auction1_for_item, (60000, types, level, quality, name,))
        # for name, types, level, quality in zip(cauta_auction2_names, cauta_auction2_types, cauta_auction2_levels, cauta_auction2_quality):
        #     _thread.start_new_thread(check_auction2_for_item, (25000, types, level, quality, name,))
        #check_market()
        #_thread.start_new_thread(go_smeltery, ())
        # buy_mercenaries(100000, 'samnit', 0, 96)
        # buy_mercenaries(100000, 'murmil', 0, 96)
        # buy_mercenaries(100000, 'elita', 0, 96)
        # buy_mercenaries(100000, 'maestru', 0, 96)
        # money_in_bank()
        #buy_food_auction(2000)
        eat()
        adventure_url = f"https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=location&submod=attack&location=4&stage=4&premium=0&a={millis}&sh={secureHash}"
        res = s.get(f"https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&sh={secureHash}")
        soup = BeautifulSoup(res.text, 'html5lib')
        puncte_ramase_expeditie_text = soup.find('span', attrs={'id': 'expeditionpoints_value_point'}).text
        puncte_ramase_expeditie = int(puncte_ramase_expeditie_text)
        while puncte_ramase_expeditie > 0:
            # for name, types, level, quality in zip(cauta_auction1_names, cauta_auction1_types, cauta_auction1_levels, cauta_auction1_quality):
            #     _thread.start_new_thread(check_auction1_for_item, (60000, types, level, quality, name,))
            # for name, types, level, quality in zip(cauta_auction2_names, cauta_auction2_types, cauta_auction2_levels, cauta_auction2_quality):
            #     _thread.start_new_thread(check_auction2_for_item, (25000, types, level, quality, name,))
            #_thread.start_new_thread(go_smeltery, ())
            # buy_mercenaries(100000, 'samnit', 0, 96)
            # buy_mercenaries(100000, 'murmil', 0, 96)
            # buy_mercenaries(100000, 'elita', 0, 96)
            # buy_mercenaries(100000, 'maestru', 0, 96)
            #buy_food_auction(2000)
            if get_hp() >= 45:
                res = s.get(adventure_url)
            eat()
            res = s.get(f"https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&sh={secureHash}")
            soup = BeautifulSoup(res.text, 'html5lib')
            puncte_ramase_expeditie_text = soup.find('span', attrs={'id': 'expeditionpoints_value_point'}).text
            puncte_ramase_expeditie = int(puncte_ramase_expeditie_text)
            res = s.get(f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=location&loc=0&sh={secureHash}')
            time_left = res.text.find('e-left')
            time_left += 8
            temporal_calcul = ""
            while res.text[time_left] != '"':
                temporal_calcul += res.text[time_left]
                time_left += 1
            try:
                # money_in_bank()
                repair_items(1)
                repair_items(2)
                do_quests()
                #check_market()
                #ataca_pe_edu()
                timp_ramas_urm_aventura = int(temporal_calcul)
                timp_ramas_urm_aventura /= 1000
                timp_ramas_urm_aventura += 1
                eat()
                go_dungeon_Mysterious_Laboratory()
                go_circus_provinciarum(103)

                if get_hp() >= 45:
                    go_arena_provinciarum(102)
                #eat()

                #loc_arena_bataie = go_arena(loc_arena_bataie)

                print(puncte_ramase_expeditie)
                print("Am terminat mergi_la_expeditii")
                if puncte_ramase_expeditie > 0:
                    time.sleep(timp_ramas_urm_aventura)
            except KeyboardInterrupt:
                print("Keyboard inrerupt")
                sys.exit(1)
            except:
                print("Nu am reusit mergi_la_expeditii")
        if get_hp() >= 45:
            go_arena_provinciarum(102)
        go_circus_provinciarum(103)
        get_xp()
        time.sleep(50)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        sys.exit(1)
    except:
        pass
def decode_header(header,old_headers):
    for head in header:
        if not head in old_headers.keys():
            old_headers[head] = ""

        old_headers[head] += header[head]
    return old_headers
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}
load_bag_data = {'mod' : 'inventory', 'submod' : 'loadBag', 'bag' : '512' , 'shopType' : 0, 'a' : '1556001777332', 'sh' : ""}
login_data = {
    'name' : 'etc',
    'pass' : 'etc212',
    'g-recaptcha-response': '',
    'login_server' : 's27-ro.gladiatus.gameforge.com/game/index.php?mod=start&submod=login'
}
data_eat ={
    'a' : '',
    'sh' : ''
}
data_place_in_inventory = {
    'a' : '',
    'sh' : ''
}
data_work = {'dollForJob7' : 1, 'timeToWork' : 1, 'jobType' : 4}

def get_hash(text):
    i = text.find("secureHash")
    secureHash = ""
    OK = 2
    while OK:
        if res.text[i] == "=":
            i += 2
            while OK:
                if res.text[i] == '"':
                    OK -= 1
                else:
                    secureHash += res.text[i]
                i += 1
        i += 1
    return secureHash
with requests.Session() as s:
    url = 'https://ro.gladiatus.gameforge.com/game/'
    login_url = 'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=start&submod=login'
    res = s.get(url)
    res = s.post(login_url, data=login_data, headers=headers)
    headers = res.headers.copy()
    secureHash = get_hash(res.text)
    starting_page_url = f"https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=location&loc=0&sh={secureHash}"
    adventure_url = f"https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=location&submod=attack&location=1&stage=2&premium=0&a=1554983095452&sh={secureHash}"
    load_bag_url = 'https://s27-ro.gladiatus.gameforge.com/game/ajax.php'
    # PENTRU EAT : ----Trebuie modificat from X & Y(pozitiile din inventar),
    # To e bine setat asa(caracterul tau)
    # Si e post request(trebuie sa trimiti si data_eat)
    eat_url = f"https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=512&fromX={1}&fromY={1}&to=8&toX=1&toY=1&amount=1&doll=1"
    place_in_inventory_url = f"https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=-763582&fromX=1&fromY=1&to=512&toX={1}&toY={1}&amount=1"
    work_url = f'https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=work&submod=start&sh={secureHash}'
    res = s.get(f"https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&sh={secureHash}")
    load_bag_data['sh'] = secureHash
    data_eat['sh'] = secureHash
    soup = BeautifulSoup(res.text, 'html5lib')
    puncte_ramase_expeditie_text = soup.find('span', attrs={'id' : 'expeditionpoints_value_point'}).text
    puncte_ramase_expeditie = int(puncte_ramase_expeditie_text)
    # while True:
    #     mergi_la_expeditii(26)
    # go_smeltery()
    barrier = threading.Barrier(10)
    t = []
    # for i in range(10):
    #     tl = threading.Thread(target=try_forja, args=(0,))
    #     t.append(tl)
    # for i in range(10):
    #     t[i].start()
    y_place = 1
    x_place = 1
    duplicateItems(20, -1, 'antonius')
    #repair_eq_items(1)
items_id = {
    'Arme' : 1,
    'Scuturi' : 2,
    'Platosa' : 3,
    'Coifuri' : 4,
    'Manusi' : 5,
    'Inele' : 6,
    'Utilizabile' : 7,
    'Papuci' : 8,
    'Amulete' : 9,
    'Saltari' : 11,
    'Imbunatatiri' : 12,
    'Mercenar' : 15,
    'Pergamente' : 20
}
"""
    for i in range(6):
        s.get(adventure_url)
        time.sleep(10)
        if i % 5 == 0:
            s.post(eat_url, data_eat)
    print(res.text)
    soup = BeautifulSoup(res.text, 'html5lib')
    data_place_in_inventory['sh'] = secureHash
    numar = 0
    while soup.find('input', attrs={'name' : 'packages[]'})['value'] != 0 and numar < 100:
        supa = soup.find('input', attrs={'name' : 'packages[]'})['value']
        for i in range(1,6):
            for j in range(1,9):
                place_in_inventory_url = f"https://s27-ro.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=-{supa}&fromX=1&fromY=1&to=512&toX={i}&toY={j}&amount=1"
                s.post(place_in_inventory_url, data=data_place_in_inventory)
        res = s.get(f"https://s27-ro.gladiatus.gameforge.com/game/index.php?mod=packages&sh={secureHash}")
        soup = BeautifulSoup(res.text, 'html5lib')
        numar += 1
    data_eat['sh'] = secureHash
    res = s.post(eat_url, data = data_eat)
    #print(res.text)
"""