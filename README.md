# Generátor obsahu pro snowfall šablonu iROZHLAS.cz

> Já jsem šablona, co generuje střeva pro snowfall články.

## Předpoklady
Je třeba [Python 3](https://www.python.org/downloads/) a nainstalované (`pip install KNIHOVNA`) knihovny:
markdown
jsmin
ast
csscompressor

## Nový článek

Jelikož si každý projekt nese dost "svého" bince, je vhodné pro každý článek založit separátní repozitář. Je tedy nutné si stáhnout (nebo naklonovat) šablonu a nastavit jí gitový *remote* na nový repozitář.

- Naklonujeme repo do nového adresáře

```bash
git clone git@bitbucket.org:samizdatcz/snowfall-builder.git jmeno-projektu
```

- Odstraníme současný remote (vedoucí na šablonu)

```bash
git remote remove origin
```

- Vytvoříme pro projekt nové repo. `smzd create` sám rovnou nastaví správný nový remote

```bash
smzd add jmeno-projektu
```

- To je celé! Teď už se můžeme vrhnout na psaní článku.

## Psaní článku
Celý neinteraktivní obsah se nastavuje v souboru `article.md`. Skládá se, podobně [Jekyll](https://jekyllrb.com/docs/frontmatter/), ze dvou částí: hlavičky a obsahu.

### Hlavička
Hlavička je uvozena a ukončena třemi spojovníky: `---`, uvnitř se používá ~~YAML~~ Cíbova prasokonvence. V zásadě je tam každá proměnná na novém řádku, její název je to co je před pajpou (|) a mezerou a obsah co je za ní. Textový obsah (pokud to není pole) se nedává do uvoizovek. Uvozovky v uvozovkách je nejlepší řešit typografickými uvozovkami.

```yaml
---
title| Nejrelativnější „článek“
---
```

Prasostyl umí i pole, to se používá u seznamu autorů. To se píše jako ve většině programovacích jazyků

```yaml
authors| ["Jan Boček", "Jiří Hošek", "Jan Cibulka", "Marcel Šulek"]
```

V hlavičce jsou tyto podporované proměnné. Pokud není napsáno jinak, jsou povinné.

- `title` Nadpis článku.
- `perex` Perex.
- `authors` Seznam autorů.
- `coverimg` Odkaz na webově dosažitelný uvodní velkoobrázek. Co největší, při prvním buildu se vygenerují potřebné zmenšeniny.  Má-li se použít šablona bez obrázku, proměnná se vůbec nezadává a celý řádek se smaže.
- `libraries` pole požadovaných externích knihoven. Je nutné vložit celou URL na knihovnu, nedoporučuju ale odkazovat knihovny na cizích serverech, v každém případě cíl musí být na https.
- `styles` pole požadovaných externích stylů, píše se celá URL, např. `styles: [https://js.arcgis.com/3.17/esri/css/esri.css]`. Opět příliš nedoporučuju odkazovat na cizí servery a opět cíl musí být na https.
- **Ideálně vkládejte JS skripty do složky `js` a CSS styly do složky `styles`**

### Obsah
Obsah se píše v [Markdownu](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Ne všechny prvky jsou nastylovány z výroby, pokud vám nějaký bude scházet. dejte vědět.

Různé interaktivity a obrázky se vkládají přes čisté HTML a s **absolutními cestami k souboru**, v dohledné době přibydou i šablony na boxíky.

## Buildování
Celý článek buildnete příkazem
```bash
python builder.py
```

Build vytvoří `article.html`, jehož obsah následně vrazíte do hlavní položky ve snowfall šabloně.

Pokud potřebujete nahrát nejrůznější obrázky, vkládejte je do složky media, objeví se na adrese `interaktivni.rozhlas.cz/data/jmeno-projektu/media/SOUBOR`.