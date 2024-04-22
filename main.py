import logging
import yaml
from time import sleep
import schedule

# A logger beállítása. Érdemes így hagyni. Ha túl sok az kimenet, a "level" változót lehet változtatni.
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level = logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
logging.info(f"Konfigurációk betöltése megkezdődött...")

# File helyek importálása. A paths.yaml file ezzel a scriptel egyhelyen kell hogy legyen!
paths: dict[str] = []
with open("paths.yaml") as paths_file:
    paths = yaml.safe_load(paths_file)
logging.info(f"File helyek: {paths}")

# Időpontok importálása egy könyvtárba.
events: dict[str, str] = []
with open(paths["events"]) as events_file:
    events = yaml.safe_load(events_file)
logging.info(f"Események: {events}")

# Funkció a különböző típusú események felismerésére és a megfelelő feladat futtatására.
def run_event(event_type: str) -> None:
    match event_type:
        case "becsengo":
            logging.info(f"Becsengő sikeresen futtatva.")
            pass

        case "kicsengo":
            logging.info(f"Kicsengő sikeresen futtatva.")
            pass

        case "hirdetes":
            logging.info(f"Hirdetés sikeresen futtatva.")
            pass

        case _:
            logging.warning(f"A bemeneti file nem megfelelően van formázva!, \"{event_type}\" esemény nem létezik.")

# A konfigurációs fileban megadott események beisőzítése HÉTKÖZNAPOKRA.
# Szombati munkanap? Iskola vége után?
logging.info(f"Események időzítése...")
for event in events:
    event_time = event["time"]
    event_type = event["type"]
    schedule.every().monday.at(event_time).do(run_event, event_type)
    schedule.every().tuesday.at(event_time).do(run_event, event_type)
    schedule.every().wednesday.at(event_time).do(run_event, event_type)
    schedule.every().thursday.at(event_time).do(run_event, event_type)
    schedule.every().friday.at(event_time).do(run_event, event_type)

logging.info(f"Inicializáció sikeres!")
        
# A beidőzített események végrehajtása.
logging.info(f"Várakozás az eseményekre...")
while True:
    schedule.run_pending()
    sleep(1)