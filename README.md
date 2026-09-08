# Open Biocenter

**A laboratory you can operate from anywhere.**

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

Live control page: <https://opendrop.151-115-76-163.sslip.io/>

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

## Licences

Writing, drawings and photographs are under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Hardware designs are
under the [CERN Open Hardware Licence](https://cern-ohl.web.cern.ch/). Control
software is published under its own open source licence. Everything here is
free to share, adapt and build on, with attribution.

## This repository

The site is one self-contained page. `index.html` carries its own CSS, its
p5.js sketches and its images, so deploying it means copying a single file. It
follows the Open Science Foundation brand,
[osf-brand](https://github.com/Opening-Science/osf-brand).

`fonts/` is deliberately absent. Selecta (Maxitype) and ABC Diatype Semi Mono
are licensed commercially for this subdomain and cannot be redistributed, so
they live on the server only. A clone renders in fallback faces.
