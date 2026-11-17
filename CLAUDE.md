# Nutmeg – how to update

This repo publishes an encrypted, read-only copy of a workload tracker to GitHub Pages.
The plaintext data is never stored here. The master data lives in the owner's private
Claude artifact (file `data/tracker.json`); its link is in the owner's project instructions.

## Rebuild after a check-in
1. Read `data/tracker.json` from the private artifact and apply the agreed changes.
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
- `projects[]` – `id, theme, title, detail, status, rag, flag, owner, due, next, why, decision, updates[{date,status,text}]` (newest first).
- `wins[]` – `date (YYYY-MM or YYYY-MM-DD), title, impact, evidence|null, who (Ella|Ellis|Team), pid`.

## Rules
- RAG ratings change only when the owner says so.
- Never tick tasks for the owner from guesswork: completions come from her Friday OneNote screenshot or what she says.
- Unticked OneNote items carry forward into next week's priorities.
- Every completed milestone is a candidate win: log impact, and ask for evidence when missing.

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
