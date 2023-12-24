playwright test example
======

This repo contains a zero dependency python server that serves some html and
a json endpoint that enables us to test a swath of situations we hit in
'real' software. The goal is to be able to quickly launch synthetic setups
to check that we can get playwright to do what we need in a highly controlled
environment before moving it into the real setup needed.

## Running

For now, we've been able to not use any dependencies and still get a setup
that covers the scenarios we need. That may change in the future.

```bash
python3 main.py
```

Will start on localhost:8002 by default (can change port by modifying main.py)