# LinkedIn Post — Spine Planner Launch

**Status:** Draft
**Date:** 2026-03-23
**Images needed:** De-identified pre-op X-ray, plan output, post-op X-ray, construct record

---

**I built a free, open-source spinal instrumentation planning tool — and I need your help.**

As a spinal surgeon, I've spent years sketching instrumentation plans on paper templates. They work, but they don't export, translate, or travel well between teams.

So I built a digital replacement: **Spinal Instrumentation Plan & Record** — a visual planning tool that runs in any browser, works completely offline, and needs no installation. It's designed for the realities of hospital IT: locked-down machines, no admin access, no internet required. Open it from a USB stick or bookmark it from the web.

**What it does:**
- Pedicle screws, hooks, fixation, interbody cages (ACDF through ALIF), osteotomies (Schwab 1-6), deformity correction forces
- 16 implant manufacturers, 90+ screw systems
- Dual-window sync for theatre dual-display setups
- PDF and JPG export for clinical records
- Session privacy mode for shared machines

It's available in **16 languages** — but that's where I need help.

**The translations are machine-generated and verified against published clinical glossaries** (AO Spine, DWG, SFCR, GEER, SICV&GIS and others), but they haven't been reviewed by native-speaking surgeons. If you operate in German, French, Spanish, Italian, Portuguese, Swedish, Norwegian, Danish, Finnish, Dutch, Polish, Greek, Turkish, Russian, or Ukrainian, I'd hugely value 20 minutes of your time to review the clinical terminology in your language.

The tool includes a built-in review form — just select your language and flag anything that doesn't match how you'd describe it in theatre.

**Try it:** plan.skeletalsurgery.com/spine
**Source code:** github.com/nigelgummerson/spine
**Licence:** GNU GPLv3 — free forever, no accounts, no tracking, no data leaves your machine.

Nigel Gummerson FRCS (Tr & Orth)
Spinal Surgeon, Leeds Teaching Hospitals NHS Trust

---

## Image plan

1. Pre-op AP X-ray + Plan output (side by side or stacked)
2. Post-op AP X-ray + Construct record

Or as a LinkedIn carousel: pre-op X-ray → plan → post-op X-ray → construct record.

## De-identification checklist

- [ ] Strip DICOM metadata (`exiftool -all= image.jpg`)
- [ ] Crop out patient name labels, date stamps, hospital identifiers
- [ ] Check no identifiable unusual construct/anatomy
