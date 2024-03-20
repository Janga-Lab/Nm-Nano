#note user should provide the coordinate file and the fastq file
import subprocess
import sys
import argparse

#https://stackoverflow.com/questions/21579892/using-argparse-to-for-filename-input 
# Initialize parser
parser = argparse.ArgumentParser("start of getting RNA fastq files")

#reference file argument
parser.add_argument('-r', action='store', dest='ref_input', help='Provide reference genome file')

#fastq file argument 
parser.add_argument('-f', action='store', dest='fastq_input', help='Provide Fastq file')
 

# Read arguments from command line
args = parser.parse_args()

ref = args.ref_input
fastq_reads = args.fastq_input
if ref is None or fastq_reads is None:
       print("You Must enter the reference genome and the fastq reads files")
       exit(1) # to stop executing the remaining python code after this line.
##################################################################################
#a=sys.argv[1]
#b=sys.argv[2]
f = open("hek.sam", "w")
f1 = open("hek.bam", "w")
f3 = open("hek-reads-ref.eventalign.txt", "w")
####subprocess.run(["minimap2", "-ax", "map-ont", "--split-prefix", "/tmp/temp_name", "ref.fa", "reads.fastq"], stdout=f)    #minimap2 -ax map-ont --split-prefix /tmp/temp_name  ref.fa  reads.fastq > hek.sam
subprocess.run(["minimap2", "-ax", "map-ont", "--split-prefix", "/tmp/temp_name", ref, fastq_reads], stdout=f) 
subprocess.run(["nanopolish" ,"index", "-d", "fast5_files/", "reads.fastq"])   #nanopolish index -d fast5_files/ reads.fastq 
subprocess.run(["samtools" ,"view", "-S", "-b", "hek.sam"],stdout=f1)#samtools view -S -b hek.sam > hek.bam 
subprocess.run(["samtools" ,"sort", "hek.bam", "-o", "hek.sorted.bam"]) #samtools sort hek.bam -o hek.sorted.bam
subprocess.run(["samtools" ,"index", "hek.sorted.bam"]) #samtools index hek.sorted.bam
subprocess.run(["samtools","quickcheck" ,"hek.sorted.bam"]) #$samtools quickcheck hek.sorted.bam
subprocess.run(["nanopolish","eventalign" ,"--reads", "reads.fastq", "--bam", "hek.sorted.bam","--genome", "ref.fa", "--scale-events"], stdout=f3) #$nanopolish eventalign  --reads reads.fastq --bam  hek.sorted.bam  --genome ref.fa --scale-events > hek-reads-ref.eventalign.txt
subprocess.run(["python","gen_coors_Nm.py"])
subprocess.run(["python","extract_nm.py",])
