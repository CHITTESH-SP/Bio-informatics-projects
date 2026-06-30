

def ask():
   import re
   DNA = input("Enter the DNA sequence :")
   DNA_1 = DNA.upper()
   DNA_2 = re.sub(r"[\d\s]+","",DNA_1)
   return DNA_2


def cDNA(DNA_2):
    trans = str.maketrans("ATGC","TACG")
    DNA_3 = DNA_2.translate(trans)
    print("The entered DNA sequence is : ")
    print(DNA_2,"\n")
    print("The complementary DNA sequence is : ")
    print(DNA_3,"\n")
    print("Job done")
    print("\n\n")


def reverse_cDNA(DNA_2):
    trans = str.maketrans("ATGC","TACG")
    DNA_3 = DNA_2.translate(trans)
    DNA_rev = DNA_3[::-1]
    print("The entered DNA sequence is : ")
    print(DNA_2,"\n")
    print("The reverse compliment DNA sequence is : ")
    print(DNA_rev,"\n")
    print("Job done")
    print("\n\n")


def mRNA(DNA_2):
    trans = str.maketrans("ATGC","UACG")
    DNA_3 = DNA_2.translate(trans)
    print("The entered DNA sequence is : ")
    print(DNA_2,"\n")
    print("The transcripted mRNA sequence is : ")
    print(DNA_3,"\n")
    print("Job done!!")
    print("\n\n")
    
def translation(mRNA):
     
     start = mRNA.find('AUG')
     RNA_1 = mRNA[start:]
     
     n = int(len(RNA_1)/3) 
     l = 0
     i = 0
     mRNA_1 = list()
     while l <= n:
        mRNA_1.append(RNA_1[i:i+3])
        i = i+3
        l = l+1
     
     mRNA_2 = list()
     for n in mRNA_1:
        if n == 'UAA':
            break
        elif n == 'UAG':
            break
        elif n == 'UGA':
            break
        else:
            mRNA_2.append(n)


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
         "GGU":"G","GGC":"G","GGA":"G","GGG":"G"
       }  
       
     pro = ""
     for n in mRNA_2 :
         pro = pro + genetic_code[n]
           

     print("\n\n")  
     print(pro)
     print("\n\n")
     print("Job done!!")
     print("\n\n")


def GC_cont(DNA_2):
    DNA = DNA_2
    G_Content = DNA.count("G")
    C_Content = DNA.count("C")
    A_Content = DNA.count("A")
    T_Content = DNA.count("T")
    length = len(DNA)
    GC_Content = ((G_Content + C_Content)/length)*100
    AT_Content = ((A_Content + T_Content )/length)*100
    print(f"% of  GC content : {GC_Content}%")
    print(f"% of  AT content : {AT_Content}%")
    print("\n\n")

while True:
    print("Type of operation:")
    print("1.Complementary strand ")
    print("2.reverse complement")
    print("3.mRNA conversion")
    print("4.translation")
    print("5.GC_content")
    print("6.exit")
    op = int(input("Enter the mode of operation :"))
    valid = set("ATGC")
    valid_R = set("AUGC")
    
    if op == 1:
       DNA_2 = ask()
       if not all (base in valid for base in DNA_2) :
           print("WARNING !! Invalid input sequence","\n")

       else :  
          cDNA(DNA_2)
       

    elif op == 2:
       DNA_2 = ask()
       if not all (base in valid for base in DNA_2) :
           print("WARNING !! Invalid input sequence","\n")

       else :   
           reverse_cDNA(DNA_2)
       
      
    elif op == 3:
        DNA_2 = ask()
        if not all (base in valid for base in DNA_2) :
           print("WARNING !! Invalid input sequence","\n")

        else :   
           mRNA(DNA_2)
        
    
    elif op == 4:
        mRNA = input("enter the mRNA sequence :")
        if not all (base in valid_R for base in mRNA) :
           print("WARNING !! Invalid input sequence","\n")

        else :   
           translation(mRNA)
        
             
    elif op == 5:
        DNA_2 = ask()   
        if not all (base in valid for base in DNA_2) :
           print("WARNING !! Invalid input sequence","\n")

        else :   
           GC_cont(DNA_2)
        

    elif op == 6:
         break
     
    else :
        print("inavild operation")
       
print("Job done ! thank you ")
