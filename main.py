import os
import logging
from time import sleep
import re
import subprocess

# Külső könyvtárak
import yaml
import schedule
from dotenv import load_dotenv

# Konstansok
POSSIBLE_EVENTS = ["becsengo", "kicsengo", "hirdetes"]

# Környezeti változók betöltése
load_dotenv()
RUNNING_PATH = os.environ.get("RUNNING_PATH", default="./")
LOGGING_LEVEL = int(os.environ.get("LOGGING_LEVEL", default="20"))

# A logger beállítása. Érdemes így hagyni. Ha túl sok az kimenet, a "level" változót lehet változtatni.
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level = LOGGING_LEVEL, datefmt='%Y-%m-%d %H:%M:%S')

# Logging
logging.info("Konfigurációk betöltése...")

# File helyek importálása. A paths.yaml file ezzel a scriptel egyhelyen kell hogy legyen!
paths: dict[str] = []
with open(RUNNING_PATH + "paths.yaml") as paths_file:
    paths = yaml.safe_load(paths_file)

# Ellenőrzés hogy léteznek-e a megadott fileok illetve mappák.
for path_name, path in paths.items():
    if not os.path.exists(path):
        logging.error("A '%s' kulcshoz megadott '%s' file vagy mappa nem létezik!", path_name, path)
logging.debug("File helyek: %s", paths)

# Időpontok importálása egy könyvtárba.
events: dict[str, str] = []
with open(paths["events"]) as events_file:
    events = yaml.safe_load(events_file)

# Az időpontok és eseménytípusok ellenőrzése.
for event in events:
    if not re.match(r"[0-2]\d:[0-5]\d", event["time"]):
        logging.error("A '%s' eseményhez megadott '%s' időpont formázása helytelen. Helyes formátum: HH:MM", event["type"], event["time"])
    if event["type"] not in POSSIBLE_EVENTS:
        logging.error("A '%s' időponthoz rendelt '%s' esemény nem létezik! Lehetséges opciók: '%s'", event["time"], event["type"], POSSIBLE_EVENTS)
logging.debug("Események: %s", events)

# Funkció a különböző típusú események felismerésére és a megfelelő feladat futtatására.
def run_event(event_type: str) -> None:
    match event_type:
        case "becsengo":
            logging.info("Becsengő lejátszása...")
            try:
                subprocess.run("ffplay -v 0 -nodisp -autoexit " + paths["sounds-in"])
            except Exception:
                logging.warning("Becsengő sikertelen!")
            else:
                logging.debug("Becsengő lejátszva.")
            return

        case "kicsengo":
            logging.info("Kicsengő lejátszása...")
            try:
                subprocess.run("ffplay -v 0 -nodisp -autoexit " + paths["sounds-out"])
            except Exception :
                logging.warning("Kicsengő sikertelen!")
            else:
                logging.debug("Kicsengő lejátszva.")
            return

        case "hirdetes":
            logging.error("Fejlesztés alatt!")
            return

            logging.debug("Hirdetés keresése...")
            possible_files = os.listdir(paths["announcements-new"])
            possible_announcements = [e for e in possible_files if re.match(r".*\.mp3", e)]
            if not possible_announcements:
                logging.info("Nincs hirdetés!")
                return
            announcement_name = possible_announcements[0]
            # TODO: Play chime before announcement
            logging.info("A '%s' nevű hirdetés lejátszása...", announcement_name)
            subprocess.run("ffplay -v 0 -nodisp -autoexit " + paths["announcements-new"] + announcement_name)
            os.rename(paths["announcements-new"] + announcement_name, paths["announcements-old"] + announcement_name)
            logging.debug("Hirdetés lejátszva.")
            return

        case _:
            logging.warning("A bemeneti file nem megfelelően van formázva!, '%s' esemény nem létezik.", event_type)
            return

# A konfigurációs fileban megadott események beidőzítése hétköznapokra.
logging.info("Események időzítése...")
for event in events:
    schedule.every().monday.at(event["time"]).do(run_event, event["type"])
    schedule.every().tuesday.at(event["time"]).do(run_event, event["type"])
    schedule.every().wednesday.at(event["time"]).do(run_event, event["type"])
    schedule.every().thursday.at(event["time"]).do(run_event, event["type"])
    schedule.every().friday.at(event["time"]).do(run_event, event["type"])

# Logging
logging.info("Inicializáció sikeres!")

# A beidőzített események végrehajtása.
logging.info("Várakozás az eseményekre...")
while True:
    schedule.run_pending()
    sleep(1)
