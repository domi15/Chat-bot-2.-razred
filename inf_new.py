import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import textwrap

# Download Croatian resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Set up stop words
croatian_stop_words = [
    "i", "ili", "ali", "a", "u", "za", "s", "sa", "o", "po", "na", "nad", "iznad",
    "pod", "ispod", "kroz", "preko", "kao", "tako", "također", "međutim", "no", "bez",
    "do", "od", "kod", "oko"  # Add more Croatian stop words as needed
]
stop_words = set(stopwords.words('english')).union(set(croatian_stop_words))

# Define your knowledge base
knowledge_base = {
    "Što je IoT": "IoT je mreža fizičkih uređaja, vozila, kućanskih aparata i drugih predmeta koji su opremljeni senzorima, softverom i mrežnom povezanošću kako bi mogli razmjenjivati podatke i međusobno komunicirati.",
    "Što znači Internet of Things": "Internet stvari (IoT) opisuje fizičke objekte (ili grupe takvih objekata) sa senzorima, sposobnošću obrade, softverom i drugim tehnologijama koje se povezuju i razmjenjuju podatke s drugim uređajima i sustavima putem interneta ili drugih komunikacijskih mreža. Internet stvari smatra se pogrešnim nazivom jer uređaji ne moraju biti povezani s javnim internetom, samo trebaju biti povezani s mrežom i imati mogućnost individualne adrese.",
    "Što su senzori u kontekstu Internet stvari?": "Senzori su uređaji koji prikupljaju podatke iz okoline ili uređaja i prenose ih u IoT mrežu radi daljnje obrade i analize.",
    "Kako IoT uređaji komuniciraju međusobno?": "IoT uređaji komuniciraju putem različitih komunikacijskih protokola kao što su Wi-Fi, Bluetooth, Zigbee i LoRaWAN.",
    "Koje su primjene Internet stvari u pametnim gradovima?": "IoT se može primijeniti u pametnim gradovima za upravljanje prometom, pametno osvjetljenje, praćenje kvalitete zraka, sustave pametnih parkiranja i mnoge druge svrhe.",
    "Kako IoT utječe na industrijski sektor (Industrija 4.0)?": "IoT omogućuje praćenje i upravljanje industrijskim procesima, optimizaciju lanaca opskrbe, povećanje produktivnosti i smanjenje troškova kroz upotrebu senzora, robotike i analitike podataka.",
    "Kako se osigurava sigurnost u IoT mreži?": "Sigurnost u IoT mreži postiže se kroz različite metode kao što su enkripcija podataka, autentikacija uređaja, upravljanje pristupom i praćenje sigurnosnih događaja.",
    "Koje su prednosti i izazovi Internet stvari?": "Prednosti IoT-a uključuju poboljšanu učinkovitost, automatizaciju, udobnost i praćenje podataka. Međutim, izazovi uključuju sigurnosne rizike, privatnost podataka, interoperabilnost i skalabilnost mreže.",
    "Kako se IoT primjenjuje u zdravstvu?": "IoT se primjenjuje u zdravstvu za praćenje pacijenata, upravljanje medicinskim inventarom, pametne uređaje za praćenje zdravlja i poboljšanje kvalitete zdravstvene skrbi.",
    "Koje su mogućnosti povezivanja vozila putem IoT-a?": "Povezivanje vozila putem IoT-a omogućuje praćenje voznog parka, upravljanje prometom, poboljšanje sigurnosti na cestama i pružanje dodatnih usluga vozačima.",
    "Kako IoT može poboljšati kvalitetu života u domovima?" : "IoT omogućuje pametno upravljanje rasvjetom, termostatom, kućanskim aparatima i sigurnosnim sustavima, čime se povećava udobnost i energetska učinkovitost u domovima.",
    "Kako se IoT primjenjuje u poljoprivredi?" : "IoT se primjenjuje u poljoprivredi za nadzor poljoprivrednih usjeva, automatsko navodnjavanje, praćenje kvalitete tla i optimizaciju rasta biljaka.",
    "Koje su primjene Internet stvari u sektoru transporta i logistike?" : "IoT se koristi u sektoru transporta i logistike za praćenje tereta, upravljanje voznim parkom, optimizaciju rute i poboljšanje isporuke robe.",
    "Kako se IoT primjenjuje u pametnim kućama?" : "IoT se koristi u pametnim kućama za kontrolu rasvjete, grijanja, hlađenja, sigurnosnih sustava i kućanskih aparata putem pametnih uređaja.",
    "Koje su mogućnosti IoT-a u industriji zabave?" : "IoT se može koristiti u industriji zabave za stvaranje personaliziranih doživljaja, praćenje korisničkih preferencija, upravljanje pametnim uređajima i poboljšanje interakcije s publikom.",
    "Kako IoT može unaprijediti održivost i zaštitu okoliša?" : "IoT može pomoći u praćenju potrošnje energije, upravljanju otpadom, praćenju kvalitete zraka i vode te promicanju održivih praksi za zaštitu okoliša.",
    "Kako se IoT primjenjuje u sektoru pametne energije?" : "IoT se koristi u sektoru pametne energije za nadzor potrošnje energije, upravljanje mrežom, optimizaciju distribucije energije i integraciju obnovljivih izvora energije.",
    "Koje su potencijalne prijetnje sigurnosti u IoT mreži?" : "Potencijalne prijetnje sigurnosti u IoT mreži uključuju hakiranje uređaja, krađu podataka, napade uskraćivanja usluge (DDoS) i zloupotrebu privatnosti korisnika.",
    "Kako se IoT primjenjuje u sektoru pametnih gradova?" : "IoT se koristi u sektoru pametnih gradova za upravljanje prometom, praćenje kvalitete zraka, pametno osvjetljenje, upravljanje otpadom i poboljšanje javnih usluga.",
    "Koje su mogućnosti IoT-a u sektoru e-zdravstva?" : "IoT pruža mogućnosti za praćenje vitalnih znakova, udaljeno savjetovanje, praćenje kroničnih bolesti i poboljšanje brige o pacijentima u e-zdravstvu.",
    "Koje su etičke i privatnosne brige vezane uz IoT?" : "Etičke i privatnosne brige vezane uz IoT uključuju prikupljanje i korištenje osobnih podataka, praćenje korisnika bez njihovog znanja i potencijalnu zloupotrebu informacija.",
    "Kako se IoT primjenjuje u sektoru proizvodnje?" : "IoT se koristi u sektoru proizvodnje za praćenje proizvodnih procesa, upravljanje zalihama, održavanje strojeva i optimizaciju proizvodne učinkovitosti.",
    "Koje su mogućnosti IoT-a u sektoru pametnih trgovina?" : "IoT pruža mogućnosti za praćenje zaliha, personalizirane marketinške kampanje, poboljšanje korisničkog iskustva i automatizaciju plaćanja u pametnim trgovinama.",
    "Koje su primjene Internet stvari u sektoru financija?" : "IoT se koristi u sektoru financija za praćenje imovine, sigurno plaćanje, prevenciju prijevara i poboljšanje korisničkog iskustva u bankarstvu.",
    "Kako IoT može poboljšati sigurnost u domovima?" : "IoT omogućuje nadzor sigurnosnih kamera, senzora za dim i pokreta, daljinsko zaključavanje vrata i upozorenja u stvarnom vremenu za poboljšanu sigurnost domova.",
    "Koje su izazovi vezani uz interoperabilnost u IoT mreži?" : "Izazovi interoperabilnosti u IoT mreži uključuju različite standarde, protokole i komunikacijske tehnologije koje moraju biti usklađene radi uspješne komunikacije između uređaja.",
    "Kako se IoT primjenjuje u sektoru turizma i gostoprimstva?" : "IoT se koristi u sektoru turizma i gostoprimstva za personalizirane usluge gostima, upravljanje hotelskim objektima, pametne sustave za sobe i poboljšanje korisničkog iskustva.",
    "Koje su mogućnosti IoT-a u sektoru sportske industrije?" : "IoT pruža mogućnosti za praćenje sportskih performansi, analizu podataka o treningu, poboljšanje sigurnosti sportaša i poboljšanje iskustva gledatelja.",
    "Kako se IoT primjenjuje u sektoru automobila i povezane mobilnosti?" : "IoT se koristi u sektoru automobila i povezane mobilnosti za praćenje vozila, upravljanje prometom, poboljšanje sigurnosti na cestama i pružanje pametnih usluga u vozilima.",
    "Koje su perspektive razvoja IoT-a u budućnosti?" : "Perspektive razvoja IoT-a uključuju sve veći broj povezanih uređaja, napredak u umjetnoj inteligenciji, razvoj 5G mreže i širenje IoT primjena u različitim sektorima.",
    # Add more questions and answers as needed
}

# Function to preprocess user input
def preprocess_input(input_text):
    # Tokenize the input text
    tokens = word_tokenize(input_text.lower())
    
    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Return the preprocessed tokens as a string
    return ' '.join(filtered_tokens)

# Function to find the best match in the knowledge base
def find_best_match(question):
    # Preprocess the input question
    preprocessed_question = preprocess_input(question)
    
    # Initialize variables for best match
    best_match = None
    best_score = 0
    
    # Iterate over the knowledge base
    for q, a in knowledge_base.items():
        # Preprocess each question in the knowledge base
        preprocessed_q = preprocess_input(q)
        
        # Calculate similarity score using a simple word overlap approach
        score = len(set(preprocessed_question.split()) & set(preprocessed_q.split()))
        
        # Update best match if the current score is higher
        if score > best_score:
            best_score = score
            best_match = a
    
    return best_match

# Main loop for the bot
while True:
    # Get user input
    question = input("Ask me a question: ")
    
    # Check for exit condition
    if question.lower() == "exit":
        break
    
    # Find the best match in the knowledge base
    answer = find_best_match(question)
    
    # Print the answer
    if answer:
        wrapped_lines = textwrap.wrap(answer, width=80)  # Adjust the width as needed
        for i, line in enumerate(wrapped_lines):
            if i == 0:
                print("Mirko:", line)
            else:
                print("      ",line)
    else:
        print("Bot: Sorry, I don't have an answer to that question.")
      print("      ",line)
    else:
        print("Bot: Sorry, I don't have an answer to that question.")
