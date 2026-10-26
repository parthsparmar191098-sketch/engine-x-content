---
title: Pump Cavitation and NPSH Explained — Why a Pump Sounds Like Gravel
date: 2026-10-22
category: guide
summary: Cavitation is when liquid boils inside a pump and the bubbles collapse on the impeller. How NPSH available and NPSH required decide whether it happens, with a worked example.
seo_title: Pump Cavitation and NPSH Explained, With an Example
seo_description: What pump cavitation is, why it sounds like gravel, and how NPSH available vs NPSH required decide if it happens. Includes a worked example.
image: assets/2026-10-22-pump-cavitation-npsh.svg
image_alt: Diagram of a pump drawing water from a tank below it, showing how atmospheric pressure, suction lift, friction and vapour pressure add up to NPSH available
image_credit: Diagram: Engine-X
model: pump
keywords: pump cavitation, what is NPSH, NPSHa vs NPSHr, how to calculate NPSH available, centrifugal pump cavitation causes
tldr: A centrifugal pump stays free of cavitation only when the system gives more suction head (NPSHa) than the pump needs (NPSHr), with a healthy margin on top.
takeaways:
- Cavitation is liquid turning to vapour at the impeller eye, then the bubbles collapsing and hammering the metal.
- NPSHa is what the suction system supplies; NPSHr is what the pump needs, set by the maker from tests.
- NPSHa = pressure head ± static head − friction − vapour pressure head (+ a small velocity head).
- Hot liquid, high suction lift and narrow or long suction pipes all cut NPSHa.
- A common rule: keep NPSHa above NPSHr by at least about 1 m (3.3 ft) or 10%, whichever is bigger.
faq:
- What is cavitation in a centrifugal pump? | Cavitation is the formation of vapour bubbles where suction pressure drops below the liquid's vapour pressure, followed by their violent collapse inside the impeller, which causes noise, vibration and pitting.
- What is the difference between NPSHa and NPSHr? | NPSHa is the suction head the system actually provides above vapour pressure; NPSHr is the minimum the pump needs, given by the manufacturer from tests. NPSHa must be larger.
- What does NPSH3 mean on a pump curve? | NPSH3 is the suction head at which the pump's head drops by 3% because of cavitation; the Hydraulic Institute has used this test point since 1932.
- How do you stop a pump from cavitating? | Raise NPSHa by lowering the pump or raising the liquid level, using a larger and shorter suction pipe, cooling the liquid, or reducing pump speed and flow.
sources:
- Hydraulic Institute — The basics of NPSH & pump operating regions | https://www.pumps.org/2022/12/07/the-basics-of-npsh-pump-operating-regions/
- Pumps & Systems — Understanding NPSH & its effect on pump selection & setup | https://pumpsandsystems.com/understanding-npsh-its-effect-pump-selection-setup
- Pumps & Systems — How to understand net positive suction head | https://www.pumpsandsystems.com/how-understand-net-positive-suction-head
- Atlas Copco — What is pump cavitation and how to avoid it? | https://atlascopco.com/en-us/construction-equipment/resources/blog/cavitation-in-centrifugal-pump
---
Pump cavitation is the formation of vapour bubbles inside a pump when the pressure at the impeller inlet falls below the liquid's vapour pressure, followed by the bubbles collapsing as pressure rises again. Whether a centrifugal pump cavitates depends on one comparison: the suction head the system supplies (NPSHa) against the suction head the pump needs (NPSHr).

The warning signs are hard to miss. [Atlas Copco](https://atlascopco.com/en-us/construction-equipment/resources/blog/cavitation-in-centrifugal-pump) describes a noise like rocks being pumped, heavy vibration and falling performance. If you want to see where the impeller eye and volute sit before reading on, the [Engine-X centrifugal pump guide](https://engx3d.com/centrifugal-pump) shows the parts in 3D.

## Why does a centrifugal pump cavitate?

A centrifugal pump cavitates because the lowest pressure in the whole system sits right at the impeller eye, where the liquid enters the vanes. Liquid speeds up as it enters the impeller, and faster liquid has lower static pressure. If that pressure drops below the liquid's vapour pressure at its temperature, the liquid boils — even if it is only cold water.

The damage happens a moment later. The impeller then raises the pressure, and the vapour bubbles collapse almost instantly. Each collapse sends a small, sharp pressure shock into the nearby metal. Repeated millions of times, those jets cause pitting, cracking and chipping of the impeller, and the vibration that comes with them wears seals and bearings early, as Atlas Copco notes.

## What is NPSH available (NPSHa)?

NPSH available (NPSHa) is the total head at the pump suction, in absolute terms, above the vapour pressure of the liquid. NPSH stands for *net positive suction head*. NPSHa is a property of the system — the tank, the pipes and the liquid — not of the pump. [Pumps & Systems](https://pumpsandsystems.com/understanding-npsh-its-effect-pump-selection-setup) breaks it into five terms:

1. **Pressure head on the liquid surface.** For an open tank this is atmospheric pressure. At sea level, 14.7 psi equals about 34 ft, or roughly **10.3 m of water**.
2. **Static head.** Added when the liquid level is above the pump centreline (flooded suction), subtracted when the pump sits above the liquid (suction lift).
3. **Friction losses.** Subtracted. Longer pipes, smaller diameters, more bends and valves, and higher flow all increase them.
4. **Velocity head** at the suction port. Added, but usually small.
5. **Vapour pressure head** of the liquid at its pumping temperature. Subtracted. Hotter liquid has a higher vapour pressure, so the same system gives less NPSHa.

## What is NPSH required (NPSHr) and NPSH3?

NPSH required (NPSHr) is the minimum suction head a pump needs to run at a given flow and speed, set by the manufacturer from test data. In practice, pump curves usually plot **NPSH3**: the NPSHa at which the pump's head drops by 3% because of cavitation. According to the [Hydraulic Institute](https://www.pumps.org/2022/12/07/the-basics-of-npsh-pump-operating-regions/), this definition dates from 1932, when a 3% drop was the smallest change that could be measured reliably.

The key point engineers miss is that NPSH3 is *not* a cavitation-free point. At NPSH3 the pump is already cavitating enough to lose 3% of its head, and bubbles start forming at higher suction pressures than that. The Hydraulic Institute adds that today's faster, higher-energy pumps often need a bigger margin above NPSH3 to reach an acceptable life.

## How do you calculate NPSH available? A worked example

NPSH available is calculated by adding up the five terms for the actual installation. Take a pump drawing cold water (about 20 °C) from an open tank at sea level:

| Term | Value |
|---|---|
| Atmospheric pressure head | +10.35 m |
| Suction lift (pump 3 m above water level) | −3.00 m |
| Friction loss in suction pipe and fittings | −1.00 m |
| Vapour pressure head of water at ~20 °C (0.34 psia) | −0.24 m |
| Velocity head (ignored here) | ≈ 0 |
| **NPSHa** | **≈ 6.1 m** |

If the pump curve shows NPSH3 = 4.0 m at the duty flow, the margin is about 2.1 m. Pumps & Systems gives a common rule of thumb: a margin of at least 3.3 ft (about 1 m) or 10% of NPSHa, whichever is greater. Here that means at least 1 m, so this installation passes.

Now move the same pump 3 m higher, to a 6 m suction lift. NPSHa falls to about 3.1 m — below the 4.0 m NPSH3 — and the pump will cavitate badly. Nothing about the pump changed; only the system did.

## How do you stop a pump from cavitating?

You stop a pump from cavitating by raising NPSHa, lowering NPSHr, or both:

- **Lower the pump or raise the liquid level** to cut suction lift, or give it a flooded suction.
- **Make the suction pipe larger and shorter**, with fewer bends and fully open valves. A partly closed suction valve is a classic cause.
- **Clean suction strainers and filters**, since a clogged strainer adds friction loss.
- **Cool the liquid** or pressurise the tank when pumping hot liquids.
- **Reduce speed or flow**, as Atlas Copco suggests, and run the pump near its best efficiency point (BEP). The Hydraulic Institute notes that running outside the preferred operating region increases the NPSH margin a pump needs.

## The engineering takeaway

Cavitation is a system problem that shows up as pump damage. The impeller only fails where the suction side is starved, so the fix is usually in the piping, the liquid level or the temperature, not in replacing the pump. Before blaming a noisy pump, add up NPSHa and compare it with the NPSH3 on the curve — with a margin. For the bigger picture of when a different pump type suits better, see [centrifugal vs positive displacement pumps](https://engx3d.com/centrifugal-vs-positive-displacement-pump), and for another machine that lives on its intake conditions, read how a [ship's turbocharger feeds a two-stroke engine](https://engx3d.com/blog/posts/2026-10-21-ship-turbocharger-two-stroke.html).
