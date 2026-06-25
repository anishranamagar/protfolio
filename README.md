# Alex Müller — Computer Science Portfolio

> Live site: **[git@github.com:anishranamagar/protfolio.git](https://github.com/anishranamagar/protfolio.git)**

A personal computer science portfolio website built with plain HTML5 and CSS3,
hosted on GitHub Pages as part of a working student application.

---

## Repository Structure

```
.
├── index.html              ← Single-page portfolio website
├── assets/
│   └── css/
│       └── style.css       ← All styles (no framework, pure CSS3)
├── cv/
│   ├── cv.tex              ← LaTeX source for CV
│   └── cv.pdf              ← Compiled CV (download link on website)
├── projects/
│   ├── data-analysis/      ← Python: Student Grade Analyser
│   ├── library-system/     ← Java: Library Management System
│   └── db-design/          ← SQL: University Database Schema
├── report.tex              ← LaTeX project report
└── README.md               ← This file
```

## Projects

| Project | Language | Description |
|---|---|---|
| [Student Grade Analyser](projects/data-analysis/) | Python | CSV processing, descriptive stats, Matplotlib charts |
| [Library Management System](projects/library-system/) | Java | OOP, custom linked list, JUnit tests |
| [University Database Schema](projects/db-design/) | SQL | ER diagram, 3NF normalisation, complex queries |

## Technologies Used

- **HTML5 / CSS3** — No framework; all layout via CSS Grid and Flexbox
- **Vanilla JavaScript (ES6+)** — Scroll effects, mobile nav, IntersectionObserver
- **GitHub Pages** — Free static hosting, auto-deployed on push
- **LaTeX** — CV and project report typesetting (compiled via Overleaf)

## Local Preview

No build step needed. Open `index.html` directly in your browser:

```bash
git clone https://github.com/anishranamagar/protfolio.git
cd git@github.com:anishranamagar/protfolio.git
open index.html       # macOS
xdg-open index.html   # Linux
```

## Deploying to GitHub Pages

1. Create a repository named exactly `git@github.com:anishranamagar/protfolio.git`
2. Push all files to the `main` branch
3. In **Settings → Pages**, set source to `main` branch, root folder
4. Site goes live at `https://github.com/anishranamagar/protfolio.git` within a minute

## Compiling the LaTeX Files

Use [Overleaf](https://overleaf.com) (recommended) or a local TeX installation:

```bash
pdflatex cv/cv.tex       # produces cv/cv.pdf
pdflatex report.tex      # run twice for table of contents
```

---

*Portfolio created as part of a working student application — Gisma University of Applied Sciences, 2025.*
