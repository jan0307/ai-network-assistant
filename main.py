from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def fraga_ai(problem):
    try:
        prompt = f"""
Du är en AI Network Assistant.
Din uppgift är att hjälpa användaren felsöka nätverksproblem.

Användarens problem:
{problem}

Förklara den troliga orsaken på ett enkelt sätt.
Ge sedan felsökningssteg i rätt ordning.
"""
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text
    except Exception as error:
        return f"AI-tjänsten kunde inte svara. fel: {error}"

def visa_startmeddelande():
    print("AI Network Assistant")
    print("programmet har startat!")

def felsok_dns():
    print("1. Kontrollera vilken DNS-server datorn använder.")
    print("2. Testa att pinga en IP-adress.")
    print("3. Testa sedan att pinga ett domännamn.")
    print("4. Om IP fungerar men domännamnet inte fungerar kan problemet vara DNS.")

def felsok_internet():
    while True:
        anslutning = input("Är nätverkskabeln ansluten eller Wi-Fi aktivt? ja/nej: ").lower()

        if anslutning == "nej":
            print("Kontrollera nätverkskabeln eller anslut till Wi-Fi.")
            break

        elif anslutning == "ja":
            break
        else:
            print("Ogiltigt svar. Skriv ja eller nej.") 

    if anslutning =="ja":
        print("bra. nästa steg är att kontrollera om datorn har fått en IP-adress.")

        while True:
            ip_adress = input("Har datorn fått en IP-adress? ja/nej: ").lower()

            if ip_adress == "nej":
                print("kontrollera IP-inställningarna eller om DHCP fungerar.")
                break

            elif ip_adress == "ja":
                break
            else:
                print("Ogiltigt svar för IP-adress. Skriv ja eller nej.")
        if ip_adress =="ja":  
            print("bra. Datorn har en IP-adress.")
            while True:
                gateway = input("Har datorn en default gateway? ja/nej: ").lower()

                if gateway == "nej":
                    felsok_gateway()
                    break

                elif gateway == "ja":
                     break
                else:
                    print("Ogiltigt svar för gateway. Skriv ja eller nej.")

            if gateway =="ja":
                print("Bra. Datorn har en default gateway.")
                while True:
                    ping_gateway = input("Kan du pinga default gateway? ja/nej: ").lower()

                    if ping_gateway == "nej":
                        print("Default gateway svarar inte på ping. Kontrollera router, kabel eller Wi-Fi.")
                        break

                    elif ping_gateway == "ja":
                        break
                    else:
                        print("Ogiltigt svar för ping gateway. Skriv ja eller nej.")
                if ping_gateway == "ja":    
                    print("Bra. Default gateway svarar på ping.")
                    while True:
                        ping_internet = input("Kan du pinga en IP-adress på internet? ja/nej: ").lower()

                        if ping_internet == "nej":
                            print("Datorn når default gateway men inte internet. Problemet kan ligga i routern eller internetanslutningen.")
                            break

                        elif ping_internet == "ja":
                            break
                        else:
                            print("Ogiltigt svar för ping internet. Skriv ja eller nej.")
                    if ping_internet == "ja":
                            print("Bra. Datorn kan nå internet via en IP-adress.") 
                            while True:
                                ping_doman = input("Kan du pinga ett domännamn, till exempel google.com? ja/nej: ").lower()

                                if ping_doman == "nej":
                                    print("IP-adresser fungerar men domännamn fungerar inte. Problemet kan vara DNS.")
                                    felsok_dns()
                                    break

                                elif ping_doman == "ja":
                                    break
                                else:
                                    print("Ogiltigt svar för domännamn. Skriv ja eller nej.")
                            if ping_doman == "ja":
                                print("Bra. DNS fungerar också.")
                            

                        
                    
            
                               
             

def felsok_gateway():
    print("1. Kontrollera vilken default gateway datorn har.")
    print("2. Kontrollera att gateway-adressen ligger i samma nätverk som datorns IP-adress.")
    print("3. Testa att pinga default gateway.")
    print("4. Om gateway inte svarar, kontrollera router, kabel eller Wi-Fi.")

def felsok_wifi():
    print("1. Kontrollera att Wi-Fi är aktiverat.")
    print("2. Kontrollera att du är ansluten till rätt nätverk.")
    print("3. Kontrollera om datorn har fått en IP-adress.")     
    print("4. Testa att pinga default gateway.")

def felsok_ip():
    print("kontrollera datorns IP-adress och att den ligger i rätt nätverk.") 

def felsok_ping():
    print("kontrollera om enheten är nåbar och om brandväggen blockerar ICMP.")

def felsok_kabel():
    print("1. Kontrollera att nätverkskabeln sitter ordentligt.")
    print("2. Kontrollera om kabeln är skadad.")
    print("3. Testa en annan nätverkskabel.")
    print("4. Kontrollera om nätverksportens lampor lyser.")

def visa_problem(problem):
    print("du skriver",problem)

visa_startmeddelande()

while True:
    problem = input("beskriv ditt nätverksproblem: ").lower()

    if problem == "avsluta":
        print("AI Network Assistant avslutas. Hej då!")
        break    

    visa_problem(problem)

    if problem == "ai":
        ai_problem = input("beskriv nätverksproblemet för AI: ")
        ai_svar = fraga_ai(ai_problem)
        print(ai_svar)

    elif "internet" in problem:
        felsok_internet()

    elif "dns" in problem:
        felsok_dns()

    elif "gateway" in problem:
        felsok_gateway()

    elif "wifi" in problem or "wi-fi" in problem:
        felsok_wifi()

    elif "ip" in problem or "ip-adress" in problem or "ip adress" in problem:
        felsok_ip()
            

    elif "ping" in problem or "pinga" in problem:
        felsok_ping()
    

    elif "kabel" in problem or "ethernet" in problem:
        felsok_kabel()    

    else:
        print("jag känner inte igen problemet än.")