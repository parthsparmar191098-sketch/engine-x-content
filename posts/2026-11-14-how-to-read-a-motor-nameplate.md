---
title: How to Read an Electric Motor Nameplate, With a Real 7.5 kW Example
date: 2026-11-14
category: learn
summary: What every number on a three-phase motor nameplate means, from frame size and star/delta voltages to slip, IP rating, duty S1 and bearing sizes, worked through on a 7.5 kW 4-pole motor.
seo_title: How to Read a Motor Nameplate (7.5 kW Example)
seo_description: What each field on a three-phase motor nameplate means: frame, kW, volts, star/delta, rpm and poles, efficiency class, IP rating, duty S1 and bearings.
image: assets/2026-11-14-motor-nameplate.svg
image_alt: Example nameplate of a 7.5 kW 4-pole three-phase induction motor in frame 132M with callouts explaining frame size, star and delta voltages, power and current, speed and poles, IP55, duty S1, ambient temperature and bearing sizes
image_credit: Diagram: Engine-X
model: inductionmotor
keywords: how to read a motor nameplate, motor nameplate explained, what does s1 duty mean, how to find motor poles from rpm, delta star voltage on motor nameplate
tldr: A motor nameplate tells you the frame size, output power, voltages for star and delta, full-load current and speed, efficiency, enclosure, duty and bearings, and the speed alone tells you how many poles the motor has.
takeaways:
- Frame 132M means the shaft centre is 132 mm above the feet; S, M or L is the foot length.
- 400 V Δ / 690 V Y: connect in delta on a 400 V supply, star on 690 V.
- Rated speed just under 3000, 1500, 1000 or 750 rpm (50 Hz) tells you 2, 4, 6 or 8 poles.
- kW is mechanical power at the shaft, not what the motor draws from the supply.
- S1 means continuous duty; IP55 means dust-protected and safe against water jets.
faq:
- How do you tell how many poles a motor has from the nameplate? | Look at the rated speed. On 50 Hz a motor just under 3,000 rpm has 2 poles, just under 1,500 rpm has 4, under 1,000 rpm has 6 and under 750 rpm has 8, because the rotor runs a few percent slower than the field.
- What does S1 mean on a motor nameplate? | S1 is continuous duty: the motor can run at its rated load all day, every day. Other duty types cover short-time, intermittent and varying loads.
- Is the kW on the nameplate the power the motor uses? | No. It is the mechanical power the shaft delivers at full load. The motor takes more from the supply, its output divided by its efficiency, so a 7.5 kW motor at 90.4 % takes about 8.3 kW.
sources:
- AEMT / IPE — Guide to motor nameplates | https://www.ipesearch.co.uk/AEMT-guide-motor-nameplates
- Marathon Electric — How to read an industrial motor nameplate | https://www.marathonelectric.com/articles/How-to-read-an-industrial-motor-nameplate
- SEVA — MX3-132M1-4 7.5 kW 4-pole motor data sheet | https://www.seva-tec.de/media/pdf/91/f5/d7/SEVA-Datenblatt-MX3-132M1-4-7-5KW-4-polig-Bauform-B35-Drehstrommotor.pdf
- FRAMO — FRA1 IE3 132M4 7.5 kW 400/690 V 50 Hz B3 data sheet | https://live.public.francoysbe.profitplus.be/nl/attachment/4881551/23574124/FRAMO-FRA1-IE3-132M4-1500T-7-5kW-400-690V-50Hz-B3
- Control Engineering — Anatomy of an AC induction motor | https://www.controleng.com/anatomy-of-an-ac-induction-motor-3/
- Engine-X — Induction motor 3D model | https://engx3d.com/3d-models/induction-motor
---
A motor nameplate is the motor's data sheet riveted to its frame. It gives the frame size, output power, supply voltages, full-load current and speed, efficiency, enclosure rating, duty and often the bearings. Read in order, it tells you how to connect the motor, what it can drive and what spares to stock.

To see what sits behind those numbers, take apart the [Engine-X induction motor 3D model](https://engx3d.com/3d-models/induction-motor), a 7.5 kW 4-pole motor in frame 132M, and read the [induction motor guide](https://engx3d.com/induction-motor) for how the stator field turns the rotor.

## What does the frame size on a motor nameplate mean?

The frame number is the height from the bottom of the motor's feet to the shaft centre, in millimetres. A **132** frame has its shaft 132 mm above the feet; the letter after it, **S, M or L**, gives the foot length, so the spacing of the mounting holes ([AEMT](https://www.ipesearch.co.uk/AEMT-guide-motor-nameplates)).

That is why IEC motors of the same frame are interchangeable on a baseplate: a 132M from one maker bolts down where a 132M from another came out. The mounting code next to it, such as **IM B3**, says how it is mounted; B3 is a foot-mounted motor.

## Power, voltage and current: how to connect it

Our example motor is a 7.5 kW, 4-pole motor in frame 132M, taking **14.26 A at 400 V** at full load ([SEVA data sheet](https://www.seva-tec.de/media/pdf/91/f5/d7/SEVA-Datenblatt-MX3-132M1-4-7-5KW-4-polig-Bauform-B35-Drehstrommotor.pdf)). Each line on its plate answers a practical question:

1. **kW** is the mechanical power at the shaft at full load, not what the motor draws. At 90.4 % efficiency this motor takes about 7.5 ÷ 0.904 ≈ 8.3 kW from the supply.
2. **400 V Δ / 690 V Y** is two ways to connect the same windings. Delta is the low-voltage connection and star the high-voltage one ([AEMT](https://www.ipesearch.co.uk/AEMT-guide-motor-nameplates)), so on a 400 V three-phase supply this motor is linked in delta ([FRAMO](https://live.public.francoysbe.profitplus.be/nl/attachment/4881551/23574124/FRAMO-FRA1-IE3-132M4-1500T-7-5kW-400-690V-50Hz-B3)).
3. **Amps** is the full-load current at that voltage. It is the number to set the overload relay to, and a motor running well above it is overloaded.
4. **cos φ** (power factor) is 0.84 here: the share of the current that does real work. The rest magnetises the motor.
5. **3~** in front of the data means three-phase.

| Plate field | Example (7.5 kW, 132M) | What it tells you |
|---|---|---|
| Power | 7.5 kW | Shaft output at full load |
| Voltage | 400 V Δ / 690 V Y | Delta on 400 V, star on 690 V |
| Current | 14.26 A at 400 V | Overload relay setting |
| Speed | 1,450 rpm | 4 poles, 3.3 % slip |
| Efficiency | 90.4 % | Losses: about 0.8 kW of heat |
| Power factor | 0.84 | Reactive current the supply carries |
| Bearings | 6308 / 6308 | Spares to order |

## How do you find the number of poles from the rpm?

From the rated speed. On 50 Hz a three-phase motor's field turns at 3,000 rpm with 2 poles, 1,500 with 4, 1,000 with 6 and 750 with 8; the nameplate speed sits a little below one of these because an induction motor always slips behind its field ([AEMT](https://www.ipesearch.co.uk/AEMT-guide-motor-nameplates)).

The rule behind it is synchronous speed = 120 × frequency ÷ poles ([Control Engineering](https://www.controleng.com/anatomy-of-an-ac-induction-motor-3/)). For our motor, 120 × 50 ÷ 4 = 1,500 rpm, and its 1,450 rpm rating means 50 rpm, or 3.3 %, of slip at full load. A motor running at noticeably more than its rated slip is carrying more than its rated load.

## IP rating, duty, insulation and the small print

- **IP55:** the first digit (0 to 6) is protection against solids, the second (0 to 9) against water ([AEMT](https://www.ipesearch.co.uk/AEMT-guide-motor-nameplates)). 5 and 5 mean dust-protected and safe against water jets: fine for a plant room, not for being washed down hard.
- **S1:** continuous duty, built to run around the clock at rated load. There are ten duty types in all, for short-time, intermittent and varying loads ([AEMT](https://www.ipesearch.co.uk/AEMT-guide-motor-nameplates)).
- **Insulation class (Ins. Cl. F):** the thermal class the winding was made to. A repairer needs it, because a rewind must use the same class or better.
- **Ambient:** the hottest surrounding air the rating allows, commonly 40 °C ([AEMT](https://www.ipesearch.co.uk/AEMT-guide-motor-nameplates)). A motor in a hotter room must be derated.
- **IE class:** IE1 to IE4, standard to super-premium efficiency; Ecodesign rules set the minimum class for new motors ([AEMT](https://www.ipesearch.co.uk/AEMT-guide-motor-nameplates)).
- **Bearings:** many plates list the drive-end and opposite-end bearing numbers ([Marathon Electric](https://www.marathonelectric.com/articles/How-to-read-an-industrial-motor-nameplate)). Our motor has a **6308** at each end, the first spare to keep on the shelf.
- **Service factor** (on NEMA motors): 1.15 means the motor can safely run at 115 % of its rated power ([Marathon Electric](https://www.marathonelectric.com/articles/How-to-read-an-industrial-motor-nameplate)). IEC plates usually leave it out.

On ships and in plants the plate is often painted over or corroded, which is a good reason to photograph every motor's nameplate when it is new and keep the photos with the equipment list.

## The engineering takeaway

A nameplate answers three questions before you touch a motor: how to connect it (voltage, star or delta, current), what it can drive (kW, rpm and poles, duty) and how to keep it running (bearings, insulation class, IP rating). The speed alone tells you the poles, and the current tells you how hard it is working.
