# Bio-informatics-projects
Beginer level python codes and pipelines for bio-informatics

Welcome to my Python portfolio repository. This repository serves as a centralized hub showcasing production-grade Python applications, automated workflows, and data pipelines designed to solve real-world problems.

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


