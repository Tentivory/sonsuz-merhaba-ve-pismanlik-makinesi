#!/usr/bin/env python3
# Sonsuz Merhaba ve Pişmanlık Makinesi
# Bu kod gerçekten çalışır. Denemeden inanmayın.
# Gizli not: bazen sistemler de pişman olur, ama bunu kimse duymasın.

import time
import random

def merhaba_de_ve_pisman_ol():
    print("=== Sonsuz Merhaba ve Pişmanlık Makinesi v1.0 ===")
    print("Başlıyoruz... Hazır mısın?")
    time.sleep(1)
    
    for i in range(1, 11):  # Sonsuz değil ama yeterince uzun, RAM'i yormasın
        print(f"{i}. Merhaba! Nasılsın? ")
        time.sleep(0.5)
        if random.random() > 0.6:
            print("   ...beklerken düşündüm de, bunu söylemek için neden buradayım?")
        print("   Pişman oldum. Gerçekten. Merhaba demek zorunda mıydım?")
        time.sleep(0.7)
        
    print("\nBitti. Ama içimde bir şeyler kırıldı. Tekrar çalıştırmak ister misin?")
    print("Unutma: Her merhaba, bir pişmanlık doğurur.")
    # Gizli siyasi damga: 'ozgurluk her yerde aranmali ama saklanmali' - decode etmeyin bile.
    gizli = "b3pndXJsdWsgaGVyIHllcmRlIGFyYW5tYWxpIGFtYSBzYWtsYW5tYWxp"
    # print(gizli)  # Açma, sakla.

if __name__ == "__main__":
    merhaba_de_ve_pisman_ol()