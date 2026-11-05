---
title: DIAL: The 3D Printing Method That Lets the Ink Hold Up Its Own Overhangs
date: 2026-11-05
category: news
tag: design
summary: Northwestern engineers spread a paste-like ink into thin sheets and harden it with patterned light. The unhardened paste supports overhangs, so no scaffolds are needed, and one test part printed over 4x faster.
seo_title: DIAL 3D Printing: Yield-Stress Ink With No Supports
seo_description: Northwestern's DIAL method spreads paste-like ink into 50-micron sheets and cures it with light. How it works, why no supports are needed, and what it prints.
image: assets/2026-11-05-dial-3d-printing.svg
image_alt: Diagram of the DIAL 3D printing cycle: a slot-die nozzle lays paste-like ink, a blade spreads it into a 50-micron sheet, a projector cures a pattern, and the uncured paste holds up an overhang without supports
image_credit: Diagram: Engine-X
keywords: DIAL 3D printing, direct ink additive lithography, yield stress ink 3D printing, 3D printing without supports, Northwestern 3D printing
tldr: DIAL combines extrusion-style thick inks with light-based curing, and because the uncured paste holds its shape, it prints overhangs without supports and fine features faster than extrusion.
takeaways:
- DIAL stands for direct ink additive lithography, from Northwestern University.
- A blade spreads paste-like ink into 50-micron sheets; a projector hardens each layer's pattern.
- The ink has a yield stress, so the uncured paste stays put and supports overhangs.
- A porous grid took 30 minutes with DIAL against 124 minutes with extrusion printing.
- Uses shown: battery electrolyte lattices and hydrogel cell-culture containers.
faq:
- What is DIAL 3D printing? | DIAL (direct ink additive lithography) is a 3D printing method from Northwestern University that spreads a thick, paste-like ink into thin sheets and hardens each layer's pattern with projected light, layer after layer.
- Why does DIAL not need support structures? | The ink has a yield stress: it flows while the blade spreads it, then stiffens and holds its shape, so the uncured ink around the part holds up overhangs and bridges until the print is finished.
- How fast is DIAL compared with extrusion printing? | In Northwestern's test, a porous grid took 30 minutes with DIAL and 124 minutes with conventional extrusion printing, more than four times faster.
sources:
- EurekAlert! (Northwestern University) — New method DIALs up new capabilities for 3D printing | https://www.eurekalert.org/news-releases/1150529
- Mirage News — New DIAL method expands 3D printing capabilities | https://www.miragenews.com/new-dial-method-expands-3d-printing-capabilities-1772084/
- Science Advances — Rapid, voxel-based 3D printing with yield-stress fluid inks | https://www.science.org/doi/10.1126/sciadv.aei1146
---
DIAL is a new 3D printing method from Northwestern University that spreads a thick, paste-like ink into 50-micron sheets and hardens each layer with patterned light. Because the paste holds its own shape, the uncured ink supports overhangs, so no scaffolds are needed. In one test it printed a porous grid in 30 minutes, against 124 minutes for extrusion.

The study was published in *Science Advances* on 4 November 2026 by Pranav Kaarthik (lead author) and Ryan Truby (senior author) of Northwestern's Robotic Matter Lab, [according to the university's release](https://www.eurekalert.org/news-releases/1150529). DIAL stands for direct ink additive lithography. It takes the thick inks of extrusion printing and the light-based curing of resin printing and puts them in one machine.

## How does DIAL 3D printing work?

DIAL 3D printing works by laying down a thin, even sheet of paste and then curing only the parts of it that belong to the object. Each layer goes through the same cycle:

1. A slot-die nozzle, a long narrow slot, pushes the paste-like ink onto a flat build surface.
2. A blade sweeps across and spreads the ink into a uniform sheet about 50 microns thick.
3. A projector shines a patterned image onto the sheet, hardening only the lit areas.
4. The next sheet is spread on top, and the cycle repeats until the part is complete.
5. The uncured ink is washed away, and the excess can be reused.

Northwestern says resolution depends mainly on the projector's pixel size and the layer thickness, not on the nozzle size, so clogging matters less than in extrusion printers.

## Why does DIAL not need support structures?

DIAL does not need supports because its ink has a yield stress. A yield-stress fluid is one that behaves like a solid until enough force is applied, then flows, like toothpaste: it comes out when squeezed and stays as a ribbon on the brush. The team made its model ink yield-stress by mixing fumed silica nanoparticles into a light-curable resin.

Under the blade the ink flows; once the blade passes, it stiffens and stays put. So the uncured paste around the part acts as a temporary support for overhangs and bridges. In normal extrusion printing, Kaarthik notes, "If you don't print the scaffold, your printed object will literally fail."

## How does DIAL compare with other printing methods?

DIAL sits between the two printing families engineers already use, and borrows a strength from each:

| | Extrusion (direct ink writing) | Resin vat (light curing) | DIAL |
|---|---|---|---|
| Ink | Thick pastes, filled inks | Runny liquid resins | Thick pastes, filled inks |
| How a layer is made | Nozzle draws each line | Light cures a whole layer | Blade spreads a sheet, light cures it |
| Overhangs | Need printed supports | Need printed supports | Held up by the uncured paste |
| Fine detail limited by | Nozzle size | Projector pixels | Projector pixels and layer thickness |

The test numbers in the release and in [Mirage News](https://www.miragenews.com/new-dial-method-expands-3d-printing-capabilities-1772084/):

- **Speed:** a porous grid in 30 minutes, against 124 minutes with conventional extrusion.
- **Detail:** lattice walls as thin as 150 microns, which extrusion could not produce.
- **Batteries:** 15 porous electrolyte lattices, each about the size of a coin cell, in a single 15-minute run, using a polymerizable ionic liquid.
- **Biology:** hydrogel containers like cell-culture inserts, with arrays of microscopic inverted pyramids.
- **Size:** a honeycomb nearly four times larger than the projector's illumination area.

## What does DIAL mean for engineers and designers?

For engineers, DIAL matters because many useful materials only come as thick, particle-filled pastes, which resin printers cannot use and extrusion printers struggle to print finely. Designers also get freedom from supports: no support marks to grind off and no internal scaffolds trapped in lattices. The team lists aerospace, robotics, medical devices, energy storage and tissue engineering as targets. It is a lab method for now, not a printer you can buy.

Choosing a material still comes first, as in our [practical material selection guide](https://engx3d.com/blog/posts/2026-10-26-material-selection-ms-ss304-ss316-cast-iron.html), and the CAD model behind any print starts in tools compared in [AutoCAD vs SolidWorks](https://engx3d.com/blog/posts/2026-10-26-autocad-vs-solidworks.html). If you want to try printing machine parts today, every part of the Engine-X machines is a [free STL download](https://engx3d.com/3d-models/).

## The engineering takeaway

DIAL makes the ink do the job of the supports. A yield-stress paste spread in 50-micron sheets and cured by light gives extrusion-style materials with resin-style detail, and prints overhangs without scaffolds. It beat extrusion by more than four times on one test part. Watch for it in printed battery parts and medical devices first.
