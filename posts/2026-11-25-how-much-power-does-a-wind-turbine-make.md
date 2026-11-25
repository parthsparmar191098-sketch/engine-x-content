---
title: How Much Power Does a Wind Turbine Make? The Formula, Worked on a 5 MW Turbine
date: 2026-11-25
category: learn
summary: Wind power = ½ × air density × swept area × wind speed³ × power coefficient. Worked through on the NREL 5 MW turbine with its 126 m rotor, with a power table from cut-in to cut-out and why the cube law matters so much.
seo_title: How Much Power Does a Wind Turbine Make? (Formula)
seo_description: Wind turbine power = ½ρAv³ × Cp. Worked on a 5 MW turbine with a 126 m rotor: power at each wind speed, the Betz limit and why the cube law matters.
image: assets/2026-11-25-wind-turbine-power-curve.svg
image_alt: Power curve of the NREL 5 MW wind turbine, rising with the cube of wind speed from cut-in at 3 metres per second to 5 megawatts at 11.4 metres per second, then held flat by blade pitch until cut-out at 25 metres per second
image_credit: Diagram: Engine-X
model: windturbine
keywords: how much power does a wind turbine make, wind turbine power formula, wind power calculation, betz limit, wind turbine power curve, power coefficient cp
tldr: A wind turbine's power is half the air density times the swept area times the wind speed cubed, times the power coefficient; a 5 MW turbine with a 126 m rotor makes about 1.8 MW at 8 m/s and its full 5 MW from 11.4 m/s.
takeaways:
- Power in the wind = ½ × ρ × A × v³, with ρ ≈ 1.225 kg/m³ and A = π × radius².
- No rotor can catch more than 59.3 % of it (the Betz limit); good rotors reach about 45–50 %.
- Twice the wind speed gives eight times the power; a 10 % longer blade gives 21 % more.
- The NREL 5 MW turbine makes about 1.8 MW at 8 m/s and 5 MW from 11.4 m/s.
- Above rated wind the blades pitch to hold 5 MW, and above 25 m/s the turbine shuts down.
faq:
- What is the formula for wind turbine power? | Power = ½ × air density × swept area × wind speed³ × power coefficient. With air at 1.225 kg/m³, a 126 m rotor sweeping 12,469 m² and an 8 m/s wind, the wind carries 3.9 MW, and a rotor with a power coefficient of 0.482 catches about 1.9 MW.
- How much power does a 5 MW wind turbine actually make? | It makes 5 MW only in winds of about 11.4 m/s and above. At 8 m/s the NREL 5 MW turbine makes about 1.8 MW, and at 5 m/s less than 0.5 MW, because power falls with the cube of the wind speed.
- What is the Betz limit? | The most power any rotor can take from the wind: 16/27, or 59.3 %. A rotor that stopped the air completely would block the flow, so some speed must be left in the air behind it. Modern large turbines reach peak power coefficients of about 0.45 to 0.50.
- Why do wind turbines have such long blades? | Because power is proportional to the swept area, which grows with the square of the blade length. A blade 10 % longer sweeps 21 % more area and catches 21 % more power at the same wind speed.
- Why does a wind turbine stop in very strong wind? | To protect itself. Above its cut-out speed, 25 m/s on the NREL 5 MW turbine, the loads get too high, so the blades are turned edge-on to the wind, the rotor stops and the brake holds it.
sources:
- NREL turbine models — NREL 5 MW reference turbine | https://nrel.github.io/turbine-models/NREL_5MW_126_RWT.html
- Specification table of the NREL 5 MW turbine (Cp 0.482, 12.1 rpm, 94.4 % efficiency), arXiv 2405.06829 | https://arxiv.org/pdf/2405.06829
- NREL — Definition of a 5-MW Reference Wind Turbine (Jonkman et al., NREL/TP-500-38060) | https://www.nrel.gov/docs/fy09osti/38060.pdf
- UBC Physics — Wind turbines: Betz's law explained | https://c21.phas.ubc.ca/article/wind-turbines-betz-law-explained/
- Wikipedia — Betz's law | https://en.wikipedia.org/wiki/Betz%27s_law
- U.S. Department of Energy — How a wind turbine works | https://www.energy.gov/eere/wind/inside-wind-turbine-0
- Engine-X — Wind turbine nacelle 3D model | https://engx3d.com/3d-models/wind-turbine
---
A wind turbine's power is ½ × air density × swept area × wind speed³ × its power coefficient. For the NREL 5 MW reference turbine, with a 126 m rotor, that is about 1.8 MW at 8 m/s and the full 5 MW from 11.4 m/s. Because of the cube, wind speed matters most.

The numbers below use the turbine in the new [Engine-X wind turbine nacelle 3D model](https://engx3d.com/3d-models/wind-turbine), and the [wind turbine guide](https://engx3d.com/wind-turbine) walks through the gearbox, generator, pitch and yaw systems part by part.

## What is the formula for wind power?

The power carried by the wind through the rotor is ½ × ρ × A × v³, where ρ is the air density, A the swept area and v the wind speed ([UBC Physics](https://c21.phas.ubc.ca/article/wind-turbines-betz-law-explained/)). The rotor only catches a fraction of it, set by its power coefficient Cp:

**Power (W) = ½ × ρ × A × v³ × Cp**

Use ρ = 1.225 kg/m³ for air at sea level and 15 °C, A in m² and v in m/s, and the answer comes out in watts.

## Step 1: work out the swept area

The swept area is the circle the blades sweep: A = π × radius². The NREL 5 MW turbine has a 126 m rotor, so its radius is 63 m ([NREL](https://nrel.github.io/turbine-models/NREL_5MW_126_RWT.html)):

**A = π × 63² = 12,469 m²**

That is close to two football pitches. Multiply by ½ × 1.225 and you get a handy constant for this rotor: about **7,637 W for every (m/s)³** of wind.

## Step 2: power in the wind at 8 m/s

Cube the wind speed and multiply by that constant. At 8 m/s, a good, steady wind, 8³ is 512, so the wind carries about 3.9 MW through the rotor:

**7,637 × 512 = 3,910,000 W ≈ 3.9 MW**

The rotor cannot catch all of that. If it stopped the air completely, no more air could flow through, so some speed has to be left in the air behind it.

## How much can the rotor catch?

At most 16/27, or **59.3 %**. This is the Betz limit, and modern large turbines reach peak power coefficients of about 0.45 to 0.50 ([Wikipedia](https://en.wikipedia.org/wiki/Betz%27s_law)). The NREL 5 MW rotor's best Cp is 0.482, and its generator is 94.4 % efficient ([NREL 5 MW data](https://arxiv.org/pdf/2405.06829)).

So at 8 m/s:

- Rotor power = 3.91 MW × 0.482 = **1.88 MW**
- Electrical power = 1.88 MW × 0.944 = **1.78 MW**

## Power at every wind speed

Run the same sum at other wind speeds and you get the turbine's power curve. The figures below assume the best Cp all the way to rated wind speed, which is a simplification; the real curve is a little lower at the bottom end.

| Wind speed | Power in the wind | Rotor power (Cp 0.482) | Electrical power |
|---|---|---|---|
| 3 m/s (cut-in) | 0.21 MW | 0.10 MW | 0.09 MW |
| 5 m/s | 0.95 MW | 0.46 MW | 0.43 MW |
| 8 m/s | 3.9 MW | 1.9 MW | 1.8 MW |
| 10 m/s | 7.6 MW | 3.7 MW | 3.5 MW |
| 11.4 m/s (rated) | 11.3 MW | 5.3 MW | 5.0 MW |
| 15 m/s | 25.8 MW | 5.3 MW (pitched) | 5.0 MW |

From 11.4 m/s the turbine is at its rating, so the pitch drives turn the blades slightly out of the wind to hold 5 MW. Above 25 m/s it shuts down: the blades feather, the rotor stops and the brake holds it ([NREL](https://nrel.github.io/turbine-models/NREL_5MW_126_RWT.html), [DOE](https://www.energy.gov/eere/wind/inside-wind-turbine-0)).

## Why the cube law matters so much

Because small changes in wind speed make big changes in power. Going from 5 to 10 m/s doubles the wind speed but multiplies the power by eight, from 0.43 MW to 3.5 MW in the table above. That is why wind farms are built on hills, coasts and out at sea, and why taller towers reach steadier, faster wind.

Blade length matters too, but only as a square. A blade 10 % longer sweeps 1.1² = 1.21 times the area, so it catches 21 % more power at the same wind speed.

## Three mistakes to avoid

1. **Using the blade length as the diameter.** The radius is the blade length plus about half the hub, and the area uses the radius squared; mixing up radius and diameter gives an answer four times too big or too small.
2. **Forgetting Cp.** ½ρAv³ is the power in the wind, not the power out of the turbine. Multiply by about 0.45 for a good rotor, never more than 0.593.
3. **Multiplying the rating by 24 hours.** A 5 MW turbine only makes 5 MW above 11.4 m/s. Average wind speed, cubed, sets the energy it actually delivers over a year.

## The engineering takeaway

Wind power grows with the cube of wind speed and the square of blade length, and no rotor can catch more than 59.3 % of it. A 5 MW turbine is really a 5 MW cap: below rated wind it makes far less, and above it the pitch system throws the extra away.
