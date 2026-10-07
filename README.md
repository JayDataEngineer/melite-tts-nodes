# melite-tts-nodes

Carved from melite-audio-nodes 2026-09-04 (the all-in-one wrapper of
the audiocpp-fork was too heavy for a master extension pack — separate
packs per card lane). Class names unchanged; graphs survive the swap.

## Install

Install through ComfyUI-Manager (git URL
`https://github.com/JayDataEngineer/melite-tts-nodes`). Manager
runs `install.py`, which fetches + sha-verifies the pinned native
library release asset (`libaudiocore-3938031`) into this pack's
`native/` dir — no estate tooling, no environment variables,
nothing external. A manual clone converges the same way by running
`python install.py`, then restart ComfyUI.

Provenance: melite-audio-nodes (published from the inference estate
2026-09-01); its own repo since 2026-10-17.
