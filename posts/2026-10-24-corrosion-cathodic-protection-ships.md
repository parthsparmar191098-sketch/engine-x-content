---
title: How Ships Stop Rusting — Corrosion, Sacrificial Anodes and Impressed Current
date: 2026-10-24
updated: 2026-10-26
category: field-notes
summary: Sea water turns a steel hull into a giant battery. How galvanic corrosion works, how zinc and aluminium anodes sacrifice themselves to protect the hull, and how impressed-current systems do it electrically.
seo_title: Ship Corrosion: Sacrificial Anodes vs Impressed Current
seo_description: How sea water corrodes a steel hull, how zinc and aluminium anodes protect it, and how impressed current cathodic protection (ICCP) works.
image: assets/2026-10-24-cathodic-protection.svg
image_alt: Diagram comparing a ship hull protected by sacrificial zinc or aluminium anodes with one protected by an impressed current system using inert anodes, a reference electrode and a controller
image_credit: Diagram: Engine-X
keywords: cathodic protection ship hull, how do sacrificial anodes work, zinc vs aluminium anodes, impressed current cathodic protection ICCP, galvanic corrosion seawater
tldr: Cathodic protection stops a steel hull corroding by making it the cathode of a cell — either with sacrificial zinc or aluminium anodes that corrode instead, or with an impressed-current system that drives protective current from inert anodes.
takeaways:
- Galvanic corrosion needs three things: two different metals, electrical contact, and an electrolyte such as sea water.
- The more active metal (the anode) corrodes; the more noble one (the cathode) is protected.
- Sacrificial anodes of zinc or aluminium are deliberately more active than steel, so they corrode instead of the hull.
- Aluminium anodes hold about 3.4 times more charge per kilogram than zinc.
- Impressed current (ICCP) systems use inert anodes, a reference electrode and a controller, and can last around 15–20 years.
faq:
- What is cathodic protection? | Cathodic protection is a method of stopping corrosion by making the steel the cathode of an electrochemical cell, so that another metal or an external current supplies the electrons instead of the steel dissolving.
- How do sacrificial anodes work on a ship? | Sacrificial anodes are blocks of zinc or aluminium fixed to the hull; because they are more active than steel, they corrode first and send electrons to the hull through the sea water circuit, protecting it.
- Which is better, zinc or aluminium anodes? | Aluminium anodes deliver about 3.4 times more charge per kilogram than zinc, so they last longer for the same weight, while zinc is a long-proven and widely available choice for sea water.
- What is ICCP on a ship? | ICCP (impressed current cathodic protection) uses a DC power unit to push current from inert hull-mounted anodes, with reference electrodes measuring hull potential so a controller can adjust the current automatically.
sources:
- Corrosionpedia — Galvanic corrosion | https://www.corrosionpedia.com/definition/568/galvanic-corrosion
- US EPA — Cathodic protection: nature of discharge (vessel discharges) | https://19january2021snapshot.epa.gov/sites/static/files/2015-08/documents/2007_07_10_oceans_regulatory_unds_tdddocuments_appacathodic.pdf
- Evac — What is a sacrificial anode and why ICCP systems are a better solution | https://evac.com/article/what-is-a-sacrificial-anode-and-why-iccp-systems-are-a-better-solution/
---
Ships stop their steel hulls rusting with two lines of defence: a paint coating that keeps sea water off the steel, and cathodic protection for every scratch the paint misses — zinc or aluminium anodes that corrode instead of the steel, or an electrical system that pushes protective current into the water.

Cathodic protection works by making the hull the protected side of an electrochemical cell, so the steel stops giving up metal even where the paint has a scratch or a holiday (a missed spot).

Sea water is an excellent electrolyte, and a ship is full of different metals in contact: a steel hull, a bronze propeller, stainless shafts and fittings. Left alone, that combination behaves like a battery, and the steel is the part that gets eaten.

## What causes galvanic corrosion?

Galvanic corrosion is the damage that happens when two different metals are in electrical contact in an electrolyte. [Corrosionpedia](https://www.corrosionpedia.com/definition/568/galvanic-corrosion) lists the three conditions it needs:

1. **Two electrochemically different metals.**
2. **Electrical contact** between them (touching, welded, bolted or connected by a wire or the hull itself).
3. **An electrolyte** connecting them — sea water is ideal.

In that circuit, the more active (less noble) metal becomes the **anode** and corrodes faster than it would alone. The more noble metal becomes the **cathode** and corrodes slowly or not at all. Metal ions leave the anode into the water while electrons flow through the metal path to the cathode.

How far apart two metals sit on the **galvanic series** — the ranking of metals by how active they are in sea water — decides how strong the effect is. Corrosionpedia gives two extremes: zinc in contact with platinum in salt water corrodes very quickly, while 304 and 316 stainless steel have little effect on each other. The area ratio of the two metals also changes the rate.

## How does cathodic protection stop corrosion?

Cathodic protection stops corrosion by turning the steel you care about into the cathode of the cell. If the steel is the cathode, the corrosion happens somewhere else. There are two ways to supply the electrons that make this happen:

- **Sacrificial anodes** — a more active metal corrodes and supplies them.
- **Impressed current** — a power supply drives them in from inert anodes.

Both rely on the same principle. The [EPA's vessel discharge report](https://19january2021snapshot.epa.gov/sites/static/files/2015-08/documents/2007_07_10_oceans_regulatory_unds_tdddocuments_appacathodic.pdf) describes impressed current as using shipboard DC power instead of an anode's own galvanic current, with the protection mechanism otherwise the same.

## How do sacrificial anodes work on a ship?

Sacrificial anodes work by being deliberately more active than steel. A block of zinc or aluminium alloy is welded or bolted to the hull; with the hull as cathode and sea water as electrolyte, the anode corrodes first and sends electrons to the steel.

[Evac](https://evac.com/article/what-is-a-sacrificial-anode-and-why-iccp-systems-are-a-better-solution/) describes this as the anode, hull and sea water forming a galvanic cell in which the anode is consumed so the hull corrodes less.

The EPA report gives the key material numbers:

| Anode material | Charge capacity | Notes |
|---|---|---|
| Zinc (≈99.3% Zn) | 812 A·h/kg | Long-proven in sea water; widely used |
| Aluminium alloy (≈95% Al, with zinc and indium) | 2,759 A·h/kg | About 3.4× zinc per kg; more prone to passivation |

The number and size of anodes depend on the wetted area of the hull, the planned replacement interval and the ship's corrosion history. The EPA report notes that sacrificial anodes suit large ships with dry-docking intervals under three years and most smaller craft. It also records how fast they go: Navy maintenance records show about half of a zinc anode consumed after three years, with full consumption around six years on average — and consumption about four times faster underway than alongside.

Anodes are fitted where corrosion risk is highest: along the hull, around the stern near the bronze propeller, and on appendages. They are also used inside sea chests, ballast tanks and heat exchangers. Renewing them is a standard [dry-docking](https://engx3d.com/blog/posts/2026-10-23-what-is-ship-dry-docking.html) job.

## How does an impressed current (ICCP) system work?

An impressed current cathodic protection (ICCP) system works by pushing DC current from the ship's power supply through inert anodes into the sea water and back to the hull.

The EPA report describes the anodes as platinum-plated tantalum designed for a 20-year service life, with a silver/silver chloride reference electrode measuring the hull's potential so the system can adjust its output.

An ICCP system has three main parts:

1. **Inert anodes** mounted on the hull, insulated from it. They pass current but are not consumed like zinc.
2. **Reference electrodes** that measure the hull's electrical potential against the sea water — the "sensor" that shows whether the hull is protected.
3. **A controller and power unit** that raises or lowers the current automatically. Evac notes this lets the system keep protection steady as water temperature and salinity change.

Evac lists the advantages: fewer anodes, more even protection on large or complex hulls, maintenance without dry-docking, and a design life of around 15 years for some anode designs. The trade-off is a higher upfront cost and the need for a working power supply and controller.

## Sacrificial anodes vs ICCP: which is better?

| | Sacrificial anodes | ICCP |
|---|---|---|
| Power needed | None | Ship's DC supply |
| Adjustable | No — output fixed by anode size | Yes — controller follows conditions |
| Anode life | Consumed; typically renewed every few years | Inert anodes; ~15–20 year design life |
| Best for | Small and mid-size ships, sea chests, tanks | Large hulls, long dry-dock intervals |
| Main risk | Anodes used up or painted over | Controller fault or over-protection damaging paint |

Many ships use both: ICCP for the main hull, and sacrificial anodes in sea chests, tanks and coolers where an impressed system cannot reach.

## The engineering takeaway

Corrosion in sea water is electrochemistry, so the fix is electrochemistry too. Coatings keep the water away, and cathodic protection makes sure that wherever the water does reach the steel, something else corrodes instead — a zinc or aluminium block you can replace, or current from a controller. The rule that follows from the galvanic series applies everywhere on board: think about which metal is the anode before you join two different metals in sea water, whether it is a hull fitting, a [heat exchanger](https://engx3d.com/blog/posts/2026-10-23-shell-and-tube-vs-plate-heat-exchanger.html) or a pipe flange. And never paint over an anode — a coated anode protects nothing.
