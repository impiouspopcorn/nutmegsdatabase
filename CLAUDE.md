# Nutmeg – how to update

This repo publishes an encrypted, read-only copy of a workload tracker to GitHub Pages.
The plaintext data is never stored here. The master data lives in the owner's private
Claude artifact (file `data/tracker.json`); its link is in the owner's project instructions.

## Rebuild after a check-in
1. Read `data/tracker.json` from the private artifact. Then read the artifact's database collection `overrides` (one doc per project ID with any of `theme`, `rag`, `status`, `owner`, plus `at`): these are edits the owner made on the page. Apply them to tracker.json, add a dated update line noting the change, then delete those override docs. Then apply the agreed check-in changes.
2. Put the data at `<work>/data/tracker.json`, copy `tools/template.html` and `tools/build.py`
   to `<work>/src/`, and `keys/*` to `<work>/keys/`.
3. `python3 <work>/src/build.py <work>` writes `dist/private/index.html` (plain) and
   `dist/public/index.html` (encrypted with `keys/public.pem`; no password needed).
4. Republish the private artifact (page + `data/tracker.json`), then copy
   `dist/public/index.html` to `index.html` here, commit and push to `main`.
5. Check the public file contains no plaintext project names before pushing.

## Data shape (tracker.json)
- `meta.updated` – date of the last check-in.
- `week` – `label`, `days[{date, items[], note}]`, `priorities{must,should,iftime}[{text,pid,done}]`, `added[]` (new tasks mid-week), `ellis[]` + `ellisNote`, `george[]` (GW catch-up points), `esweekly[]` + `esNote` (Energy Services weekly, Mon 8:30), `super6` (weekly reminder text). List items are `{text,pid,done}`.
- Copy for OneNote follows the owner's OneNote order: Tasks at start of the week, Ellis work this week, GW catch-up, ES Weekly, Super 6.
- `projects[]` – `id, theme` (strategy pillar: Net zero pathway | Fair transition | Data & innovation | Embed in decisions | Supply chain | Team & admin; `area` keeps the old grouping), `title, detail, status, rag, flag, owner, due, next, why, decision, updates[{date,status,text}]` (newest first).
- `wins[]` – `date (YYYY-MM or YYYY-MM-DD), title, impact, evidence|null, who (Ella|Ellis|Team), pid`.

## Rules
- Claude may update RAG ratings based on the owner's updates. Always list every RAG change in the check-in summary so she can overrule it.
- Never tick tasks for the owner from guesswork: completions come from her Friday OneNote screenshot or what she says.
- Unticked OneNote items carry forward into next week's priorities.
- Every completed milestone is a candidate win: log impact. Wins without evidence show no label (owner's choice, 20 Nov 2026).

## Drafting next week's priorities (agreed 20 Nov 2026 after errors)
- Build them only from: unticked OneNote items, items the owner names, and hard deadlines that fall that week.
- Anything on the Nutmeg list that isn't on her OneNote: ask her where it's at. Don't carry it silently and don't drop it silently.
- Look ahead: at every Monday plan and Friday draft, scan project due dates for the next 2–3 weeks and pull them forward ("Looking ahead: X due …") so she sees them before they arrive.
- An item with a future deadline stays visible every week until it's done, however far away the deadline is: as a priority when it's that week's work, otherwise as "Looking ahead".
- A ticked OneNote item is done. Never turn it into a follow-up (e.g. "send by …") unless she says so.
- Leave out anything owned by or waiting on someone else (marketing, suppliers, Ellis). That goes in the project's `next` as "Waiting on …".
- Put work in the week it will actually be done; later work stays in the project's `next` (e.g. a 16 Dec workshop is planned the week before, not now).
- Meetings go on the days panel, not in priorities.
- Don't link projects or news unless she links them (e.g. the EDF acquisition is company news, not part of plug-in solar).
- Mark carried items "(carried over)". Label the week "(draft)" and show her the draft priorities in the reply; drop the label once she confirms or at the Monday plan.
- Project titles must say what the item is now (they show in "Coming up").

## Weekly rhythm
- Monday before 8:30: Monday plan – diary, deadlines, what's new. Output: tiered priorities, ES Weekly points, GW catch-up points, proposed asks for Ellis.
- Monday after the 10:00 Ellis catch-up: Ellis's rundown updates `week.ellis`.
- Any time: "for George …" adds to `week.george`; new projects get added. Ordinary new tasks stay in OneNote.
- Friday: OneNote screenshot + narrative + wins + next week's knowns. Output: updates, wins, carry-forwards, draft next week.

## Audiences (learned from the owner)
- George (GW catch-up): board member. Only very high-level items: strategic decisions, risks that need his weight, resourcing, major milestones. No operational detail (e.g. Football Rebooted data issues) and nothing he has already heard.
- Energy Services weekly (Mon 8:30, formerly "HS weekly"): George's department meeting (field services incl. metering and solar). Only critical, very high-level updates relevant that week – e.g. the strategy launch, events. Plug-in solar is always of interest, at headline level only.
- Days panel: log only notable, one-off meetings (AI Council, SGG, Football Rebooted, external meetings). Never recurring ones (start/end of week team meetings, ES weekly, PR weekly, George catch-up).

## Asking questions
- When the OneNote page has entries that don't match a known project or person, ask what they are before filing them. Ask about possible wins and closed-out items at every check-in.

## What counts as a win
- Significant achievements with external or senior visibility, or major deliveries: launches, awards, press coverage, big pieces of written work (e.g. the Business South / Daily Echo copy), programme completions.
- Not admin or bookings. Something booked becomes a win only when it is delivered (e.g. Madeline's final presentation).
- Big pieces of work often happen in other chats: check past conversations for wins and evidence.

## Context
- Social Spark is a social-housing solar initiative run by George and Caitlin – not a sustainability team project.
- Recurring meetings never go on the days panel; monthly LT feedback is the exception and is shown.

## Board report and newsletter
- The Briefs tab has Board report and Newsletter views for any month, built from that month's updates and wins, grouped by pillar. Pillar columns follow the monthly-sustainability-reporting skill.
- Before drafting the monthly board paper: check memory and past chats for anything this month not yet in Nutmeg, log it, then pre-fill the skill's input template from Nutmeg. After the board paper is approved, log anything new it contains back into Nutmeg.
- New projects must be given a pillar.
