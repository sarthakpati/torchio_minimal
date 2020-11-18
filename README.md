# torchio_minimal

## Data

https://1drv.ms/u/s!AgvRZZtXCbbOnPgMjwBnFkHFdmNl-w?e=cRzBhA


## Instructions

### Environment setup
```powershell
git clone ${repo_link}
cd ${repo_name}
conda create -p ./venv python=3.6.5 -y
conda activate ./venv
conda install pytorch torchvision cudatoolkit=10.2 -c pytorch -y # install according to your cuda version https://pytorch.org/get-started/locally/
pip install -e .
```

### Data

Download from https://1drv.ms/u/s!AgvRZZtXCbbOnPgPFJtmucE_eMYoxA?e=lpRImD and expand into `${repo_name}` so that all data is in `${repo_name}/data`

### Run

```powershell
# continue from previous shell
python main.py
# see error
```