# AI Interior Design Configurator

## Opis projektu

Projekt łączy modelowanie 3D w Blenderze z technologią sztucznej inteligencji, tworząc interaktywny konfigurator wnętrz. System umożliwia dynamiczną zmianę parametrów pomieszczenia poprzez panel sterowania oparty na presetach wygenerowanych przez AI.

---

## Cel projektu

### Dla przedmiotu: Modelowanie 3D
- Stworzenie modelu pomieszczenia w Blenderze
- Modelowanie mebli i elementów wyposażenia
- Przygotowanie materiałów i oświetlenia
- Renderowanie sceny w różnych konfiguracjach

### Dla przedmiotu: Sztuczna Inteligencja
- Wykorzystanie AI do generowania koncepcji designu
- Implementacja systemu parametrycznego sterowanego przez AI
- Automatyzacja procesu projektowania wnętrz
- Integracja AI z narzędziami 3D poprzez Python

---

## Technologie

| Technologia | Wersja | Zastosowanie |
|-------------|--------|--------------|
| **Blender** | 3.x+ | Modelowanie 3D, renderowanie, środowisko wykonawcze |
| **Python** | 3.x | Automatyzacja, logika systemu, UI |
| **JSON** | - | Przechowywanie konfiguracji i presetów |
| **Blender Python API** | bpy | Manipulacja sceną 3D |
| **AI (Konceptualne)** | - | Generowanie stylów i parametrów designu |

### Wykorzystane biblioteki Python:
- `bpy` - Blender Python API
- `json` - parsowanie plików konfiguracyjnych
- `os` - operacje na plikach
- `random` - generator losowych designów

---

## Architektura projektu

```
AI-Interior-Configurator/
│
├── Untitled.blend         # Plik Blender z modelem pokoju ✅
├── designs.json           # Presety designów (5 stylów AI) ✅
├── ai_panel.py           # Główny skrypt Python ✅
├── ai_panel_simple.py    # Uproszczona wersja (zalecana) ✅
├── README.md             # Raport projektu (PL) ✅
├── INSTRUKCJA.md         # Instrukcja użytkowania (PL) ✅
├── .gitignore            # Konfiguracja Git ✅
└── screenshots/          # Zrzuty ekranu (do utworzenia)
```

---

## Proces tworzenia

### Etap 1: Modelowanie w Blenderze ✅

**Status:** Ukończony

Utworzono model pokoju zawierający:
- **Ściany** - podstawowa konstrukcja pomieszczenia z oknami
- **Podłoga** - płaszczyzna bazowa
- **Zasłony** - dekoracyjne zasłony przy oknach
- **Meble:**
  - Sofa - kanapa w pokoju
  - Dywan (Carpet) - element dekoracyjny
- **Oświetlenie:**
  - Lampa - źródło światła

**Nazewnictwo obiektów w Outliner:**
```
Scene
├── Walls ✅
├── FloorPlates ✅
├── FloorUnder ✅
├── Sofa ✅
├── Lamp ✅
├── Carpet ✅
├── Zaslona1 ✅
├── Zaslona2 ✅
└── Camera ✅
```

**Uwaga:** System automatycznie zmienia kolory WSZYSTKICH obiektów przy wyborze stylu. Nie trzeba ręcznie zmieniać nazw - skrypt obsługuje istniejące nazwy!

### Statystyka modelu:
- **Liczba obiektów:** 8 (ściany, podłoga, meble, dekoracje)
- **Obiekty sterowane przez AI:** 7 (wszystkie oprócz kamery)
- **Materiały:** 7 (każdy obiekt ma dedykowany materiał)
- **Oświetlenie:** 1 lampa z dynamiczną kontrolą

---

### Etap 2: Konfiguracja AI ✅

**Status:** Ukończony

Wykorzystanie AI do wygenerowania różnych stylów wnętrza:

1. **Minimalist** - styl minimalistyczny
   - Jasne, neutralne kolory
   - Proste formy
   - Maksymalna funkcjonalność

2. **Cozy** - styl przytulny
   - Ciepłe kolory (brązy, beże, pomarańcze)
   - Miękkie oświetlenie
   - Atmosfera domowa

3. **Futuristic** - styl futurystyczny
   - Chłodne kolory (niebieski, szary)
   - Mocne kontrasty
   - Nowoczesne formy

---

### Etap 3: Implementacja Python ✅

**Status:** Ukończony

**Funkcjonalność:**

✅ **Automatyczna zmiana kolorów** - wszystkie obiekty w pokoju:
   - Ściany (Walls)
   - Podłoga (FloorPlates, FloorUnder)
   - Sofa
   - Dywan (Carpet)
   - Zasłony (Zaslona1, Zaslona2)

✅ **Przełączanie układów mebli** - 3 różne layouty (A, B, C)

✅ **Sterowanie oświetleniem** - włączanie/wyłączanie lampy

✅ **Generator losowego designu** - losowa kombinacja stylu i layoutu

✅ **Losowe kolory indywidualne** - możliwość losowania koloru dla każdego obiektu osobno

✅ **Panel UI w Blenderze** - intuicyjny interfejs sterowania

---

## Rola AI w projekcie

### Generowanie koncepcji
AI został wykorzystany do:
- Stworzenia koncepcji trzech różnych stylów wnętrza
- Wygenerowania palet kolorystycznych
- Określenia parametrów oświetlenia dla każdego stylu
- Zaproponowania układów mebli
- napisanie scryptu python

### Parametryzacja designu
Każdy styl zawiera precyzyjne parametry dla WSZYSTKICH obiektów w pokoju:

**Kolory:**
- Ściany (Walls)
- Podłoga (Floor, FloorPlates, FloorUnder)
- Sofa
- Dywan (Carpet)
- Zasłony (Zaslona1, Zaslona2)

**Oświetlenie:**
- Intensywność światła
- Kolor światła
- Temperatura barwowa


---

## Instalacja i uruchomienie

### Wymagania
- **Blender 3.0+** (testowano na Blender 3.x)
- **Python 3.x** (wbudowany w Blender)
- **System operacyjny:** Windows 10/11

### Jak uruchomić (krok po kroku)

#### Metoda 1: Dla nowych użytkowników (zalecana)

1. **Otwórz plik Blender** z modelem pokoju

2. **Załaduj skrypt:**
   - Przejdź do zakładki **Scripting**
   - Kliknij **Open** (ikona folderu)
   - Wybierz plik **`ai_panel_simple.py`** ← to jest uproszczona wersja!
   - Kliknij **Run Script** (▶️) lub naciśnij **Alt + P**

3. **Otwórz panel sterowania:**
   - Wróć do zakładki **Layout**
   - W widoku 3D naciśnij klawisz **N**
   - Znajdź zakładkę **"AI Design"**
   - Gotowe! 🎉

4. **Testuj funkcje:**
   - Kliknij dowolny styl (np. "Minimalist")
   - Obserwuj jak zmienia się scena

#### Metoda 2: Klonowanie z GitHub

```bash
git clone https://github.com/[username]/AI-Interior-Configurator.git
cd AI-Interior-Configurator
```

Następnie wykonaj kroki z Metody 1.

---

## Analiza projektu

### Zalety wykorzystania AI ✅
- **Szybkość generowania wariantów** - AI wygenerował 5 kompletnych stylów w ciągu sekund
- **Spójność stylistyczna** - każdy styl ma harmonijnie dobrane kolory i parametry
- **Automatyzacja** - zmiana całego wnętrza jednym kliknięciem
- **Parametryzacja** - łatwe modyfikowanie i dodawanie nowych stylów
- **Eksperymentowanie** - funkcja losowych kolorów pozwala na kreatywne kombinacje
- **Skalowalność** - system można łatwo rozszerzyć o nowe obiekty

### Ograniczenia ⚠️
- AI generuje **parametry**, ale nie tworzy geometrii 3D automatycznie
- Wymaga ręcznego modelowania podstawowej sceny
- Presety są statyczne (zapisane w JSON, nie generowane na żywo)
- Brak uczenia maszynowego - system oparty na predefiniowanych regułach
- Zależność od struktury sceny (wymaga określonych nazw obiektów)

### Wyzwania techniczne podczas implementacji
- **Problem z ścieżkami plików** w Windows (cyrylica w nazwach folderów)
- **Integracja Python → Blender** wymagała dokładnej znajomości Blender API
- **Zarządzanie materiałami** - system węzłów (nodes) w Blenderze jest złożony
- **Kompatybilność** - kod musi działać na różnych wersjach Blendera

### Rozwiązania zastosowane w projekcie
✅ Stworzenie **dwóch wersji skryptu** (standardowa i uproszczona)  
✅ **Fallback mechanizm** dla wczytywania plików  
✅ **Szczegółowe komunikaty diagnostyczne** w konsoli  
✅ **Obsługa błędów** - skrypt informuje o brakujących obiektach  
✅ **Dokumentacja** - szczegółowa instrukcja w języku polskim

### Możliwości rozwoju 🚀

**Krótkoterminowe (możliwe do dodania w projekcie):**
- 📸 Automatyczne renderowanie wszystkich stylów
- 🎨 Większa paleta kolorów (10+ wariantów na styl)
- 📐 Więcej layoutów (5-7 różnych układów)
- 🪑 Dodanie więcej mebli (krzesła, stół, półki)
- 💾 Zapisywanie ulubionych konfiguracji

**Długoterminowe (rozwinięcie projektu):**
- 🤖 Integracja z rzeczywistym API AI (GPT-4, Midjourney)
- 🖼️ Generowanie tekstur przez AI (Stable Diffusion)
- 🏗️ Automatyczne tworzenie geometrii przez AI
- 🎮 Eksport do Unreal Engine / Unity
- 🥽 Podgląd w VR/AR
- 🌐 Aplikacja webowa (Three.js + React)
- 📊 Uczenie maszynowe - system uczący się z preferencji użytkownika

---

## Podsumowanie

Projekt **AI Interior Design Configurator** skutecznie łączy modelowanie 3D w Blenderze z technologiami sztucznej inteligencji. System umożliwia automatyczne zmiany parametrów wizualnych pomieszczenia na podstawie presetów wygenerowanych przez AI.

### Rezultaty projektu:
- ✅ **Funkcjonalny konfigurator** z 5 stylami AI
- ✅ **Intuicyjny interfejs** użytkownika w Blenderze
- ✅ **Kompletna dokumentacja** w języku polskim (2 pliki markdown)
- ✅ **Kod źródłowy** z komentarzami (450+ linii)
- ✅ **System gotowy do prezentacji** i dalszego rozwoju

### Statystyka projektu:

| Metryka | Wartość |
|---------|---------|
| Linie kodu Python | ~450 |
| Pliki projektu | 7 |
| Style AI | 5 |
| Layouty mebli | 3 |
| Sterowane obiekty | 7 |
| Parametry na styl | 10+ |
| Całkowite kombinacje | 15+ (style × layouty) |
| Czas realizacji | 2 dni |

### Zastosowanie praktyczne:
Tego typu systemy znajdują zastosowanie w:
- 🏠 Projektowaniu wnętrz
- 🏗️ Architekturze wizualizacyjnej
- 🎮 Tworzeniu gier (proceduralne generowanie lokacji)
- 🛋️ E-commerce (konfigurator mebli)
- 🎓 Edukacji (nauka AI i modelowania 3D)

---
---

## FAQ - Najczęstsze pytania

**Q: Czy mogę dodać własne style?**  
A: Tak! Edytuj plik `designs.json` i dodaj nowy preset z własnymi kolorami.

**Q: Czy projekt wymaga połączenia z internetem?**  
A: Nie. Wszystko działa lokalnie w Blenderze.

**Q: Czy można użyć tego w innych scenach?**  
A: Tak, ale wymagane jest dostosowanie nazw obiektów do formatu skryptu.

**Q: Jak dodać więcej obiektów do sterowania?**  
A: Dodaj nazwę obiektu w funkcji `set_material_color()` oraz w sekcji "Aplikuj kolory" operatora.

---

## Licencja

Projekt edukacyjny - wolne użycie na potrzeby nauki i rozwoju.
