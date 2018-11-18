## Instrukcja przygotowania środowiska do warsztatów

1. Pobierz i zainstaluj środowisko Anacondy dla odpowiedniego systemu (wersja z python 3):
https://www.anaconda.com/download/

2. Uruchom środowisko Anacondy - dla Windows otwórz konsolę Anaconda Prompt
https://docs.anaconda.com/anaconda/user-guide/getting-started

3. Pobierz repozytorium z materiałami do ćwiczeń:
``` git clone https://github.com/JoannaMisztalRadecka/nlp_workshops.git ```

4. Zainstaluj dodatkowe pakiety używane podczas warsztatów:
```pip install -r requirements.txt```

5. Uruchom skrypt do pobrania dodatkowych zasobów językowych potrzebnych podczas warsztatów (uwaga: jeden z modeli użyty w przykładzie ma ponad 900MB, można go pobrać opcjonalnie - należy odkomentować linijkę w skrypcie)
```python ./download_lang_resources.py```

6. Pobierz dane z platformy Kaggle (wymaga rejestracji i zaakceptowania warunków serwisu):
- https://www.kaggle.com/snapcrack/all-the-news/downloads/articles1.csv/4
- https://www.kaggle.com/goweiting/ted-talks-transcript#ted_metadata_kaggle.csv
- https://www.kaggle.com/kemical/kickstarter-projects

7. Z konsoli Anacondy uruchom Jupyter Notebook i otwórz folder notebooks z repozytorium z interfejsu w przeglądarce
```jupyter notebook```