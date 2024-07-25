pyenv activate dx
dx login

dx run --instance-type mem1_ssd1_v2_x2 app-cloud_workstation

dx ssh job-GpQkY4QJzVpQ0FB33Xb9pvJ9

# after ssh connected
unset DX_WORKSPACE_ID
dx cd $DX_PROJECT_CONTEXT_ID:

dx select --level=VIEW

# VCF files for the filtered data of 1000 indviduals & 70K SNPs
dx download filtered.tar.gz

tar -xzf filtered.tar.gz

# count number of files out of cuorisity
cd filtered
ls -l |  wc -l