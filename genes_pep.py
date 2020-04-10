import os, glob

KEGG_DB_LOC = '/data11/bio/databases/kegg/'
all_peps_gz = glob.glob(os.path.join(KEGG_DB_LOC, 'genes/organisms/*/*.pep.gz'))


orgs = []
for o in all_peps_gz:
    orgs.append({'short_name': o.split('/')[-2], 'T_name': o.split('/')[-1].replace('.pep.gz', '')})

pep_gz_wc = os.path.join(KEGG_DB_LOC, 'genes/organisms/{short_name}/{T_name}.pep.gz')
pep_ungz_wc = os.path.join(KEGG_DB_LOC, 'genes/organisms/{short_name}/{T_name}.pep')

ungzed = []
for org in orgs:
    ungzed.append(pep_ungz_wc.format(**org))


rule ungz_pep:
    input: pep_gz_wc
    output: pep_ungz_wc
    shell: 'gunzip -c {input} > {output}'
        
rule ungz_all:
    input: ungzed