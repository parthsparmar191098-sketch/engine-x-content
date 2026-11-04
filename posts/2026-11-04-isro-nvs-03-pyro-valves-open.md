---
title: Why ISRO Launched NVS-03 With Its Pyro Valves Already Open
date: 2026-11-04
category: news
tag: space
summary: NVS-02 was stranded because one valve never opened. For NVS-03, launched on 30 October 2026, ISRO fired its pyro valves on the ground. How pyro valves work and what that trade-off means.
seo_title: Why ISRO Flew NVS-03 With Pyro Valves Open
seo_description: NVS-02 failed when a pyro valve never got its firing signal. Why ISRO launched NVS-03 with the valves already open, and the leak risk that trade-off brings.
image: assets/2026-11-04-nvs-03-pyro-valves.svg
image_alt: Diagram of a satellite propellant line: oxidiser tank, pyro valve, latch valve and orbit-raising engine; NVS-02 had the pyro valve closed and its firing signal never arrived, NVS-03 flew with the pyro valves already open so only the latch valve has to work
image_credit: Diagram: Engine-X
keywords: NVS-03 pyro valves open, NVS-02 failure reason, what is a pyro valve, GSLV-F18 NVS-03, ISRO NavIC satellite launch
tldr: ISRO removed the step that killed NVS-02, the in-space firing of a one-shot pyro valve, by opening the valves before launch, and now relies on a re-closable latch valve to hold the propellant back.
takeaways:
- GSLV-F18 placed NVS-03 in its transfer orbit on 30 October 2026.
- NVS-02 got stuck in 2025 because the firing signal never reached a pyro valve on the oxidiser line.
- A pyro valve is a one-shot valve opened by a small explosive charge; it cannot be closed again.
- For NVS-03, ISRO flew with three pyro valves already open, after shock and vibration tests.
- The trade-off: no firing command needed in space, but the latch valve downstream must now hold back the propellant on its own.
faq:
- Why did NVS-02 fail? | NVS-02 reached its transfer orbit in January 2025, but the drive signal never reached the pyro valve on the oxidiser line of its orbit-raising engine, so the engine could not fire. ISRO's committee found the most likely cause was a contact that came loose in a connector, in both the main and the backup path.
- What is a pyro valve on a satellite? | A pyro valve is a single-use valve that keeps propellant sealed until a small explosive charge is fired electrically to open it. Once opened, it cannot be closed again.
- Why did ISRO launch NVS-03 with pyro valves open? | Opening the valves on the ground removes the in-space firing step that failed on NVS-02. ISRO says a committee approved the change after vibration and shock tests.
- What is the risk of launching with pyro valves open? | Propellant is then held back only by the downstream latch valve, so that valve must not leak during ground work and the shaking of launch, and must open in space when commanded.
sources:
- ISRO — NVS-02 spacecraft: on-orbit observations and Apex Committee recommendations | https://www.isro.gov.in/ISRO_EN/NVS-02-Spacecraft-On-Orbit-Observations.html
- ISRO — GSLV-F18/NVS-03 mission | https://www.isro.gov.in/Mission_GSLVF18.html
- The Federal — NVS-03 to fly with pyro valves open as ISRO seeks to avert repeat failure | https://thefederal.com/category/science/nvs03-to-fly-with-pyro-valves-open-as-isro-seeks-to-avert-repeat-failure-260902
- The Week — ISRO reveals the tiny glitch that doomed the NVS-02 | https://www.theweek.in/news/sci-tech/2026/02/26/isro-reveals-the-tiny-glitch-that-doomed-the-nvs-02.html
- Fact Net — ISRO chief explains three-pyro-valve decision behind NVS-03 launch success | https://www.fact.net.in/leisure/tech/isro-chief-explains-three-pyro-valve-decision-behind-nvs-03-launch-success
- Eurasia Review — Success of NVS-03: why India needs to rethink its satellite navigation strategy | https://eurasiareview.com/04112026-success-of-nvs-03-why-india-needs-to-rethink-its-satellite-navigation-strategy-analysis
---
ISRO launched the NVS-03 navigation satellite on 30 October 2026 with three of its pyro valves already open. Its sister satellite NVS-02 was stranded in 2025 because the firing signal never reached one pyro valve on the oxidiser line. Opening the valves on the ground removes that step, but leaves a latch valve to hold the propellant back on its own.

[ISRO's GSLV-F18](https://www.isro.gov.in/Mission_GSLVF18.html), the 20th flight of the GSLV, placed NVS-03 in its geosynchronous transfer orbit from Sriharikota. NVS-03 is the third of ISRO's next-generation NavIC satellites, adding an L1 signal to the existing L5 and S-band signals. The launch matters because, as [Eurasia Review](https://eurasiareview.com/04112026-success-of-nvs-03-why-india-needs-to-rethink-its-satellite-navigation-strategy-analysis) notes from a July 2026 statement in Parliament, only three NavIC satellites were working, one short of the four needed for standalone positioning.

## What went wrong with NVS-02?

NVS-02 failed because its orbit-raising engine never got oxidiser. The satellite reached a 170 × 37,785 km transfer orbit on 29 January 2025 and deployed its solar panels normally. But [ISRO's Apex Committee](https://www.isro.gov.in/ISRO_EN/NVS-02-Spacecraft-On-Orbit-Observations.html) found that the drive signal did not reach the pyro valve on the oxidiser line of that engine.

The most likely cause, the committee said, was the disengagement of at least one contact in a connector, in both the main and the redundant path. In other words, the backup failed for the same reason as the main line. Without oxidiser the engine could not fire, so NVS-02 is still stuck in its transfer orbit, [The Week](https://www.theweek.in/news/sci-tech/2026/02/26/isro-reveals-the-tiny-glitch-that-doomed-the-nvs-02.html) reports.

## How does a pyro valve work?

A pyro valve is a single-use valve that keeps a propellant line sealed until a small explosive charge is fired electrically to open it. [The Federal](https://thefederal.com/category/science/nvs03-to-fly-with-pyro-valves-open-as-isro-seeks-to-avert-repeat-failure-260902) explains that once it fires, it cannot be closed again.

That makes pyro valves very good seals for launch: the propellant stays locked in its tank through ground handling and the violent ride to orbit. A latch valve is different: it can be commanded open and closed again during the mission. A typical satellite line therefore has both:

| Valve | How it opens | Can it close again? | Job |
|---|---|---|---|
| Pyro valve | Small explosive charge, fired by an electrical signal | No, one shot | Seal the propellant until the mission starts |
| Latch valve | Electrical command | Yes | Turn the flow on and off during the mission |

The same idea of "isolation first, then control" shows up on any ship or plant pipeline: a positive shut-off valve isolates the line and a second valve controls the flow, as in our guide to [gate, globe, butterfly and check valves](https://engx3d.com/blog/posts/2026-10-27-gate-globe-butterfly-check-valves.html).

## Why fly with the valves already open?

Flying with the pyro valves already open removes the step that failed on NVS-02: the electrical firing command in space. If the valve is open before launch, a loose connector cannot keep it shut.

[Fact Net](https://www.fact.net.in/leisure/tech/isro-chief-explains-three-pyro-valve-decision-behind-nvs-03-launch-success) reports ISRO chairman V. Narayanan saying the satellite flew with three pyro valves already open, and that a national committee chaired by former ISRO chief A. S. Kiran Kumar approved the decision after vibration and shock testing. He also gave the injection accuracy: perigee 170.31 km against a planned 170.36 km.

The trade-off, The Federal points out, is that the propellant is now held back only by the downstream isolation latch valve:

1. With the pyro valve open, any leakage collects at the latch valve, which now has to seal on its own.
2. The spacecraft has to stay in that state through ground operations and the vibration and acceleration of the GSLV ascent.
3. If the latch valve then fails to open in space, the mission is lost anyway.

ISRO has swapped one single point of failure (the firing signal) for a different one (the latch valve), and judged the second one safer after testing.

## The engineering takeaway

NVS-02 was lost not to a big engine failure but to one connector contact, which knocked out the main and backup firing paths together. For NVS-03, ISRO removed that step by opening the one-shot pyro valves on the ground. Whether the trade worked will show in the coming orbit-raising burns. The lesson for any engineer is the same one used in pressure testing and valve inspection: redundancy only helps when the backup does not share the weak point. Our [hydrostatic pressure testing guide](https://engx3d.com/blog/posts/2026-10-24-hydrostatic-pressure-testing.html) shows how a sealed line is proved before it goes into service.
