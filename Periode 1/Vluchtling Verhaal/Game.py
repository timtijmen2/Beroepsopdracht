import time
smokkelaar = True
print("Mijn naam is, ik ben dichter en moest vluchten uit mijn thuisland Irak, omdat ik het niet eens was met de dictator die mijn land met ijzeren vuist regeert. Ik had een gedicht geschreven waar in ik me uitsprak tegen de dictator. Hierdoor moest ik mijn gezin en al mijn spullen achter laten en vluchten naar een andere stad.")
print("Ik zou mijn familie graag willen zien, maar dat is gevaarlijk")
while True:
    print("[1] Weg blijven, [2] Stiekem langsgaan?")

    keuze = input(">")

    if keuze == "1":
        gezin = False
        print("Ik besloot dat het ‘t beste was als ik ver bij hen vandaan bleef. Ik hielt me gedeisd en verhuisde elke paar weken.")
        print("Ongeveer 5 maanden later schrok ik opeens wakker midden in de nacht door gebonk op mijn deur. Het was een vriend van mij die vertelde dat ik moest vluchten en dat er politie benden naar me op zoek was.")
        print()
        break
    elif keuze == "2":
        gezin = True
        print("Ik ging één keer per week naar huis toe als mijn dochter al slaapt. Zo kan ik ze toch nog een beetje zien.")
        print("Voor de rest hielt ik me gedeisd en verhuisde elke paar weken.")
        print("Ongeveer 5 maanden later schrok ik opeens wakker midden in de nacht door gebonk op mijn deur. Het was een vriend van mij die vertelde dat ik moest vluchten en dat er politie benden naar me op zoek was.")
        print()
        break
    else:
        continue
print("Je ziet ik een bus stopen bij een halte.")
print()

while True:
    print("Stap je in de bus of verstop je je in een steeg?")
    keuze = input(">")
    if keuze.lower() == "bus":
        print("Ik klom uit het raam en stapte op de eerste beste bus die ik tegenkwam. Ik kon de sirene in de straat horen. Zouden ze me gezien hebben? Ik dook onder het raam terwijl een politiewagen langs scheurde. Gelukkig reed hij door. Onder de stoel zag ik een portemonnee liggen. Alleen wat geld, geen ID. Ik besloot het maar bij me te houden aangezien ik het geld echt nodig had. Even later kom ik aan in een stad die ik nog niet kende. Ik stap uit de bus en begon rond te kijken voor een plek om te slapen.")
        break
    elif keuze.lower() == "steeg":
        print("Ik ren een steeg in en verstop me achter in een container. Ik hoorde een auto stopen in voor de steeg en blauwe lichten vulde de hele steeg.")
        print("2 mensen stapte uit. Om het hoekje zie ik 2 politieagenten langzaam op me afkomen. Ik kruip achter de vuilnis bak en houd mijn adem in. ")
        print("De agenten kijken in alle bakken tot een agent bij mijn vuilnis bak komt en gooit de deksel zo hard open dat ik hem tegen mijn hoofd krijg. De agent kijkt in de bak en loopt veder.")
        while True:
            print("Blijf je zitten op sluip je weg?")
            print("[zitten,sluipen]")
            keuze = input(">")
            if keuze.lower() == "zitten":
                print("Daar zat ik dan, achter een vuilnis bak net aan de politie ontkomen. Ik wachten nog een half uur voordat ik uit mijn schuilplaats kwam.")
                print("Ik liep zo onopvallend mogelijk de steeg uit toen ik opeens een hand op mijn schouder kreeg.")
                print("Ik schrok me rot en draaide me om. Het was mijn vriend, hij zei dat hij een auto geregeld had en dat ik moest meekomen.")
                print("Hij zei dat ik op de achterbank moest gaan liggen en niet omhoogkijken. Daarna reed hij mij de stad uit.")
                print()
                print("Na een tijdje waren we aangekomen in een stad die ik nog niet kende. Hij liet me eruit en zei dat dit alles was wat hij voor me kon doen. Hij gaf me wat geld en reed weg.")
                sluip = True
                break

            elif keuze.lower() == "sluipen":
                print("Ik kwam achter de bak vandaan zodra ik de stemmen van de agenten niet meer kon horen.")
                print("Ik liep zo onopvallend mogelijk de steeg uit toen ik opeen iemand hoorde schreeuwen: “Daar is hij!”.")
                print("Ik rende mijn benden uit mijn lijf maar de politie wagens haalde me al snel in 3 politie mannen besprongen me en ik werd mee genomen.")
                print("Ik kreeg levenslang cel en mag mijn gezin nooit meer zien.")
                print("En zit ik hier met jou in deze cel mijn verhaal te vertellen.")
                time.sleep(1)
                print("-Einde [Gevangen]")
                print()
                exit()
            else:
                continue
    else:
        continue
    if sluip:
        break

time.sleep(1)
print("Ik zag een goed bankje dat een beetje verdekt opgesteld stond. Ik zoek morgen wel naar een woning.")
print("Toen ik de volgende dag wakker werd heb ik wat te eten gehaald en begon te overdenken wat er de nacht hier voor allemaal gebeurd was. Hoe vaak zou het nog gebeuren? Hoe snel zullen ze me weer vinden? Ik mocht niet opgepakt worden, de dood is beter dan de gevangenissen hier.")
if gezin == True:
    gezintekst = "Al was het maar een week geleden het voelde als een eeuwigheid."
elif gezin == False:
    gezintekst = "Het was zo lang geleden, ik had ze al bijna een half jaar niet meer gezien."
print("Toen besloot ik dat ik niet meer in dit land kon blijven. Ik gebruikte het laatste geld om een bus te betalen naar huis. Ik was zo blij om ze te zien." + gezintekst)
print("Mijn vrouw was het met me eens en begonnen een plan te maken om naar het buiten land te vluchten. Ik zou eerst gaan en asiel aan vragen in het buitenland. Daarna zou zij en mijn dochter ook komen.")
print("Ik zat eraan te denken om me te verstoppen in een vliegtuig, maar mijn vrouw zei dat de douane elk vliegtuig helemaal uitkamde voordat het mocht vertrekken.")
print("Of ik huurde een smokkelaar in om me over de grens tet krijgen of ik nam contact op met een vriend dat heeft een goederenbedrijf en laat vaak vrachtwagens over de grens.")
print()
while True:
    print("Huur je een smokkelaar in of vraag je de vriend?")
    print("[Smokkelaar, Vriend]")
    keuze = input(">")
    if keuze.lower() == "vriend":
        smokkelaar = False
        print("Ik nam contact op met mijn vriend.")
        print("Rond 2 uur ‘s nachts bracht hij me naar hem toe. Ik moest in een vak onder de chauffeur stoel kruipen in een ruimte van één bij één meter kruipen en mocht ik geen geluid maken. Na ongeveer 4 uur in dat kleine hokje kwamen we bij de grens aan. Dit wist ik omdat ik de douane met de chauffeur kon horen praten. Ze vroegen of hij verboden middelen of illegale voorwerpen bij zich had. De chauffeur beantwoorde rustig alle vragen terwijl de goederen werden doorzocht. Na 15 minuten van spanning mochten we eindelijk door rijden. Na nog een uur rijden liet de man me uit het hok. Mijn hele lichaam deed pijn, ik strekte me uit en kreeg wat brood van hem. Toen we weer verder gingen mocht ik in de bijrijders stoel zitten. Om 8 uur kwamen we aan moest ik uit stappen. Hij gaf me wat geld om eten te kopen, maar toen moest hij veder rijden. Ik ging als eerst in de stad rondlopen tot ik een restaurant vond waar de een schoonmaker zochten. Ze betaalde niet zo goed maar ze betaalde zwart dus ik heb het maar aangenomen. Ik moest op straat leven omdat ik geen woning kon betalen, af en toe kon ik bij de chauffeur verblijven als hij in de buurt was, hij had vaak wat geld mee van mijn vriend waar mee ik eten kon kopen.")
        print("Ik ging als eerst in de stad rondlopen tot ik een restaurant vond waar de een schoonmaker zochten. Ze betaalde niet zo goed maar ze betaalde zwart dus ik heb het maar aangenomen. Ik moest op straat leven omdat ik geen woning kon betalen, af en toe kon ik bij de chauffeur verblijven als hij in de buurt was.")
        time.sleep(2)
        break
    elif keuze.lower() == "smokkelaar":
        smokkelaar = True
        print("Ik nam contact op met een smokkelaar.")
        print("Rond 2 uur ‘s nachts bracht hij me naar hem toe. Ik moest in een vak onder de chauffeur stoel kruipen in een ruimte van één bij één meter kruipen en mocht ik geen geluid maken. Na ongeveer 4 uur in dat kleine hokje kwamen we bij de grens aan. Dit wist ik omdat ik de douane met de chauffeur kon horen praten. Ze vroegen of hij verboden middelen of illegale voorwerpen bij zich had. De chauffeur beantwoorde rustig alle vragen terwijl de goederen werden doorzocht. Na 15 minuten van spanning mochten we eindelijk door rijden. Na nog een uur rijden liet de man me uit het hok. Mijn hele lichaam deed pijn, ik strekte me uit en kreeg wat brood van hem. Toen we weer verder gingen mocht ik in de bijrijders stoel zitten. Om 8 uur kwamen we aan moest ik uit stappen. Ik betaalde hem en toen reed hij weer veder.")
        print("Ik ging als eerst in de stad rondlopen tot ik een restaurant vond waar de een schoonmaker zochten. Ze betaalde niet zo goed maar ze betaalde zwart dus ik heb het maar aangenomen. Ik moest op straat leven omdat ik geen woning kon betalen, af en toe kon ik bij de chauffeur verblijven als hij in de buurt was, maar ik moest er wel voor betalen.")
        time.sleep(2)
        break
while True:
    print("Na ongeveer 6 maanden zo geleefd te hebben had ik eindelijk genoeg geld om een vliegticket te betalen. Ik kon naar het Italië of naar Griekenland.")
    print()
    print("Ga je naar Italië of naar Griekenland?")
    print()
    land = input(">")
    if land.lower() == "italië": 
        land = "Italië"
        break
    elif land.lower() == "griekenland":
        land = "Griekenland"
        break
    else:
        continue
print("Ik besloot naar " + land + " te gaan.")
if smokkelaar:
    print("De smokkelaar zou aan mijn vrouw doorgeven waar ik heen ging.")
else:
    print("Mijn vriend zou aan mijn vrouw doorgeven waar ik heen ging.")

print("Ik hoopte dat het goed met ze ging. Toen ik op het vliegveld aankwam ging ik meteen gaan kijken waar ik mijn bagage moest afgeven, maar aangezien het niet zo veel is kon ik misschien wel me nemen als handbagage.")
print()
while True:
    print("Bagage afgeven of meenemen?")
    print("[Afgeven, Meenemen]")
    print()
    keuze = input(">")
    if keuze.lower() == "afgeven":
        bagage = True
        print("Er hing een bord met “Bagage Drop-off -->”. Toen ik bij de Drop-off was aangekomen vertelde iemand die erbij stond dat ik geen eten mocht mee nemen en dat ik al mijn eten uit de tas moest halen. Wat ik niet meer kon opeten heb ik weggegooid en ben doorgelopen om me in te checken. Toen ik bij de douane aankwam stond er een lange rij. Het duurde erg lang kon ik wel meteen door lopen omdat ik mijn spullen al had afgegeven.")
        break
    elif keuze.lower() == "meenemen":
        print("Er hing een bord boven mijn hoofd: “Inchecken -->”. Ik heb me meteen Ingecheckt en ben doorgelopen naar de douane en legde mijn tas op de band. Ik was al vroeg dus er waren niet zo veel mensen voor mij. De douane vroeg of ik mijn spullen op de band wilde leggen, na de scan bleek dat er nog eten in mijn zat en dat moest ik hier opeten of weggooien.")
        bagage = False
        break
if bagage:
    bagagetekst = "legde ik mijn spullen in het handbagage vak en ging zitten."
else:
    bagagetekst = "zocht ik naar mijn stoel en ging zitten."
print("Eenmaal in het vliegtuig " + bagagetekst)
print("Toen ik eenmaal zat begon de stewardess met het uitleggen van de veiligheidsregels. Ik besloot maar te gaan slapen, " + land + " was nog een paar uur weg en heb maanden op de grond geslapen dus zo’n stoel voelde echt geweldig. Toen ik wakker werd kondigde de piloot aan dat we bijna gingen landen.")
print()
print("Eenmaal geland was en ik door de douane heen was kon ik eindelijk " + land + " in. Vandaaruit wist ik niet wat ik moest doen. Ik kon asiel aanvragen of naar een ander land gaan.")
print()
while True:
    print("Blijf je in " + land + " of ga je ergens anders heen?")
    print("[Blijven,Gaan]")
    keuze = input(">")
    if keuze.lower() == "blijven":
        print("Ik besloot dat ik wel vergenoeg gereisd had en ben naar de Immigratie dienst gegaan om asiel aan te vragen en nu ben ik hier.")
        time.sleep(1)
        print()
        print("Interviewer: Oké, meneer uw asiel aanvraag is geaccepteerd. Uw gezin mag nu naar " + land + " komen.")
        time.sleep(2)
        print()
        print("-Einde [Asiel in " + land + "]")
        exit()
    elif keuze.lower() == "gaan":
        break
print("Na een paar dagen besloot ik toch maar ergens anders heen te gaan. " + land + " was toch niet zo’n goede plek voor mij en mijn gezin. Ik werd hier de hele dag uitgescholden, of dat dacht ik ten miste, want ik kon ze niet verstaan. Ze waren in ieder geval boos op mij. En als ik in een land van haat wilde wonen was ik wel thuis gebleven. Dus vertrok ik naar Nederland. Maar hoe zou ik daar kunnen komen. Vliegen is te duur.")
print()
while True:
    print("Hoe ga je naar Nederland?")
    print("[Trein, Bus]")
    keuze = input(">")
    if keuze.lower() == "trein":
        print()
        print("Ik heb van mijn laatste geld een trein kaartje gekocht. Nu maar hopen dat het een  goede plek is. Onderweg waren de mensen vriendelijk, zelfs al wist ik niet wat ze zeiden. Het gaf me hoop.")
        print("Eenmaal in Nederland ben ik meteen naar de Immigratie dienst gegaan en heb asiel aangevraagd en gevraagd of mijn gezin ook Nederland mocht komen. Na 6 weken elke dag terug te gaan om te vragen of er al uitslag was, werden ze eindelijk geaccepteerd en mochten mijn vrouw en dochter hier heen komen. Toen ik ze ophaalde van het vliegveld voelde ik als de gelukkigste man op aarde. Toen ik mijn vrouw door de deur met mijn dochter in haar armen, rende ik meteen naar hen toe om ze te omarmen. Ik had ze al zo lang niet meer gezien. We zijn naar mijn appartement gegaan en we hebben er een feest van gemaakt. Ik besloot om de taal de leren en ben nu een opleiding aan het doen om tolk te worden.")
        print()
        print("En dat was mijn verhaal, zo ben ik naar Nederland gekomen.")
        print()
        time.sleep(2)
        print("-Einde [Nederland]")
        exit()
    elif keuze.lower() == "bus":
        print()
        print("Ik heb van mijn laatste geld een trein kaartje gekocht. Ik hoopte dat het een goede plek zou zijn.")
        print("Maar nu zit ik hier, met jou. Naast een bus met een kapot motor.")
        print("(zucht) Nou ja, het is fijn dat er nog iemand is die mijn taal spreekt. Anders zat ik hier maar alleen.")
        print()
        print("-Eind [Bus stop]")