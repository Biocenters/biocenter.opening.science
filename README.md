# Open Biocenter

**A laboratory you can operate from anywhere.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22685448.svg)](https://doi.org/10.5281/zenodo.22685448)

<https://biocenter.opening.science>

## Intro

Most experiments still happen in a local lab, performed by a person standing
at a bench. Compute met the same limit decades ago and answered it with data
centers: shared machines, remote access, capacity added one unit at a time.
Biology has no equivalent.

## What an Open Biocenter is

A building that holds machines instead of benches. Each machine automates one
class of experiment and occupies one slot in a rack. Capacity grows by adding
slots, not by hiring hands.

A team anywhere on the planet opens a web page or a phone. Commands travel to
a machine in Interlaken, which moves a real sample. Onboard sensors and a
camera report what happened. On the way back, machine vision reads the images
and world models turn them into a state the team can act on.

## First prototype

The **OpenDrop BioServer** was installed on 1 September 2026 in Interlaken,
Switzerland. Two OpenDrop boards sit in a glass enclosure. Each carries an
electrode array that moves droplets across a surface by switching voltage cell
by cell, with magnets and heaters acting on the droplet as it travels. Samples
and reagents sit on the shelf below. A console reports the state of the
machine, and the unit answers to a web page over the network.

Live control page: [external-service notice](https://biocenter.opening.science/external-control.html).

## Features

- **Open hardware.** The design files for every machine in the rack are public.
- **Open source.** The control software is published and runs on hardware you own.
- **Auditable by reading.** A claim about what a machine did can be checked
  against its design.
- **Forkable.** Anyone can build a second unit and change it.
- **No vendor lock-in.** No part of the stack is held by a single supplier.
- **Reproducible elsewhere.** A result obtained here can be repeated on a
  machine someone else owns.
- **Remote by default.** Every operation available at the bench is available
  over the network.
- **Observation first.** The state of the sample returns before the next
  command is sent.

## Who

| | |
|---|---|
| [GaudiLabs](https://www.gaudi.ch/OpenDrop/) | Urs Gaudenz, Miranda Moss |
| [Radical Design Studio](https://radicaldesignstudio.eu) | JB Labrune |
| [Open Science Foundation](https://opening.science) | Host of the partnership, at Etherlaken |
| Etherlaken | The site, Interlaken, Switzerland |

## Brand and marks

The favicon is this site's own. The header carries the Open Science
Foundation website mark (`assets/logo/OSF_mark_website.svg`, sha256
`bef9c1f9...07aa1935`), and the footer carries the full lockup. Both are
reproduced unmodified, at the request of the Foundation. The Open Science
Foundation lockup in the footer is reproduced **unmodified** under the
[OSF Brand Assets Permission](https://github.com/Opening-Science/osf-brand/blob/main/LICENSES/LicenseRef-OSF-Brand-Assets.txt)
(`LicenseRef-OSF-Brand-Assets`), to identify the host of this partnership. It is
the base64 of `assets/logo/OSF_positive_original.svg` from
[osf-brand](https://github.com/Opening-Science/osf-brand), sha256
`6a2813ca…e86d5f8a`, byte-identical to that repository's manifest.

That permission is limited and not an open licence. Under it: do not recolour,
crop, distort, redraw or recombine the lockup, and do not present it as this
site's own identity. It stays a footer credit; the header mark is ours. Nothing
here is a claim of endorsement beyond the hosting relationship OSF actually has,
and no trademark registration is asserted.

## Licences

Writing, drawings and photographs are under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Hardware designs are
under the [CERN Open Hardware Licence](https://cern-ohl.web.cern.ch/). Control
software is published under its own open source licence. Everything here is
free to share, adapt and build on, with attribution.

## This repository

The site is one self-contained page. `index.html` carries its own CSS, its
p5.js sketches and its images, and is accompanied by `external-control.html`, the exit notice for the live control interface. Deploy both HTML files and the existing static assets. It
follows the Open Science Foundation brand,
[osf-brand](https://github.com/Opening-Science/osf-brand).

The palette is the OSF palette unchanged, and the type scale uses OSF values.
The root font size steps 13.2px to 17px across the same six breakpoints as
opening.science, so every rem token resizes with the viewport the way the OSF
theme intends. Two deliberate deviations: `--text-xs` (0.75rem) has no OSF
counterpart and is local to this page, and the local scale names run one step
below the canonical ones. Both are recorded in the token block in `index.html`.

osf-brand's web harness targets Nuxt 4 and Astro 5. This page is neither, so
its checks do not apply here and the tokens are carried by hand.

`fonts/` is deliberately absent. Selecta (Maxitype) and ABC Diatype Semi Mono
are licensed commercially for this subdomain and cannot be redistributed, so
they live on the server only. A clone renders in fallback faces.

## How it changes

The page is edited in place at `/#edit`, guarded by a password nginx checks
on `PUT /save`. Every save keeps a timestamped snapshot on the server, commits
here and pushes.

The sync runs both ways. A pull request merged on GitHub is pulled onto the
server within five minutes and deployed, so contributors do not need shell
access to change the site. A local edit and a merged pull request landing at
the same time are reconciled by rebase.


## External control notice

Both control links go through `/external-control.html`. The notice works without
JavaScript, shows the fixed destination and offers a return link. Only Continue
contacts the control service; it sends no Referer header. Do not add automatic
redirects, destination query parameters, embeds or prefetching. The page's fonts
and tokens are copied from index.html; keep those blocks in sync when restyling.

Before release, confirm with the partner the service operator, support contact,
privacy/terms URLs and whether access is public or limited to authorised users.
The current copy intentionally does not guess an operator or promise public
access. The notice does not grant permission to operate equipment.

Deployment: verify `/external-control.html` is served as its own file (not the
homepage fallback) after the repository sync. A deployment copying only
index.html must be updated to copy this file too. No server configuration or
hardware-access controls are changed by this PR.

Run `python3 -m unittest discover -s tests -v` for navigation-boundary checks.
