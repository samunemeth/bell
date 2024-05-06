## Ez a project fejlesztés alatt áll!

Egyenlőre nem játszik le hangokat, csak a log-ba jegyzi fel hogy megtörténet az esemény.

## Leírás

Iskolai be- és kicsengő hangjainak pontos lejátszására. Továbbá hangosbemondások kicsengetés előtti bejátszására.

## Tennivalók

- [x] Konfigurációs fileok beolvasáskor való ellenőrzése.
- [x] Környezeti változó a logging-level -hez.
- [ ] A hangosbemondások implementálása
- [ ] ffplay a hangok lejátszásához.
- [ ] Élő hangátvitel.

## Csomagok telepítése

### Windows

Windowson az ffmpeg-et külön kell telepíteni.

```sh
python -m venv ./venv
.\venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 main.py
```

### Linux

```sh
sudo apt install ffmpeg
python -m venv ./venv
./venv/bin/pip3 install -r requirements.txt
```

Ha így nem sikerül a telepítés, érdemese megprómálni a `requirements.txt` fileban szerereplő csomagokat egyeséve, **sorban** telepíteni a `pip3 install [name]` paranccsal.