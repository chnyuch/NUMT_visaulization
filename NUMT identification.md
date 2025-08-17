# NUMT identification

## Required software

### R

```bash
conda create -n r_env r-essentials r-base
conda activate r_env
```

### Blast

```bash
conda install bioconda::blast
```

### Bedtools

```bash
conda install bioconda::bedtools
```



## Execution

Put get_bed.R in a common directory and change the pathway and filename in the python script. Execute the python script.



## Explanation

NUMT identification is to search the nucleus DNA which is similar to mitochondrial DNA. So we used blast to do the search and set some criteria to filter out the unfitted search result and then extract the DNA from the nucleus DNA files.