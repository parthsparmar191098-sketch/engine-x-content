---
title: Spur, Helical, Bevel or Worm? How to Choose the Right Gear Type
date: 2026-10-23
updated: 2026-10-26
category: comparison
summary: Spur, helical, bevel and worm gears each suit a different shaft layout, load and noise level. How each gear works, its trade-offs, and when engineers pick it.
seo_title: Spur, Helical, Bevel or Worm Gear? How to Choose
seo_description: How spur, helical, bevel and worm gears work, which shaft layout, load and noise level each suits, and when engineers pick each one.
image: assets/2026-10-23-gear-types.svg
image_alt: Diagram comparing spur, helical, bevel and worm gears by shaft layout, with notes on noise, thrust and efficiency
image_credit: Diagram: Engine-X
keywords: types of gears, spur vs helical gear, what is a bevel gear, worm gear self locking, how to choose a gear type
tldr: Choose a gear by its shafts first — parallel (spur or helical), intersecting (bevel) or crossed at right angles (worm) — then by noise, load, thrust and efficiency.
takeaways:
- Shaft layout decides the family: parallel shafts use spur or helical gears, intersecting shafts use bevel gears, crossed shafts use worm gears.
- Spur gears are simple and efficient but get loud at high speed.
- Helical gears run quieter and carry more load, but push the shaft sideways (axial thrust).
- Worm gears give huge reductions in one step and can self-lock, but lose more power to sliding.
- Bigger thrust or sliding loads mean the bearings must be chosen for them.
faq:
- What is the difference between spur and helical gears? | Spur gears have straight teeth parallel to the shaft and engage all at once; helical gears have angled teeth that engage gradually, so they are quieter and carry more load but create axial thrust.
- Why are worm gears self-locking? | A worm gear self-locks when the friction angle between worm and wheel is bigger than the worm's lead angle, so the wheel cannot turn the worm backwards.
- What is the gear ratio of a worm gear? | The ratio is the number of teeth on the worm wheel divided by the number of starts on the worm, so a 40-tooth wheel with a single-start worm gives 40:1.
- When are bevel gears used? | Bevel gears are used when two shafts meet at an angle, usually 90°, such as in vehicle differentials and right-angle drives.
sources:
- MISUMI USA — 5 different types of gears and their applications | https://blog.misumiusa.com/5-different-types-of-gears-their-applications/
- Interesting Engineering — A guide to gears: 7 gears, their traits and how they work | https://interestingengineering.com/science/a-guide-to-gears-7-gears-their-traits-and-how-they-work
- Gear Solutions — Comparative analysis of spur and helical gears | https://gearsolutions.com/features/comparative-analysis-of-spur-and-helical-gears/
- FIRGELLI — Worm gear reduction & self-locking calculator | https://www.firgelliauto.com/blogs/engineering-calculators/worm-gear-reduction-self-locking-calculator
- MechRef — Spur gears | https://www.mechref.org/mf/Spur_Gears
---
The right gear type depends first on how the two shafts sit: spur and helical gears connect parallel shafts, bevel gears connect shafts that meet at an angle, and worm gears connect shafts that cross at right angles without meeting.

After that, the choice comes down to noise, load, side thrust on the bearings and how much power you can afford to lose.

Gears do the same job as belts and chains — carry power from one shaft to another at a new speed — but with teeth instead of friction, so they never slip. The [belt vs chain vs gear drive comparison](https://engx3d.com/belt-vs-chain-vs-gear-drive) on Engine-X covers when gears beat the other two. This guide goes one level deeper: which gear.

## How does a gear change speed and torque?

A gear pair changes speed and torque through its tooth ratio. When a small gear (the pinion) drives a larger gear, the larger gear turns slower and with more torque, because the teeth must pass the contact point at the same rate on both.

A 20-tooth pinion driving a 60-tooth gear gives a 3:1 reduction: one-third the speed, about three times the torque (minus losses).

Every gear type below follows this rule. What changes is the shape of the teeth and the direction the shafts point.

## What are spur gears and when are they used?

Spur gears are gears with straight teeth cut parallel to the shaft, and they connect parallel shafts. They are the simplest gears to make accurately, and [MISUMI](https://blog.misumiusa.com/5-different-types-of-gears-their-applications/) notes they are efficient, with minimal power lost to slippage.

The weakness is noise. Each spur tooth comes into contact across its whole width at once, so every engagement is a small impact. At high speed those impacts add up to a loud whine. Spur gears also push no load along the shaft (no axial thrust), which keeps the bearings simple. A design note from [MechRef](https://www.mechref.org/mf/Spur_Gears): with the common 20° pressure angle, a pinion should have at least about 18 teeth to avoid problems with tooth shape.

**Typical uses:** simple gear trains, pumps, hand tools, and machines where speed is moderate and cost matters.

## Why are helical gears quieter than spur gears?

Helical gears are quieter than spur gears because their teeth are cut at an angle to the shaft, so each tooth enters contact gradually, from one end to the other, instead of all at once.

More than one tooth also shares the load at any moment. [Gear Solutions](https://gearsolutions.com/features/comparative-analysis-of-spur-and-helical-gears/) explains this as an extra "overlap" contact ratio that spur gears do not have, which gives helical gears lower noise and vibration and higher load capacity.

The price is **axial thrust**. Because the teeth are angled, they push the shaft sideways along its axis as well as turning it. Interesting Engineering notes that helical gears therefore need thrust bearings, and MISUMI adds that sliding along the angled teeth makes them slightly less efficient than spur gears. Double-helical (herringbone) gears cancel this thrust by using two opposite helices side by side.

**Typical uses:** industrial gearboxes, vehicle transmissions, marine reduction gearboxes and anything that runs fast and needs to be quiet.

## What are bevel gears used for?

Bevel gears are cone-shaped gears that connect two shafts which intersect, most commonly at 90°. They turn the drive around a corner. [Interesting Engineering](https://interestingengineering.com/science/a-guide-to-gears-7-gears-their-traits-and-how-they-work) gives the classic example: the vehicle differential, which lets two wheels on one axle turn at different speeds through a corner.

Straight bevel gears behave like spur gears — simple but noisy. **Spiral bevel gears** have curved teeth that engage gradually, like helical gears, so they are stronger and quieter, but they are harder to make and create axial thrust. MISUMI notes that spiral bevel gears should be bought as matched pairs, since they mesh reliably only with gears from the same maker.

**Typical uses:** differentials, right-angle gearboxes, hand drills, and power take-offs.

## How does a worm gear work, and why is it self-locking?

A worm gear works like a screw turning a toothed wheel: the worm (a threaded shaft) meshes with the worm wheel at right angles. Each turn of a single-start worm moves the wheel by just one tooth, so the [ratio](https://www.firgelliauto.com/blogs/engineering-calculators/worm-gear-reduction-self-locking-calculator) is simply wheel teeth ÷ worm starts. A 40-tooth wheel with a single-start worm gives **40:1** in one compact stage.

FIRGELLI notes single pairs ranging from about 5:1 to well over 300:1.

The worm slides across the wheel teeth rather than rolling, and sliding means friction. That gives worm gears two linked properties:

1. **Lower efficiency.** FIRGELLI gives a range of roughly 30% for strongly self-locking designs up to about 90% for designs that allow back-driving; MechRef quotes 50–90%. The lost power turns into heat in the oil.
2. **Self-locking.** When the friction angle is larger than the worm's lead angle, the wheel cannot drive the worm backwards. The load stays put even with the motor off — useful for hoists, gates and valve actuators. FIRGELLI's example: a friction coefficient of 0.12 gives a friction angle of about 6.8°, so a 5° lead angle self-locks.

Worm gears are quiet, but they also put a high thrust load on the worm shaft, so its bearings must be sized for it.

## Which gear type should you choose?

The gear type you should choose follows from the shaft layout, then the duty:

| Gear type | Shafts | Noise | Axial thrust | Efficiency | Best for |
|---|---|---|---|---|---|
| Spur | Parallel | Loud at speed | None | High | Simple, low-cost, moderate speed |
| Helical | Parallel | Quiet | Yes | High (slightly below spur) | Fast, heavy, quiet drives |
| Bevel (straight / spiral) | Intersecting, often 90° | Loud / quiet | Spiral: yes | High | Turning a drive through an angle |
| Worm | Crossed at 90° | Quiet | High on worm | ~30–90% | Big reduction, holding loads |

## The engineering takeaway

Gear selection is a chain of trade-offs: straight teeth are simple but noisy, angled teeth are quiet but push on the bearings, and sliding teeth give big ratios and self-locking at the cost of heat. Start with the shaft layout, then check speed, noise and whether the load must hold by itself — and always size the bearings for the thrust the gear creates. If a drive keeps slipping or wearing, compare it with how a [V-belt fails from tension and alignment](https://engx3d.com/blog/posts/2026-10-23-v-belt-slip-squeal-failure.html); gears trade that slip for precise alignment and good lubrication.
