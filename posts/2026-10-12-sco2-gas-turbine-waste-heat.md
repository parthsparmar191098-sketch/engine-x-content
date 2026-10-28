---
title: A CO₂ Loop That Squeezes Extra Power From Gas Turbine Exhaust
date: 2026-10-12
updated: 2026-10-26
category: news
tag: machines
summary: A Denver startup says factory-built supercritical CO₂ power blocks can add up to 50% more power to a simple-cycle gas turbine. Here is how a CO₂ loop replaces steam, and what is still unproven.
seo_title: Supercritical CO₂ Loops for Gas Turbine Exhaust Power
seo_description: How a supercritical CO₂ loop replaces steam to turn gas turbine exhaust heat into up to 50% more power, and what is still unproven.
image: assets/2026-10-12-sco2-bottoming-cycle.svg
image_alt: Diagram of a closed supercritical CO2 loop taking heat from gas turbine exhaust, driving a turbine and generator, with a recuperator and a cooler
image_credit: Diagram: Engine-X
keywords: supercritical CO2, sCO2 power cycle, gas turbine waste heat, Brayton cycle, recuperator
tldr: A closed supercritical CO₂ loop can turn gas-turbine exhaust heat into extra power with much smaller machinery than steam, but the startup's 50% claim still needs real operating data.
takeaways:
- Simple-cycle gas turbines send hot exhaust up the stack instead of recovering it.
- Above about 31 °C and 74 bar, CO₂ becomes a dense supercritical fluid, so turbines and heat exchangers can be much smaller than for steam.
- The loop is a closed Brayton cycle: compress, recuperate, heat from exhaust, expand, cool.
- The STEP Demo pilot proved sCO₂ turbomachinery at pilot scale; commercial durability is still the open question.
faq:
- What is supercritical CO₂? | Carbon dioxide above roughly 31 °C and 7.4 MPa, where it is neither a normal liquid nor a gas but a dense fluid that flows like a gas.
- Why use CO₂ instead of steam for waste heat? | Dense CO₂ carries a lot of energy in a small volume, so the turbine, heat exchangers and piping can be much smaller than a steam system.
- Does an sCO₂ bottoming cycle change the gas turbine? | No. It only takes heat from the exhaust through a heat exchanger, so the gas turbine itself is not modified.
sources:
- Turbomachinery Magazine — American Supercritical launches sCO2 power blocks for gas turbine waste heat (6 Oct 2026) | https://www.turbomachinerymag.com/view/american-supercritical-launches-sco-power-blocks-for-gas-turbine-waste-heat
- Interesting Engineering — American Supercritical funding and supercritical CO2 waste heat power (23 Sep 2026) | https://interestingengineering.com/innovation/supercritical-co2-gas-turbine-waste-heat-power
- Pulse 2.0 — American Supercritical raises $8 million pre-seed (24 Sep 2026) | https://pulse2.com/american-supercritical-raises-8-million/
- POWER Magazine — Breakthrough for sCO2 power cycle as STEP Demo completes Phase 1 (9 Oct 2024) | https://www.powermag.com/breakthrough-for-sco2-power-cycle-as-step-demo-completes-phase-1-of-10-mw-project/
- Southwest Research Institute — STEP Demo pilot plant achieves full operational conditions (16 Oct 2024) | https://www.swri.org/press-release/step-demo-pilot-plant-achieves-full-operational-conditions-phase-1-of-testing
---
A Denver startup called **American Supercritical** has come out of stealth with $8 million in pre-seed funding and a simple pitch: bolt a factory-built "power block" onto the exhaust of a simple-cycle gas turbine and make up to **50% more electricity without burning any extra fuel**.

Instead of the usual steam equipment, the block uses carbon dioxide as its working fluid.

Those are the company's own claims, and I could not find published operating data from a commercial installation yet. But the mechanism behind them is real engineering, and it is worth understanding.

## Where does a gas turbine waste heat?

A gas turbine wastes heat in its hot exhaust. A simple-cycle gas turbine sucks in air, compresses it, burns fuel and expands the hot gas through a turbine. After the turbine, the exhaust still leaves at several hundred degrees Celsius.

In a combined-cycle plant, that heat is captured by a heat recovery steam generator (HRSG), which boils water to drive a second, steam turbine. Simple-cycle units skip all that, so the heat goes up the stack. The company says about 140 GW of such turbines operate in the US.

## What is supercritical CO₂?

Supercritical CO₂ is CO₂ held above its critical point, where it is neither a clean liquid nor a gas. Every fluid has a critical point. For CO₂ it is roughly **31 °C and 7.4 MPa** (about 74 bar). Above both, CO₂ is no longer cleanly a liquid or a gas.

It is a dense, compressible fluid that flows like a gas but is far denser than any gas.

That density is the trick. Steam at low pressure is very thin, so steam turbines and condensers must be huge. Dense CO₂ packs a lot of energy into a small volume, so the turbine, heat exchangers and piping shrink. American Supercritical says its block needs about one-tenth the space of a comparable steam system.

## How does an sCO₂ power loop work?

An sCO₂ power loop is a closed Brayton cycle, the same thermodynamic idea as the gas turbine itself, but the CO₂ never leaves the loop:

1. **Compress.** A compressor raises the cooled CO₂ to very high pressure. Because the fluid is dense, close to liquid-like, this takes much less work than compressing a thin gas. Less compression work means more net power at the shaft.
2. **Pre-heat (recuperator).** The compressed CO₂ picks up heat from the turbine's own outlet stream through a heat exchanger. This recycles heat that would otherwise be thrown away.
3. **Heat from the exhaust.** The CO₂ then passes through a heat exchanger in the gas turbine exhaust and rises to the top temperature of the loop.
4. **Expand.** The hot, high-pressure CO₂ spins a turbine connected to a generator.
5. **Cool.** After giving heat to the recuperator, the CO₂ goes through a cooler and returns to the compressor inlet, close to the critical point, and the cycle repeats.

Because the loop only borrows heat from the exhaust stream through a heat exchanger, the gas turbine itself is not changed. The company says no turbine modifications or extra permitting are needed.

## Has sCO₂ power worked at pilot scale?

Yes. The best public evidence is not from the startup. The STEP Demo, a 10 MWe pilot led by GTI Energy at Southwest Research Institute in San Antonio, ran a simple sCO₂ cycle in 2024. Its turbine reached 27,000 rpm at 500 °C and about 250 bar and delivered around 4 MWe to the grid.

The next phase was planned to move to a more efficient recompression cycle at 715 °C. That shows the turbomachinery is real; it does not prove the startup's 50% number.

## The engineering takeaway

From the dry-dock side, my instinct is to ask about the unglamorous parts: seals on a shaft running tens of thousands of rpm, corrosion at 250 bar, and heat exchangers that must survive thermal cycling. Dense, high-pressure fluids are unforgiving when something leaks. The thermodynamics favours CO₂ clearly. Whether it wins depends on how the hardware lasts in the field, and that is where the first real operating data will matter.
