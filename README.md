# Bio-informatics-projects
Beginer level python codes and pipelines for bio-informatics

Welcome to my Python portfolio repository. This repository serves as a centralized hub showcasing production-grade Python applications, automated workflows, and data pipelines designed to solve real-world problems.

 SIX-frame-translation
2) 🧬 Six-Frame DNA Translation Tool

A Python-based bioinformatics tool that performs six-frame translation of a DNA sequence into amino acid sequences — replicating the functionality of the [ExPASy Translate Tool](https://web.expasy.org/translate/).

> ✅ Validated against ExPASy — all 6 frames produce identical results.


 📌 What is Six-Frame Translation?
In molecular biology, a DNA double strand can be read in 6 different reading frames:
- 3 frames on the sense strand (5'→3') — starting at position 1, 2, and 3
- 3 frames on the antisense strand (3'→5') — starting at position 1, 2, and 3

Each frame produces a different amino acid sequence, which helps identify potential Open Reading Frames (ORFs) and protein-coding regions.

 ⚙️ Features :
- Accepts raw DNA sequence as input (handles spaces, digits, lowercase)
- Supports both 5'→3' and 3'→5' input strand orientations
- Generates all 6 reading frames
- Uses the standard genetic code (64 codons including stop codons)
- Outputs single-letter amino acid sequences for each frame
- Stop codons are represented as `"-"`

🚀 How to Run
1) Requirements
- Python 3.x (no external libraries needed)

2) Steps
```bash
git clone https://github.com/your-username/six-frame-translation.git
cd six-frame-translation
python SIX-frame_translation.py
```

 🧩 Code Structure

| Function | Description |
|----------|-------------|
| `ask()` | Takes DNA input, cleans and formats it |
| `mRNA()` | Transcribes DNA to mRNA (T→U, A→A, etc.) |
| `complement()` | Returns the complementary DNA strand |
| `reverse_cDNA()` | Returns the reverse complement of DNA |
| `codon_seperation()` | Splits mRNA into codons (triplets) |
| `translation()` | Translates codons to amino acids using the standard genetic code |



 📚 Background :
This project was built as part of a bioinformatics learning journey to understand:
- DNA transcription and translation
- Reading frame analysis
- Codon tables and the genetic code
- Reverse complement strand analysis


🔭 Future Improvements :
-  ORF detection (Met → Stop codon)
-  FASTA file input support
-  Ambiguous base handling (`N`, `R`, `Y`, etc.)
-  Color-coded HTML output (like ExPASy)
-  GUI using Tkinter or Flask

=======
1) DNA Sequence Analysis Tool 
A Python-based bioinformatics tool designed to perform fundamental DNA sequence analyses. This project provides an interactive command-line interface that allows users to analyze DNA and RNA sequences using core molecular biology concepts.

 Features :
1) GC Content Calculation – Determines the percentage of Guanine (G) and Cytosine (C) nucleotides in a DNA sequence.
2) AT Content Calculation – Calculates the percentage of Adenine (A) and Thymine (T) nucleotides.
3) Complementary DNA Strand Generation – Produces the complementary DNA sequence based on standard base-pairing rules.
4) DNA to mRNA Transcription – Converts a DNA template strand into its corresponding mRNA sequence.
5) Protein Translation – Translates an mRNA sequence into a protein sequence using the standard genetic code and identifies translation termination at stop codons.
6) Interactive Menu System – Allows users to perform multiple sequence analysis operations through a simple menu-driven interface.

Technologies Used :
* Python 3
* String Manipulation
* Loops and Conditional Statements
* Basic Molecular Biology Concepts

Learning Outcomes :
This project demonstrates the implementation of key bioinformatics concepts, including nucleotide sequence processing, transcription, translation, codon recognition, and sequence composition analysis. It serves as a beginner-friendly introduction to computational biology and bioinformatics programming.

 Future Improvements :
* Reverse Complement Generation
* FASTA File Support
* DNA/RNA Sequence Validation
* Open Reading Frame (ORF) Detection
* Six-Frame Translation
* Export Results to Text or CSV Files
* Graphical User Interface (GUI)


