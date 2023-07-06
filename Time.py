from datetime import datetime
from jdatetime import datetime as jdatetime_datetime, date as jdate, timedelta

prev_choice = None
while True:
    print("Yeki Az GozineHa Ra Entekhab Konid:")
    print("1. Mohasebe Sen")
    print("2. Tabdil Tarikh Shamsi Be Miladi")
    print("3. Mohasebe Tedad Rooz 2 Tarikh")
    print("0. Khorooj")
    choice = input("Yeki Az GozineHa Ra Entekhab Konid: ")

    if choice == "1":
        if prev_choice == "1":
            
            continue
        birth_date_str = input("Tarikh Tavalod Khod Ra Vared Konid (Format Miladi YYYY/MM/DD): ")
        birth_date = datetime.strptime(birth_date_str, "%Y/%m/%d").date()
        today = datetime.today().date()
        age_delta = today - birth_date
        age_years = age_delta.days // 365
        age_months = (age_delta.days % 365) // 30
        age_days = (age_delta.days % 365) % 30
        print(f"Shoma {age_years} Saal {age_months} Mah {age_days} Rooz Darid.")
        prev_choice = "1"

    elif choice == "2":
        if prev_choice == "2":
            
            continue
        j_date_str = input("Tarikh Shamsi Ra Vared Konid (Format YYYY/MM/DD): ")
        j_year, j_month, j_day = map(int, j_date_str.split('/'))
        g_date = jdatetime_datetime(j_year, j_month, j_day).togregorian()
        g_date_str = g_date.strftime("%Y/%m/%d")
        print(f"Tarikh Miladi: {g_date_str}")
        prev_choice = "2"

    elif choice == "3":
        if prev_choice == "3":
            
            continue
        date1_str = input("Tarikh Aval Ra Vared Konid (Format Miladi YYYY/MM/DD): ")
        date2_str = input("Tarikh Dovom Ra Vared Konid (Format Miladi YYYY/MM/DD): ")
        date1 = datetime.strptime(date1_str, "%Y/%m/%d").date()
        date2 = datetime.strptime(date2_str, "%Y/%m/%d").date()
        delta = date1 - date2
        print(f"Tafazol Tarikh: {delta.days} Rooz")
        prev_choice = "3"


    elif choice == "0":
        print("GoodBye")
        break

    else:
        print("Lotfan Yeki Az GozineHa Ra Entekhab Konid")
        continue

    go_back = input("Aya Mikhahid Be Marhale Ghabl Bargardid? (Y/N) ")
    if go_back.lower() == "Y":
        choice = prev_choice
        prev_choice = None
    else:
        print("GoodBye")