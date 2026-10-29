---
title: How a Cooling Tower Works — Evaporation, Range, Approach and Water Loss
date: 2026-10-24
updated: 2026-10-26
category: field-notes
summary: A cooling tower cools water by evaporating a small part of it into moving air. How the fill, fans and drift eliminators work, what range and approach mean, and how much water a tower uses.
seo_title: How a Cooling Tower Works: Range, Approach, Water Loss
seo_description: How a cooling tower cools water by evaporation: fill, fans and drift eliminators, what range and approach mean, and how much water it uses.
image: assets/2026-10-24-cooling-tower.svg
image_alt: Diagram of an induced-draft counterflow cooling tower with hot water sprayed over fill, air drawn up by a fan, drift eliminators, cold water basin, and labels for range, approach and wet-bulb temperature
image_credit: Diagram: Engine-X
keywords: how does a cooling tower work, cooling tower range and approach, cooling tower evaporation loss, cycles of concentration blowdown, counterflow vs crossflow cooling tower
tldr: A cooling tower rejects heat by evaporating about 1% of its circulating water for every 5.6 °C of cooling, and it can never cool water below the air's wet-bulb temperature.
field_note: I have supervised underwater cooling-tower jobs on an industrial site as part of my marine engineering work.
takeaways:
- Cooling towers cool water mainly by evaporation: a small part of the water evaporates and carries heat away.
- Range is how much the tower cools the water; approach is how close the cold water gets to the wet-bulb temperature.
- Wet-bulb temperature is the limit — no evaporative tower can cool water below it.
- Rule of thumb: about 1% of the circulating flow evaporates for every 10 °F (≈5.6 °C) of range.
- Blowdown removes concentrated minerals; running more cycles of concentration saves make-up water.
faq:
- How does a cooling tower work? | A cooling tower sprays warm water over a fill that spreads it into thin films, while a fan or natural draft moves air through it; part of the water evaporates, and the heat needed for evaporation is taken from the rest of the water, cooling it.
- What is range and approach in a cooling tower? | Range is the hot-water inlet temperature minus the cold-water outlet temperature; approach is the cold-water outlet temperature minus the air's wet-bulb temperature.
- How much water does a cooling tower lose to evaporation? | As a rule of thumb, about 1% of the circulating flow evaporates for every 10 °F (about 5.6 °C) the water is cooled.
- What is blowdown in a cooling tower? | Blowdown is the deliberate draining of some basin water to remove dissolved minerals that build up as water evaporates, preventing scale and corrosion.
sources:
- Power Engineering — Understanding the basics of cooling tower heat transfer | https://www.power-eng.com/operations-maintenance/understanding-the-basics-of-cooling-tower-heat-transfer/
- Chem-Casts — What is a cooling tower and how does it work? | https://chem-casts.com/knowledge/what-is-a-cooling-tower-and-how-does-it-work
- US EPA — WaterSense at Work, Section 6.3: Cooling towers | https://www.epa.gov/system/files/documents/2023-05/ws-commercial-watersense-at-work_Section_6.3_Cooling_Towers.pdf
---
A cooling tower is a heat exchanger that cools warm water by letting a small part of it evaporate into a stream of air. The evaporating water takes heat from the water around it, so the rest falls into the basin cooler and goes back to the plant.

Because the cooling comes from evaporation, a cooling tower can cool water below the air temperature — down towards the air's wet-bulb temperature, but never below it.

Cooling towers sit beside almost every large refinery, power station, chemical plant and air-conditioning system. They take the heat that condensers and process coolers pick up and dump it into the atmosphere. Without them, those plants would need a river's worth of once-through cooling water.

## How does a cooling tower cool water?

A cooling tower cools water mainly through evaporation. [Power Engineering](https://www.power-eng.com/operations-maintenance/understanding-the-basics-of-cooling-tower-heat-transfer/) states that evaporation is the primary method of heat transfer in a cooling tower, with only about 2–3% of the circulating water evaporating. Turning water into vapour needs a lot of energy — the latent heat of vaporisation — and that energy comes from the water that stays liquid.

A smaller share of the cooling is ordinary sensible heat transfer: the cooler air simply warms up as it passes the hot water. Power Engineering accounts for this with a correction factor in its evaporation formula, typically 0.65–0.90 (higher in summer, lower in winter).

## What are the main parts of a cooling tower?

The main parts of a cooling tower each do one job in the air-water contact process. [Chem-Casts](https://chem-casts.com/knowledge/what-is-a-cooling-tower-and-how-does-it-work) lists them:

1. **Hot water distribution** — pipes and spray nozzles (or open distribution basins) spread warm water evenly over the top of the fill.
2. **Fill (packing)** — the heart of the tower. It breaks the water into droplets (**splash fill**) or spreads it into thin sheets over plastic surfaces (**film fill**), giving a huge area for air and water to meet. Film fill is the more efficient, but it fouls more easily with dirty water.
3. **Air inlet and fan** — air enters at the base or sides. In mechanical-draft towers a fan moves it; in natural-draft towers the warm, moist air rises by itself.
4. **Drift eliminators** — zig-zag blades above the fill that catch water droplets carried up by the air, so they are not blown out of the tower.
5. **Cold water basin** — collects the cooled water, and holds the make-up and blowdown connections.

## What is range and approach in a cooling tower?

Range and approach are the two numbers that describe how hard a cooling tower is working:

- **Range** = hot water in − cold water out. It is how much the tower cools the water, and it is set by the plant's heat load and flow.
- **Approach** = cold water out − wet-bulb temperature. It is how close the tower gets to its theoretical limit.

Chem-Casts gives a typical example: hot water at 42 °C, cold water at 32 °C and a wet-bulb temperature of 27 °C give a **range of 10 °C** and an **approach of 5 °C**. A smaller approach means a better-performing (and usually larger) tower.

**Wet-bulb temperature** is the temperature a wet surface reaches when air blows over it and water evaporates. Unless the air is fully saturated, it is lower than the normal (dry-bulb) temperature. That is why, as Power Engineering points out, an evaporative tower can produce colder water than an air-cooled radiator in the same weather — and why the same tower performs worse on a hot, humid day, when the wet-bulb temperature rises.

## What types of cooling towers are there?

Cooling towers are grouped by how the air moves and which way it meets the water:

| Type | How air moves | Notes |
|---|---|---|
| Natural draft | Buoyancy (chimney effect) in a tall hyperbolic shell | Often over 100 m tall; mainly large power plants |
| Induced draft | Fan at the top pulls air through | Common in industry; good efficiency |
| Forced draft | Fan at the base pushes air in | Easier to install, more prone to recirculating warm air |
| Counterflow | Air rises straight up against falling water | Compact and efficient |
| Crossflow | Air moves sideways across falling water | Easier to inspect and maintain |

Most industrial towers combine one airflow type with one flow pattern — for example, an induced-draft counterflow tower, which is the arrangement Power Engineering analyses.

## How much water does a cooling tower use?

A cooling tower uses water in three ways: evaporation, drift and blowdown. The [US EPA](https://www.epa.gov/system/files/documents/2023-05/ws-commercial-watersense-at-work_Section_6.3_Cooling_Towers.pdf) gives the standard rule of thumb: about **1% of the circulating flow evaporates for every 10 °F (≈5.6 °C) of range**. The EPA adds that cooling towers can account for 20–50% or more of a facility's total water use.

**Drift** is water lost as droplets. The EPA puts it at 0.05–0.2% of flow without good eliminators, and below 0.005% with modern drift eliminators.

**Blowdown** exists because evaporation leaves minerals behind. As pure water evaporates, the dissolved solids in the basin become more concentrated, and eventually form scale and cause corrosion. Some water is drained off and replaced with fresh make-up water. The ratio of the basin's mineral content to the make-up water's is the **cycles of concentration (CoC)**; the EPA notes many systems run at 2–4 cycles, and that raising cycles from 3 to 6 cuts make-up water by about 20% and blowdown by about 50%.

**Worked example.** A tower circulates 1,000 m³/h with a 8 °C range:

1. Evaporation ≈ 1% × (8 ÷ 5.6) × 1,000 ≈ **14 m³/h**.
2. At 4 cycles of concentration, blowdown = evaporation ÷ (CoC − 1) = 14 ÷ 3 ≈ **4.7 m³/h** (formula from Power Engineering and Chem-Casts).
3. Make-up ≈ evaporation + blowdown + drift ≈ **19 m³/h**, or about 450 m³ a day.

## What goes wrong with cooling towers?

Cooling towers mostly lose performance through water and airflow problems. Chem-Casts lists the usual ones: **scaling** from high dissolved solids and poor blowdown control, **biological fouling** in warm, stagnant water (controlled with biocides), **dirty or damaged fill** that raises the cold-water temperature, **damaged drift eliminators** that increase drift, and **fan imbalance** that causes vibration.

The EPA recommends monitoring pH, conductivity, hardness, microbial growth and inhibitor levels, and metering make-up and blowdown so leaks and overflows show up early.

## The engineering takeaway

A cooling tower is a controlled evaporator. Its performance is limited by the weather (wet-bulb temperature), set by its fill and airflow (approach), and paid for in water (evaporation plus blowdown). Keeping the fill clean, the chemistry controlled and the drift eliminators intact keeps the approach low — and every degree of colder water helps the [heat exchangers](https://engx3d.com/blog/posts/2026-10-23-shell-and-tube-vs-plate-heat-exchanger.html) and condensers it serves. The circulating water pumps need the same care as any other pump: enough suction head to avoid [cavitation](https://engx3d.com/blog/posts/2026-10-22-pump-cavitation-npsh.html).
