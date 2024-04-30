import logging
import yaml
from time import sleep
import schedule
import playsound

# A logger beállítása. Érdemes így hagyni. Ha túl sok az kimenet, a "level" változót lehet változtatni.
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level = logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

# Logging
logging.info("Konfigurációk betöltése...")

# File helyek importálása. A paths.yaml file ezzel a scriptel egyhelyen kell hogy legyen!
paths: dict[str] = []
with open("paths.yaml") as paths_file:
    paths = yaml.safe_load(paths_file)
logging.info("File helyek: " + str(paths))

# Időpontok importálása egy könyvtárba.
events: dict[str, str] = []
with open(paths["events"]) as events_file:
    events = yaml.safe_load(events_file)
logging.info("Események: " + str(events))

# Funkció a különböző típusú események felismerésére és a megfelelő feladat futtatására.
def run_event(event_type: str) -> None:
    match event_type:
        case "becsengo":
            logging.info("Becsengő lejátszása...")
            try:
                playsound.playsound(paths["sounds"]["in"])
            except playsound.PlaysoundException:
                logging.warning("Becsengő sikertelen! A \"" + str(paths["sounds"]["in"]) + "\" file nem található.")
            else:
                logging.info("Becsengő lejátszva.")

        case "kicsengo":
            logging.info("Kicsengő lejátszása...")
            try:
                playsound.playsound(paths["sounds"]["out"])
            except playsound.PlaysoundException:
                logging.warning("Kicsengő sikertelen! A \"" + str(paths["sounds"]["out"]) + "\" file nem található.")
            else:
                logging.info("Kicsengő lejátszva.")

        case "hirdetes":
            logging.info("Hirdetés sikeresen futtatva.")

        case _:
            logging.warning("A bemeneti file nem megfelelően van formázva!, \"" + str(event_type) + "\" esemény nem létezik.")

# A konfigurációs fileban megadott események beisőzítése hétköznapokra.
logging.info("Események időzítése...")
for event in events:
    event_time = event["time"]
    event_type = event["type"]
    schedule.every().monday.at(event_time).do(run_event, event_type)
    schedule.every().tuesday.at(event_time).do(run_event, event_type)
    schedule.every().wednesday.at(event_time).do(run_event, event_type)
    schedule.every().thursday.at(event_time).do(run_event, event_type)
    schedule.every().friday.at(event_time).do(run_event, event_type)

# Logging
logging.info("Inicializáció sikeres!")
        
# A beidőzített események végrehajtása.
logging.info("Várakozás az eseményekre...")
while True:
    schedule.run_pending()
    sleep(1)