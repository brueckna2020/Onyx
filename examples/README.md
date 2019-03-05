# Sample Log files
Included in this directory are a handful of log files, output by [Gaussian 09](http://gaussian.com/), to be used as sample input for demonstrating Onyx's functionality.

## NMR
The `nmr` directory includes 5 files necessary for the shift difference computation:
- `1_hf6311_nmr.log` is the computed NMR output of the molecule. This is required to extract the computed proton shielding values.
- `1_hf6311_thermo_XX.log` files contain the computed thermochemical values for each deuterated molecule, from its respective log file. The numbers `XX` simply identify the position of the deuterium using the ID number assigned to each atom by Gaussian.
- `tms_hf6311+g2dp_nmr.log` is the computed NMR output of TMS standard.