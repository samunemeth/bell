## Ez az ág a Péterfy egyedi server konfigurációjára van szabva!

## Leírás

Iskolai be- és kicsengő hangjainak pontos lejátszására. Továbbá hangosbemondások kicsengetés előtti bejátszására.

## Használat

A `paths.yaml` fileban megadott helyekre el kell helyezni a szükséges fileokat, illetve létre kell hozni a bemondásokat tároló mappákat. Ezen helyek tetszés szerint személyre szabhatók.

Az `events.yaml` file tartalmazza a csengetési illetve bemondási rendet a fileban megadott minta szerinti kulcsszavak használatával.

A `.yaml` fileok szintaxisa [itt](https://spacelift.io/blog/yaml) jól össze van foglalva.

<!-- Instructions for the .env file -->

## Tennivalók

- [ ] `.wav` hangformátum elfogadása
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
sudo apt install ffmpeg python3-full
python -m venv ./venv
./venv/bin/pip3 install -r requirements.txt
```

Ha így nem sikerül a telepítés, érdemese megprómálni a `requirements.txt` fileban szerereplő csomagokat egyeséve, **sorban** telepíteni a `pip3 install [name]` paranccsal.