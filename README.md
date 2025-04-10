# Evidence vozidel
![obrazek](https://github.com/user-attachments/assets/310210b2-825b-4b31-99c1-ebdebe050aa9)


Tento projekt je vytvořen pomocí Python frameworku **Django** a slouží k evidenci vozidel a jejich servisních záznamů.

## Funkce

- Přehled vozidel
- Záznam STK, dálniční známky, pojištění
- Servisní úkony (např. výměna oleje)
- Možnost přidávat, upravovat a mazat údaje

## Požadavky

- Python 3.10+
- Django 4+

## Instalace

```bash
git clone https://github.com/Wolferine69/evidence_vozidel.git
cd evidence_vozidel
python -m venv .venv
.venv\Scripts\activate  # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Použití

Po spuštění přejdi na `http://127.0.0.1:8000` a začni evidovat vozidla.

---

🛠️ Projekt je ve vývoji – další funkce budou přidávány průběžně.
