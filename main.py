import logging
import yaml
from time import sleep
import schedule
import playsound
from os.path import exists as file_exists

# A logger beállítása. Érdemes így hagyni. Ha túl sok az kimenet, a "level" változót lehet változtatni.
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level = logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

# Logging
logging.info("Konfigurációk betöltése...")

# File helyek importálása. A paths.yaml file ezzel a scriptel egyhelyen kell hogy legyen!
paths: dict[str] = []
with open("paths.yaml") as paths_file:
    paths = yaml.safe_load(paths_file)

# Ellenőrzés hogy léteznek-e a megadott fileok illetve mappák.
for path_name, path in paths.items():
    if not file_exists(path):
        logging.error("A '%s' kulcshoz megadott '%s' file vagy mappa nem létezik!", path_name, path)
logging.debug("File helyek: %s", paths)

# Időpontok importálása egy könyvtárba.
events: dict[str, str] = []
with open(paths["events"]) as events_file:
    events = yaml.safe_load(events_file)
logging.debug("Események: %s", events)

# Funkció a különböző típusú események felismerésére és a megfelelő feladat futtatására.
def run_event(event_type: str) -> None:
    match event_type:
        case "becsengo":
            logging.info("Becsengő lejátszása...")
            try:
                # playsound.playsound(paths["sounds-in"])
                pass
            except playsound.PlaysoundException:
                logging.warning("Becsengő sikertelen! A '%s' file nem található.", paths["sounds-in"])
            else:
                logging.debug("Becsengő lejátszva.")

        case "kicsengo":
            logging.info("Kicsengő lejátszása...")
            try:
                # playsound.playsound(paths["sounds-out"])
                pass
            except playsound.PlaysoundException:
                logging.warning("Kicsengő sikertelen! A '%s' file nem található.", paths["sounds-out"])
            else:
                logging.debug("Kicsengő lejátszva.")

        case "hirdetes":
            logging.info("Hirdetés sikeresen futtatva.")

        case _:
            logging.warning("A bemeneti file nem megfelelően van formázva!, '%s' esemény nem létezik.", event_type)

# A konfigurációs fileban megadott események beidőzítése hétköznapokra.
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
