
def ask():
   import re
   DNA = input("Enter the DNA sequence :")
   DNA_1 = DNA.upper()
   DNA_2 = re.sub(r"[\d\s]+","",DNA_1)
   return DNA_2


def mRNA(DNA_2):
    trans = str.maketrans("ATGC","UACG")
    DNA_3 = DNA_2.translate(trans)
    return DNA_3


def reverse_cDNA(DNA_2):
    trans = str.maketrans("ATGC","TACG")
    DNA_3 = DNA_2.translate(trans)
    DNA_rev = DNA_3[::-1]
    return DNA_rev


def complement(DNA_2) :
    trans = str.maketrans("ATGC","TACG")
    DNA_3 = DNA_2.translate(trans)
    return DNA_3


def codon_separation(mRNA_X):
    
    n = int(len(mRNA_X)/3)
    l = 0 
    i = 0
    temp = list()
    while l < n :
        temp.append(mRNA_X[i:i+3])
        i = i + 3
        l = l + 1


    return temp


def translation (mRNA_E):
   
   genetic_code = {
         "AUG":"M",
         "UUU":"F","UUC":"F",
         "UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
         "AUU":"I","AUC":"I","AUA":"I",
         "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
         "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
         "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
         "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
         "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
         "UAU":"Y","UAC":"Y",
         "CAU":"H","CAC":"H",
         "CAA":"Q","CAG":"Q",
         "AAU":"N","AAC":"N",
         "AAA":"K","AAG":"K",
         "GAU":"D","GAC":"D",
         "GAA":"E","GAG":"E",
         "UGU":"C","UGC":"C",
         "UGG":"W",
         "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
         "AGU":"S","AGC":"S",
         "AGA":"R","AGG":"R",
         "GGU":"G","GGC":"G","GGA":"G","GGG":"G",
         "UAA":"-","UAG":"-","UGA":"-"
       } 
   
   pro = ""
   for n in mRNA_E :
       pro = pro + genetic_code[n]

   return pro


DNA_2 = ask()
print("\n\n")
print("the DNA sequence : ",DNA_2)
print("\n\n")
print("The given sequence is ")
print("1) 5' to 3' or")
print("2) 3' to 5' ?")
strand = int(input("enter 1 or 2 : "))
print("\n")

if strand == 1 :
    #frame 1 
    C_DNA = complement(DNA_2)
    mRNA_D1 = mRNA(C_DNA)
    mRNA_1 = codon_separation(mRNA_D1)
    pro_1 = translation(mRNA_1)
    print("The 5'3' frame 1 is :")
    print(pro_1,"\n")

    #frame 2
    mRNA_D2 = mRNA_D1[1:]
    mRNA_2 = codon_separation(mRNA_D2)
    pro_2 = translation(mRNA_2)
    print("The 5'3' frame 2 is :")
    print(pro_2,"\n")

    #frame 3 
    mRNA_D3 = mRNA_D1[2:]
    mRNA_3 = codon_separation(mRNA_D3)
    pro_3 = translation(mRNA_3)
    print("The 5'3' frame 3 is :")
    print(pro_3,"\n")

    #frame 4 
    RC_DNA = reverse_cDNA(DNA_2)
    RCC_DNA = complement(RC_DNA)
    mRNA_D4 = mRNA(RCC_DNA)
    mRNA_4 = codon_separation(mRNA_D4)
    pro_4 = translation(mRNA_4)
    print("The 3'5' frame 1 is :")
    print(pro_4,"\n")

    #frame 5
    mRNA_D5 = mRNA_D4[1:]
    mRNA_5 = codon_separation(mRNA_D5)
    pro_5 = translation(mRNA_5)
    print("The 3'5' frame 2 is :")
    print(pro_5,"\n")

    #frame 6
    mRNA_D6 = mRNA_D4[2:]
    mRNA_6 = codon_separation(mRNA_D6)
    pro_6 = translation(mRNA_6)
    print("The 3'5' frame 3 is :")
    print(pro_6,"\n")


elif strand == 2 :
    #frame 1
    mRNA_D1 = mRNA(DNA_2)
    mRNA_1 = codon_separation(mRNA_D1)
    pro_1 = translation(mRNA_1)
    print("The 5'3' frame 1 is :")
    print(pro_1)
    print("\n")

    #frame 2
    mRNA_D2 = mRNA_D1[1:]
    mRNA_2 = codon_separation(mRNA_D2)
    pro_2 = translation(mRNA_2)
    print("The 5'3' frame 2 is :")
    print(pro_2)
    print("\n")

    #frame 3 
    mRNA_D3 = mRNA_D1[2:]
    mRNA_3 = codon_separation(mRNA_D3)
    pro_3 = translation(mRNA_3)
    print("The 5'3' frame 3 is :")
    print(pro_3)
    print("\n")

    #frame 4
    RC_DNA = reverse_cDNA(DNA_2)
    mRNA_D4 = mRNA(RC_DNA)
    mRNA_4 = codon_separation(mRNA_D4)
    pro_4 = translation(mRNA_4)
    print("The 3'5' frame 1 is :")
    print(pro_4)
    print("\n")

    #frame 5
    mRNA_D5 = mRNA_D4[1:]
    mRNA_5 = codon_separation(mRNA_D5)
    pro_5 = translation(mRNA_5)
    print("The 3'5' frame 2 is :")
    print(pro_5)
    print("\n")

    #frame 6 
    mRNA_D6 = mRNA_D4[2:]
    mRNA_6 = codon_separation(mRNA_D6)
    pro_6 = translation(mRNA_6)
    print("The 3'5' frame 3 is :")
    print(pro_6)
    print("\n")


else :
    print("Invalid input ")


