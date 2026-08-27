# Phase 9 production check

This file exists only to trigger a CI run against the production
BuildDoctor deployment on Render (not the local ngrok tunnel).

Expected: the workflow fails at the apt-get step, which is build
machinery, so the diagnosis should land in the informational lane.