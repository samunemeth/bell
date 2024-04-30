## Ez a project fejlesztés alatt áll!

Egyenlőre nem játszik le hangokat, csak a log-ba jegyzi fel hogy megtörténet az esemény.

## Leírás

Iskolai be- és kicsengő hangjainak pontos lejátszására. Továbbá hangosbemondások kicsengetés előtti bejátszására.

## Csomagok telepítése

### Windows

```sh
python -m venv ./venv
.\venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 main.py
```

### Linux

```sh
python -m venv ./venv
./venv/bin/pip3 install -r requirements.txt
```

Ha így nem sikerül a telepítés, érdemese megprómálni a `requirements.txt` fileban szerereplő csomagokat egyeséve, **sorban** telepíteni a `pip3 install [name]` paranccsal.