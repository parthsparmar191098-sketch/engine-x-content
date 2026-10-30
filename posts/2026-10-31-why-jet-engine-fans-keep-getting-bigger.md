---
title: CFM56 vs LEAP vs Geared Turbofan: Why Jet Engine Fans Keep Getting Bigger
date: 2026-10-31
category: comparison
summary: Airliner engines keep growing bigger fans and higher bypass ratios. Why moving more air more slowly saves fuel, how CFM56, LEAP and the geared turbofan compare, and what limits the fan.
seo_title: Why Jet Engine Fans Keep Getting Bigger: Bypass Ratio
seo_description: Why a bigger fan and higher bypass ratio save fuel, how the CFM56, LEAP and Pratt & Whitney geared turbofan compare, and why the fan needs a gearbox.
image: assets/2026-10-31-turbofan-bypass-ratio.svg
image_alt: Diagram comparing three turbofans side by side — a CFM56-7B with a 61-inch fan and bypass ratio about 5 to 1, a LEAP-1A with a 78-inch fan and 11 to 1, and a geared turbofan with a fan gearbox and about 12 to 1 — with arrows showing bypass air around the core
image_credit: Diagram: Engine-X
model: turbofan
keywords: why are jet engine fans getting bigger, what is bypass ratio, CFM56 vs LEAP, how does a geared turbofan work, high bypass turbofan efficiency
tldr: A bigger fan moves more air more slowly, which wastes less energy in the exhaust jet, so high-bypass engines burn less fuel. The CFM56-7B runs about 5 : 1 bypass, the LEAP-1A 11 : 1 and the geared PW1100G about 12 : 1; the gearbox lets a huge fan turn slowly while its turbine spins fast.
takeaways:
- Thrust comes from speeding up air; speeding up a lot of air a little wastes less energy than a little air a lot.
- Bypass ratio is the air going around the core divided by the air going through it.
- CFM56-7B: 61-inch fan, about 5 : 1. LEAP-1A: 78-inch fan, 11 : 1, about 15% less fuel.
- A geared turbofan puts a roughly 3 : 1 gearbox between the fan and its turbine, reaching about 12 : 1 bypass.
- Fan tip speed, engine weight, nacelle drag and ground clearance limit how big a fan can get.
faq:
- What is bypass ratio in a jet engine? | Bypass ratio is the mass of air that flows around the engine core through the fan duct divided by the mass that flows through the core. The CFM56-7B is about 5 : 1, so roughly five kilograms of air bypass the core for every kilogram that is burned with fuel.
- Why do bigger fans save fuel? | A jet engine makes thrust by speeding air up. Moving a large mass of air a little faster gives the same thrust as moving a small mass much faster, but leaves far less kinetic energy wasted in the exhaust, so less fuel is burned for the same push.
- Why does a geared turbofan need a gearbox? | A very large fan must turn slowly to keep its blade tips below supersonic speed, while the low-pressure turbine that drives it works best spinning fast. A roughly 3 : 1 gearbox lets each run at its own best speed, so the turbine needs fewer stages.
- Is a higher bypass ratio always better? | No. A bigger fan means a heavier engine, a larger nacelle with more drag and less clearance under the wing. Fighter jets use low bypass ratios because they need high exhaust speed for supersonic flight.
sources:
- NASA Glenn Research Center — Turbofan engine | https://www.grc.nasa.gov/www/k-12/BGP/aturbf.html
- NASA Glenn Research Center — Turbofan thrust | https://www.grc.nasa.gov/www/k-12/BGP/turbfan.html
- EASA — Type-Certificate Data Sheet E.004, CFM56-7B series | https://www.easa.europa.eu/en/downloads/7795/en
- Aircraft Commerce — CFM56-7B specifications | https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Aircraft%20guides/CFM56-7B/ISSUE58_CFM56_7B_SPECS.pdf
- Aerospace Manufacturing — CFM International LEAP engine | https://www.aero-mag.com/cfm-international-leap-engine-high-bypass-turbofan-engine
- Wikipedia — CFM International LEAP | https://en.wikipedia.org/wiki/CFM_International_LEAP
- Wikipedia — Pratt & Whitney PW1000G | https://en.wikipedia.org/wiki/PW1000G
- Wikipedia — Geared turbofan | https://en.wikipedia.org/wiki/Geared_turbofan
- Engine-X — Turbofan jet engine 3D model | https://engx3d.com/3d-models/turbofan-engine
---
Jet engine fans keep getting bigger because a bigger fan moves more air more slowly, and that is the cheapest way to make thrust. The CFM56-7B has a 61-inch fan and about 5 : 1 bypass, the LEAP-1A a 78-inch fan and 11 : 1, and Pratt & Whitney's geared turbofan about 12 : 1.

You can see where the bypass air goes in the new [Engine-X turbofan 3D model](https://engx3d.com/3d-models/turbofan-engine), built in the CFM56-7B style, and the [turbofan guide](https://engx3d.com/turbofan-engine) walks through every stage from the fan to the exhaust.

## Why does moving more air save fuel?

Every jet engine makes thrust the same way: it pushes air backwards faster than it came in. The thrust depends on how much air it moves and how much it speeds that air up. The fuel cost depends on the energy left behind in the exhaust jet, and that energy grows with the **square** of the jet speed.

So there are two ways to get the same thrust:

1. **A little air, very fast.** A turbojet pushes all its air through the core and blasts it out at high speed. Lots of energy is wasted in that fast jet.
2. **A lot of air, a little faster.** A turbofan's big fan gives a huge mass of air a gentle push. Same thrust, much less wasted energy, so less fuel.

NASA puts it simply: because the core's fuel flow barely changes when a fan is added, a turbofan gets more thrust for nearly the same fuel ([NASA Glenn](https://www.grc.nasa.gov/www/k-12/BGP/aturbf.html)). That is why high-bypass engines are nearly as efficient as turboprops while still flying at airliner speeds.

## What is bypass ratio?

Bypass ratio is the air that goes **around** the core divided by the air that goes **through** it. Behind the fan, a ring called the splitter divides the flow.

On the CFM56-7B about five parts go down the bypass duct for every one that enters the core, where it is compressed about 32 times, burned with fuel and expanded through the turbines ([EASA TCDS E.004](https://www.easa.europa.eu/en/downloads/7795/en), [Aircraft Commerce](https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Aircraft%20guides/CFM56-7B/ISSUE58_CFM56_7B_SPECS.pdf)). The cool bypass stream gives most of the take-off thrust.

## CFM56 vs LEAP vs geared turbofan compared

| Engine (aircraft) | Fan | Bypass ratio | Fuel burn vs older engines | How the fan is driven |
|---|---|---|---|---|
| CFM56-7B (Boeing 737 NG) | 61 in (1,549 mm), 24 titanium blades | about 5.1–5.5 : 1 | baseline | Directly by a 4-stage LP turbine |
| LEAP-1A (Airbus A320neo) | 78 in (198 cm), 18 woven carbon composite blades | 11 : 1 | about 15% lower than the CFM56 | Directly by the LP turbine |
| PW1100G GTF (Airbus A320neo) | large, slow-turning fan | about 12.2 : 1 | about 16% lower than the previous generation | Through a roughly 3 : 1 planetary gearbox |

Sources: [EASA](https://www.easa.europa.eu/en/downloads/7795/en), [Aircraft Commerce](https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Aircraft%20guides/CFM56-7B/ISSUE58_CFM56_7B_SPECS.pdf), [Aerospace Manufacturing](https://www.aero-mag.com/cfm-international-leap-engine-high-bypass-turbofan-engine), [Wikipedia LEAP](https://en.wikipedia.org/wiki/CFM_International_LEAP), [Wikipedia PW1000G](https://en.wikipedia.org/wiki/PW1000G).

The LEAP's 18 composite blades are 25% fewer than the CFM56-7B's 24, and CFM says the new fan delivers nearly half of the engine's roughly 15% fuel saving ([Aerospace Manufacturing](https://www.aero-mag.com/cfm-international-leap-engine-high-bypass-turbofan-engine)). Pratt & Whitney claims about 16% lower fuel burn for the geared turbofan than the previous generation ([Wikipedia PW1000G](https://en.wikipedia.org/wiki/PW1000G)).

## Why does a geared turbofan need a gearbox?

A geared turbofan needs a gearbox because a big fan and its turbine want opposite speeds. The fan blade tips must stay below about the speed of sound, so the bigger the fan, the slower it has to turn. The low-pressure turbine that drives it works best spinning fast; slowed to fan speed, it needs extra stages.

In a direct-drive engine like the CFM56 the fan and LP turbine share one shaft, so the designer compromises. The geared turbofan puts a planetary gearbox of about 3 : 1 between them: the fan turns roughly 4,000–5,000 rpm while the LP spool turns roughly 12,000–15,000 rpm ([Wikipedia PW1000G](https://en.wikipedia.org/wiki/PW1000G)). The gearbox is the same planetary idea used in industrial reducers, explained in [helical vs worm gear reducers](https://engx3d.com/blog/posts/2026-10-29-helical-vs-worm-gear-reducer.html) ([Wikipedia: Geared turbofan](https://en.wikipedia.org/wiki/Geared_turbofan)).

## What stops fans getting even bigger?

The fan cannot grow forever. Four things push back:

- **Weight.** A bigger fan needs a bigger case, a bigger nacelle and more structure.
- **Drag.** The nacelle's wetted area grows with the fan, eating into the fuel saving.
- **Ground clearance.** Under-wing engines need room above the runway; a tall fan needs taller landing gear or a new wing.
- **Tip speed.** Without a gearbox, a larger fan forces a slower, heavier LP turbine.

Fighter jets show the other end: they use low-bypass turbofans with afterburners because supersonic flight needs a fast exhaust jet ([NASA Glenn](https://www.grc.nasa.gov/www/k-12/BGP/aturbf.html)). The same trade between gas speed and wasted energy shows up in the turbines on ships, covered in [why ship engines use turbochargers](https://engx3d.com/blog/posts/2026-10-21-ship-turbocharger-two-stroke.html).

## The engineering takeaway

Thrust is mass flow times the change in speed, but fuel burned follows the energy wasted in the jet. Bigger fans move more air more gently, so bypass ratio has climbed from about 5 : 1 on the CFM56-7B to 11 : 1 on the LEAP-1A and about 12 : 1 on the geared turbofan. The limits are weight, drag, clearance and tip speed, and the gearbox is how engineers buy a little more fan without paying for it in the turbine.
