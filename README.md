![fbref_logo](https://github.com/GabrielPastorello/FRScraper/assets/57769272/2c097739-f0af-4cb2-8c6e-eafc9d2fdf3e)<p align="center">
</p>
<p align="center">
    <a href="https://pypi.org/project/FRScraper/">
        <img src="https://img.shields.io/pypi/v/FRScraper" alt="pypi" />
    </a>
    <a href="https://pypi.org/project/FRScraper/">
        <img src="https://img.shields.io/pypi/pyversions/FRScraper" alt="python version" />
    </a>
    <a href="https://pypi.org/project/FRScraper/">
        <img src="https://img.shields.io/pypi/l/FRScraper" alt="license" />
    </a>
</p>

# ⚽ FRScraper

Python package for easy access to football data through scraping of [Football Reference](https://fbref.com/en/) website.

This allows users to obtain statistics, standings, and scores of the following tournaments:
- **Premier League** (England)
- **La Liga** (Spain)
- **Bundesliga** (Germany)
- **Ligue 1** (France)
- **Serie A** (Italy)
- **Eredivisie** (Netherlands)
- **Liga Portuguesa** (Portugal)
- **Campeonato Brasileiro** (Brazil)
- **Primera División Argentina** (Argentina)
- **Ekstraklasa** (Poland)
- **Russian Premier League** (Russia)
- **Saudi Pro League** (Saudi Arabia)

## 🚀 Installing
### Via `pip`
Install with the following command:

```
pip install FRScraper
```

## 📖 Documentation
For documentation about the API methods refer to [the documentation](https://github.com/GabrielPastorello/FRScraper/blob/main/API.md).

## 🔌 Example of use
```
import FRScraper
```

```
# League table
df = FRScraper.get_rankings('ENG').head()
```
Output:
|    | Rk | Squad           | MP | W  | D  | L  | ... | xGD  | xGD/90 | Attendance | Top Scorer Goals  |
| -- | -- | --------------- | -- | -- | -- | -- | --- | ---- | ------ | ---------- | ----------------- |
| 0  | 1  | Manchester City | 38 | 28 | 7  | 3  | ... | 44.9 | 1.18   | 50112      | 27                |
| 1  | 2  | Arsenal         | 38 | 28 | 5  | 5  | ... | 48.2 | 1.27   | 60236      | 16                |
| 2  | 3  | Liverpool       | 38 | 24 | 10 | 4  | ... | 42.0 | 1.11   | 55979      | 18                |
| 3  | 4  | Aston Villa     | 38 | 20 | 8  | 10 | ... | 3.4  | 0.09   | 41858      | 19                |
| 4  | 5  | Tottenham       | 38 | 20 | 6  | 12 | ... | 4.8  | 0.13   | 61482      | 17                |

More examples in the files.

Use it wisely!
