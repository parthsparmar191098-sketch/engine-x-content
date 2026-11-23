---
title: How to Calculate Hydraulic Cylinder Force and Speed, With Worked Examples
date: 2026-11-18
category: learn
summary: Two formulas size almost every hydraulic cylinder: force = pressure × area and speed = flow ÷ area. Worked through on a 63 mm cylinder fed by a 16 cm³ gear pump, with a quick table for common bores.
seo_title: How to Calculate Hydraulic Cylinder Force and Speed
seo_description: Hydraulic cylinder force = pressure × area and speed = flow ÷ area, worked through for a 63 mm cylinder on a 24 L/min pump, with a bore table.
image: assets/2026-11-18-cylinder-force-speed.svg
image_alt: Diagram of a 63 mm hydraulic cylinder extending with oil on the full 31.2 square centimetre piston for 49.9 kN at 12.8 cm per second, and retracting with oil on the 21.0 square centimetre ring for 33.6 kN at 19.1 cm per second
image_credit: Diagram: Engine-X
model: hydraulics
keywords: how to calculate hydraulic cylinder force, hydraulic cylinder speed calculation, hydraulic cylinder force formula bar, why does a hydraulic cylinder retract faster, gear pump flow calculation
tldr: Cylinder force is pressure times the area the oil pushes on, and speed is pump flow divided by that area; on the rod side the area is smaller, so the rod pulls with less force but moves faster.
takeaways:
- Force (kN) = pressure (bar) × area (cm²) ÷ 100.
- Speed (cm/s) = flow (L/min) × 1000 ÷ area (cm²) ÷ 60.
- Pushing uses the full piston area; pulling uses the piston area minus the rod area.
- A 63 mm cylinder at 160 bar pushes 49.9 kN and pulls 33.6 kN.
- Pump flow is displacement × speed: 16 cm³/rev at 1500 rpm is 24 L/min.
faq:
- How do you calculate the force of a hydraulic cylinder in bar? | Multiply the pressure in bar by the piston area in square centimetres and divide by 100 to get kilonewtons. A 63 mm bore has 31.2 cm², so at 160 bar it pushes 160 × 31.2 ÷ 100 = 49.9 kN.
- Why does a hydraulic cylinder retract faster than it extends? | On the rod side the rod takes up part of the area, so the same pump flow fills a smaller volume per millimetre of travel. With a 63 mm bore and 36 mm rod the rod side is 21.0 cm², so it retracts about 1.5 times faster.
- How do you work out the flow of a gear pump? | Multiply its displacement by its speed. A 16 cm³/rev pump at 1500 rpm delivers 16 × 1500 = 24,000 cm³ per minute, or 24 L/min, before a few percent of internal leakage.
- Does a bigger pump make a cylinder stronger? | No. A bigger pump gives more flow and so more speed. Force comes from pressure and area, so for more force you need a higher pressure setting or a bigger bore.
sources:
- Mobile Hydraulic Tips — Hydraulic cylinders for mobile machinery | https://www.mobilehydraulictips.com/hydraulic-cylinders-mobile-machinery/
- Atos — KTC hydraulic cylinders catalogue (CK series, ISO 6020-2) | https://www.atos.com/tables/english/KTC_Atos-hydraulic-cylinders-catalog-EN.pdf
- Rexroth AZPF-12-016 external gear pump | https://hydraulicpartsusa.com/products/bosch-rexroth/azpf-external-high-performance-gear-pumps/AZPF-12-016RRR20MB
- Axflow — How external gear pumps work | https://www.axflow.com/en-gb/applications/technical-support/pump-technologies/pump-types/how-external-gear-pumps-work/
- Engine-X — Hydraulic pump and cylinder 3D model | https://engx3d.com/3d-models/hydraulic-cylinder
---
A hydraulic cylinder's force is pressure times the area the oil pushes on, and its speed is the pump flow divided by that area. A 63 mm cylinder at 160 bar pushes 49.9 kN. Fed by a 24 L/min gear pump it extends at 12.8 cm/s and retracts faster, at 19.1 cm/s, because the rod side has less area.

All the numbers below come from the new [Engine-X hydraulic pump and cylinder 3D model](https://engx3d.com/3d-models/hydraulic-cylinder), and the [hydraulic cylinder guide](https://engx3d.com/hydraulic-cylinder) walks through the pump, valve and cylinder part by part.

## What is the formula for hydraulic cylinder force?

Force = pressure × area ([Mobile Hydraulic Tips](https://www.mobilehydraulictips.com/hydraulic-cylinders-mobile-machinery/)). Makers quote the bore diameter, so work out the area first, and keep the units consistent. In bar and square centimetres, 1 bar on 1 cm² is 10 N, which gives a handy form:

**Force (kN) = pressure (bar) × area (cm²) ÷ 100**

For a 63 mm bore:

1. Piston area = π ÷ 4 × 6.3² = **31.2 cm²**.
2. At 160 bar, force = 160 × 31.2 ÷ 100 = **49.9 kN**, about 5 tonnes.

That matches the maker's figure: Atos lists 31.2 cm² and 49.9 kN at 160 bar for its 63 mm CK cylinder, which is rated 160 bar nominal and 250 bar maximum ([Atos](https://www.atos.com/tables/english/KTC_Atos-hydraulic-cylinders-catalog-EN.pdf)).

## Why is the pulling force smaller?

Because on the rod side the rod covers part of the piston, so the oil only pushes on the ring around it. Subtract the rod area from the piston area ([Mobile Hydraulic Tips](https://www.mobilehydraulictips.com/hydraulic-cylinders-mobile-machinery/)).

With a 36 mm rod, the rod area is π ÷ 4 × 3.6² = 10.2 cm², leaving 31.2 − 10.2 = **21.0 cm²**. At 160 bar the pull is 160 × 21.0 ÷ 100 = **33.6 kN**, two thirds of the push. On a cylinder with a 2 : 1 area ratio, extending gives twice the force of retracting.

## How fast will the cylinder move?

Speed depends on flow, not pressure. The pump sends a fixed volume of oil per minute, and the piston must move far enough to make room for it:

**Speed (cm/s) = flow (L/min) × 1000 ÷ area (cm²) ÷ 60**

First the flow. A gear pump moves a fixed volume every turn, so flow is proportional to speed ([Axflow](https://www.axflow.com/en-gb/applications/technical-support/pump-technologies/pump-types/how-external-gear-pumps-work/)). A 16 cm³/rev pump, rated 250 bar continuous ([Rexroth AZPF](https://hydraulicpartsusa.com/products/bosch-rexroth/azpf-external-high-performance-gear-pumps/AZPF-12-016RRR20MB)), turned at 1,500 rpm by a 4-pole motor gives 16 × 1,500 = 24,000 cm³/min, or **24 L/min**, before a few percent of internal leakage.

Then the two directions:

- **Extending:** 24 × 1000 ÷ 31.2 ÷ 60 = **12.8 cm/s**, so a 200 mm stroke takes about 1.6 s.
- **Retracting:** 24 × 1000 ÷ 21.0 ÷ 60 = **19.1 cm/s**, about 1.5 times faster.

The rod side needs less oil per millimetre of travel, so the same flow moves the rod back faster ([Mobile Hydraulic Tips](https://www.mobilehydraulictips.com/hydraulic-cylinders-mobile-machinery/)).

## Quick table for common bores

Push and pull at 160 bar, and speeds on a 24 L/min pump, worked out with the two formulas above. The rod sizes are typical examples; check your cylinder's data sheet.

| Bore / rod (mm) | Piston area (cm²) | Push at 160 bar | Pull at 160 bar | Out at 24 L/min | In at 24 L/min |
|---|---|---|---|---|---|
| 40 / 22 | 12.6 | 20.1 kN | 14.0 kN | 31.8 cm/s | 45.6 cm/s |
| 50 / 28 | 19.6 | 31.4 kN | 21.6 kN | 20.4 cm/s | 29.7 cm/s |
| 63 / 36 | 31.2 | 49.9 kN | 33.6 kN | 12.8 cm/s | 19.1 cm/s |
| 80 / 45 | 50.3 | 80.4 kN | 55.0 kN | 8.0 cm/s | 11.6 cm/s |
| 100 / 56 | 78.5 | 125.7 kN | 86.3 kN | 5.1 cm/s | 7.4 cm/s |

The table shows the trade-off clearly: doubling the bore gives about four times the force but a quarter of the speed on the same pump.

## Three mistakes to avoid

1. **Using the full area for pulling.** Always subtract the rod; otherwise the pulling force is overestimated by a third or more.
2. **Thinking a bigger pump gives more force.** More flow gives more speed. Force comes only from pressure and area, so more force needs a higher relief setting, within the cylinder's rating, or a bigger bore.
3. **Using the relief setting as the working pressure.** The relief valve is the ceiling. Size the cylinder so the load needs less than that, or it will stall at the relief pressure and turn the pump's power into heat.

## The engineering takeaway

Pressure decides force and flow decides speed. Area connects both, which is why the rod side of a cylinder is always weaker and faster: the same oil has less area to push on.
