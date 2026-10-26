---
title: Ball, Roller or Journal Bearing? How Bearing Types Work and How to Choose
date: 2026-10-23
updated: 2026-10-26
category: guide
summary: Ball, roller and journal bearings all carry a turning shaft, but in very different ways. How each type works, which loads it handles, and how bearing life is calculated.
image: assets/2026-10-23-bearing-types.svg
image_alt: Diagram comparing a ball bearing with point contact, a roller bearing with line contact, and a journal bearing where the shaft rides on an oil wedge
image_credit: Diagram: Engine-X
model: turbo
keywords: types of bearings, ball bearing vs roller bearing, how does a journal bearing work, bearing L10 life calculation, how to choose a bearing
tldr: Pick a bearing by load and speed — ball bearings for light, fast duty, roller bearings for heavy radial or combined loads, and oil-film journal bearings for the biggest, fastest machines — then check its L10 life.
takeaways:
- Ball bearings touch the races at points: low friction, high speed, moderate load.
- Roller bearings touch along lines: higher load capacity and stiffness than ball bearings of similar size.
- Tapered and spherical rollers carry combined radial and axial loads; spherical ones also tolerate misalignment.
- Journal bearings float the shaft on an oil wedge — no metal contact once running — and suit large engines and turbines.
- L10 life = (C/P)^p million revolutions; doubling the load on a ball bearing cuts its life to one-eighth.
faq:
- What is the difference between ball and roller bearings? | Ball bearings make point contact with their races, so they run fast with low friction, while roller bearings make line contact, which gives higher load capacity, stiffness and shock resistance.
- How does a journal bearing work? | A journal bearing works by the turning shaft dragging oil into a narrowing gap, forming a pressurised oil wedge that lifts the shaft off the bearing surface so the metal parts do not touch while running.
- What is L10 bearing life? | L10 life is the number of revolutions or hours that 90% of a group of identical bearings will reach or exceed under the same load before fatigue failure.
- Which bearing takes both radial and axial load? | Tapered roller bearings take combined radial and axial load in one direction, and spherical roller bearings take radial and axial load in both directions while tolerating misalignment.
sources:
- Acorn Industrial — SKF roller bearings | https://www.acorn-ind.co.uk/skf/bearings/roller-bearings/
- Savree — Plain bearing | https://savree.com/en/product/plain-bearing/
- PIB Sales — Life calculations for bearings | https://pibsales.com/tutorials/life-calculations-for-bearings/
---
Ball bearings, roller bearings and journal bearings all support a turning shaft, but each does it differently: ball bearings roll on point contacts, roller bearings roll on line contacts, and journal bearings let the shaft slide on a thin film of pressurised oil.

The right choice depends on the load, its direction, the speed and how much space and lubrication the machine has.

Almost every machine on Engine-X depends on bearings. The [turbocharger](https://engx3d.com/turbocharger) spins on oil-fed journal bearings, a [centrifugal pump](https://engx3d.com/centrifugal-pump) carries its impeller shaft on rolling bearings, and the pulleys of a V-belt drive put a constant side load on their shaft bearings.

## What does a bearing actually do?

A bearing lets one part turn relative to another while carrying the load between them with as little friction and wear as possible. The loads come in two directions:

- **Radial load** pushes at right angles to the shaft — for example, the weight of a rotor or the pull of a belt.
- **Axial (thrust) load** pushes along the shaft — for example, the thrust from helical gears, a propeller or a pump impeller.

Most real shafts carry both. The bearing type is chosen to carry the right mix, at the right speed, for long enough.

## How do ball bearings work?

Ball bearings work by placing hardened steel balls between an inner and an outer ring (the races), so the shaft rolls instead of sliding. Each ball touches each race at a very small point, which keeps friction low and lets ball bearings run fast.

The small contact is also the limit: the load is concentrated on tiny areas, so a ball bearing carries less load than a roller bearing of similar size. The common **deep groove ball bearing** takes mainly radial load plus some axial load in either direction, which is why it appears in electric motors, fans and small pumps. **Angular contact ball bearings** have races set at an angle so they take heavier axial load in one direction, and are often fitted in pairs.

## How do roller bearings work, and which type takes which load?

Roller bearings work the same way as ball bearings but use cylinders, cones or barrels instead of balls, so each roller touches the race along a line. [Acorn Industrial](https://www.acorn-ind.co.uk/skf/bearings/roller-bearings/) notes that this line contact gives higher radial load capacity than ball bearings of a similar size, plus more stiffness and shock resistance. The roller shape decides which loads the bearing can take:

| Roller bearing type | Loads | Special feature | Typical uses |
|---|---|---|---|
| Cylindrical roller | High radial load | Some designs allow axial movement of the shaft | Electric motors, gearboxes, machine tools |
| Tapered roller | Combined radial + axial, one direction (pairs for both) | Cone-shaped rollers | Wheel hubs, gearboxes, heavy machinery |
| Spherical roller | Radial + axial, both directions | Tolerates shaft misalignment | Conveyors, mining equipment, paper machines |
| Needle roller | High radial load in a small space | Very thin rollers | Transmissions, compressors, small gearboxes |

Spherical roller bearings deserve a special note. Their outer race is part of a sphere, so the inner ring, rollers and shaft can tilt slightly without loading the rollers on their edges. That makes them forgiving on long shafts that bend or on housings that are hard to align perfectly.

## How does a journal bearing work?

A journal bearing works by letting the shaft (the journal) turn inside a smooth sleeve with a thin gap filled with oil. As the shaft spins, it drags oil into the narrowing part of the gap, and [Savree](https://savree.com/en/product/plain-bearing/) describes how this forms an **oil wedge** between the surfaces. The wedge builds enough pressure to lift the shaft, so once it is running the metal parts are separated by oil and do not touch.

Journal bearings have no rolling parts, so they run quietly, and they can be made in two halves, which is the only practical way to fit a bearing around a crankshaft. Savree notes they are used in large machinery such as steam turbines and large marine two-stroke engines, as well as almost all internal combustion engines. The lining is usually a soft white metal (Babbitt) that is designed to wear before the expensive shaft does.

Their weak moment is starting and stopping. At low speed there is no oil wedge yet, and Savree states that start-up wear is usually greater than the wear over the whole running period. That is why large engines prime the bearings with pumped oil before they turn.

## How is bearing life calculated?

Rolling-bearing life is calculated with the **L10 formula**, explained by [PIB Sales](https://pibsales.com/tutorials/life-calculations-for-bearings/):

**L10 = (C / P)^p × 10⁶ revolutions**

- **C** is the bearing's dynamic load rating from the maker's catalogue.
- **P** is the equivalent load on the bearing.
- **p** is 3 for ball bearings and 10/3 for roller bearings.
- **L10** is the life that 90% of identical bearings will reach before fatigue failure.

PIB's example: a ball bearing with C = 10,000 N under P = 2,000 N gives (5)³ = 125 million revolutions. At 1,000 rpm that is about 2,083 hours. The exponent is the lesson: because life goes with the **cube** of the load ratio, doubling the load on a ball bearing cuts its life to one-eighth. Overloading a bearing a little costs a lot of life.

PIB also stresses that L10 is an ideal figure. Poor lubrication, dirt, misalignment and heat can shorten real life far more than the load does.

## The engineering takeaway

Choose the bearing by the load first — light and fast means balls, heavy or combined means rollers, very large or very fast means an oil-film journal bearing — then check its L10 life at the real load. After that, the bearing's life depends on what the formula ignores: clean oil, correct fit, good alignment and controlled temperature. The same thrust loads that [helical and worm gears](https://engx3d.com/blog/posts/2026-10-23-gear-types-spur-helical-bevel-worm.html) create are a common reason for picking tapered or angular contact bearings.
