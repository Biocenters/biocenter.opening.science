# Open Biocenter — biocenter.opening.science

The site is a single self-contained page. `index.html` carries its own CSS,
its p5.js sketches and its images as data URIs, so deploying it is copying
one file.

## What is here

| Path | Role |
|---|---|
| `index.html` | the whole page |
| `og.jpg` | social sharing image, 1200x630 |
| `robots.txt`, `sitemap.xml` | crawling |

## What is deliberately absent

`fonts/` holds Selecta (Maxitype) and ABC Diatype Semi Mono, both under
commercial licence for this subdomain. They are installed on the server and
excluded here: this repository must stay redistributable.

## Design

The page follows the Open Science Foundation brand:
<https://github.com/Opening-Science/osf-brand>. Colour tokens are the OSF
palette, the two typefaces are the ones the brand declares, and no shadow or
gradient is used.

## How it changes

The page is edited in place at `/#edit`, protected by a password nginx checks
on `PUT /save`. Each save triggers a timestamped snapshot in `.backups/` and a
commit here.
