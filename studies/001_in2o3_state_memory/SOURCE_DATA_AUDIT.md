# Source-data audit

## Verified Drive-side archive state

The large archive is stored outside GitHub as a 12-part split ZIP. The Drive-side extraction note states:

- original archive size: approximately 23.67 GiB;
- parts `.z01` through `.z11`: 2 GiB each;
- final `.zip` part: approximately 1.67 GiB;
- all 12 parts are required;
- reconstructed archive passed `unzip -t` for 11,327 entries with no reported corruption.

A SHA-256 checksum file exists for all 12 parts. Raw parts remain external to GitHub.

## Scientific audit target

The first raw-data question is whether the lower S4 methanol STY is a persistent functional deficit or a transient recovery state. Priority files are therefore:

1. GC/MS time series spanning S1→S3→CO2-only reoxidation→S4;
2. exact gas-switch timestamps and reactor/analysis delay information;
3. synchronized In K-edge XANES/EXAFS;
4. operando XRD time series and multi-peak line-profile data;
5. Zr K-edge or composition-sensitive data where available.

## Current evidence boundary

Until those raw files are indexed and inspected, the project does not claim:

- statistical significance of the published S1/S4 STY difference;
- persistent S4 deactivation after kinetic stabilization;
- causal proportionality between single-peak FWHM and accessible active area;
- exclusion of hydroxyl/vacancy topology, Zr redistribution, phase segregation, or reactor lag.

The archive manifest and selective extraction are the next evidence upgrade.
