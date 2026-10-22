# Structure figures for MAT: active sites, salt bridges, hydrogen bonds and metals

Python scripts that turn lists of interactions in a protein structure into PyMOL scenes and interactive web viewers (GLmol). They were written for the web pages of the **Macromolecular Analysis Toolkit (MAT)** (http://mat.iitr.ac.in), which analyses a structure and reports its ligands, metals, salt bridges and hydrogen bonds.

MAT is described in: Kalyan, G.; Junghare, V.; John S, S.; Chattopadhyay, A.; Mitra, P.; Hazra, S. Parsers, Data Structures and Algorithms for Macromolecular Analysis Toolkit (MAT): Design and Implementation. *bioRxiv* **2019**, 605907.

## How it works

The scripts are code generators. For each kind of figure there are two parts:

- a **template** (`*_temp_script.py`) holding the PyMOL drawing commands, and
- a **generator** (`*_main.py`) that reads the interaction list and writes two ready-to-run PyMOL scripts with the data filled in.

```
interaction list  +  structure (inputfile.pdb)
        │
   *_main.py  (fills the template)
        │
        ├──  *_script.py     open in PyMOL to see the scene
        └──  *_script_gl.py  run with PyMOL to write a screenshot (PNG) and a GLmol web page (HTML)
```

## Modules

| Folder | Generator | Input list(s) | What is drawn | Output scripts |
|---|---|---|---|---|
| `active_site/` | `as1_main.py` | `Active_site1`, `metal_1` | The whole structure with every ligand as sticks and every metal as a sphere | `as1_script.py`, `as1_script_gl.py` |
| `active_site/as2/` | `as2_main.py` | `Active_site1`, `Active_site2` | One view per ligand, showing the ligand and the residues around it | `as2_ligand<N>_script.py`, `as2_ligand<N>_gl.py` |
| `active_site/as3/` | `as3_main.py` | `Active_site1`, `Active_site3` | One view per ligand, with the residues in contact, taken from a list of atom pairs and distances | `as3_ligand<N>_script.py`, `as3_ligand<N>_gl.py` |
| `salt_bridge/` | `sb_main.py` | `detect_saltbridge_1` | Salt bridges as distance lines between the two residues | `sb_script.py`, `sb_script_gl.py` |
| `des_salt_bridge/` | `dsb_main.py` | `detect_saltbridge_2` | Like-charge residue pairs (for example Lys–Lys, Glu–Glu), coloured and labelled | `dsb_script.py`, `dsb_script_gl.py` |
| `hydrobond/` | `hbb_main.py` | `HBonds_BB` | Backbone hydrogen bonds as distance lines (needs a structure with hydrogens) | `hbb_script.py`, `hbb_script_gl.py` |
| `metals/` | `metal1_main.py` | `metal_1` | All metal sites in the structure | `metal1_script.py`, `metal1_gl.py` |
| `metals/` | `metal2_main.py` | `metal_1`, `metal_2` | One view per metal with its coordinating residues | `metal_2_<N>_script.py`, `metal_2_<N>_gl.py` |

`active_site/as2/ty.py` is a helper that counts the ligand blocks in `Active_site2`. `salt_bridge/webpage/` holds a variant of the salt-bridge generator written for the web page (it writes separate local and web scripts).

## Input files

Put these in the working folder:

- `inputfile.pdb`, the structure, and `inputfile.txt`, containing its file name (for example `4oe9.pdb`). The hydrogen-bond module uses `placed_h.pdb`, the structure with hydrogens added.
- The interaction list for the module (see the table above). The formats, from the examples:

| File | Lines look like | Meaning |
|---|---|---|
| `Active_site1`, `metal_1` | `[Ligands]4`, then `CIT 201 A` | A header, then one `residue-name number chain` per ligand or metal |
| `Active_site3` | `CIT 201 O1 A 103 AND SER 39 HG A 544  3.99678` | Ligand atom, `AND`, contacting atom, then the distance (Å) |
| `detect_saltbridge_1` | `ARG 29 NH2 A 373 AND GLU 108 OE2 A 1607  2.79663` | The two atoms of a salt bridge, then the distance |
| `detect_saltbridge_2` | `LYS 43 A AND LYS 44 A  3.81989` | A like-charge residue pair, then the distance |
| `HBonds_BB` | `SER 2 O A 4 AND ALA 4 H A 19 3.09774` | Two atoms of a backbone hydrogen bond, then the distance |
| `metal_2` | `ZN 501 ZN C 6 AND CYS 94 SG C 1981  2.34739` | Metal, `AND`, coordinating atom, then the distance |

`Active_site2` lists each ligand followed by the residues around it.

## Running

These scripts are Python 2 and use the Python API of PyMOL 1.x.

1. Make a working folder with the input files above.
2. Copy into it the generator and template of the module, the matching exporter from `glmol_export/` (`export_to_gl.py`, or `sb_export_to_gl.py` / `dsb_export_to_gl.py` for the salt-bridge modules), and from `third_party/glmol/` the `imported.html` template and the `js/` folder. The generated scripts import the exporter from the current folder.
3. Run the generator, for example `python sb_main.py`.
4. To see the scene, open the generated `*_script.py` in PyMOL. To make the web page and screenshot, run `pymol -cq <name>_gl.py`; it writes a PNG and an HTML file (the file names are set in the script, for example `as1_glmol.html`).

`examples/` has one generated pair of scripts for each module (for example, structure 4OE9 for the active site and 5Y1Z for the metals), showing what the generators write and the data they embed.

## glmol_export/ and third-party code

`glmol_export/` holds the exporter that converts a PyMOL scene to GLmol. It is a **modified copy of `exportToWeb.py` from GLmol by biochem_fan** (Takanori Nakane, 2011), which is licensed under the **GNU Lesser General Public License v3** (or later).

`third_party/glmol/` has the original exporter, the GLmol page template (`imported.html`), its JavaScript (`js/`: GLmol, Three.js and jQuery) and the licence files (`LICENSE.txt`, `LICENSE-LGPL3.txt`, `LICENSE-GPL3.txt`), unchanged. Keep these licence files with the code. The jQuery and Three.js files are third-party libraries with their own licences.

## Notes

- The scripts are kept as they were written, so file names are set inside them. Some commented-out lines in the exporters contain old folder paths.
- No licence has been added for the code written for this repository. The GLmol-derived files stay under the LGPL v3.
