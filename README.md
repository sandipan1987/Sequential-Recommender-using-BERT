### Setup (GPU)
```
conda create -n py38 python=3.8
conda activate py38
conda install pytorch torchvision cudatoolkit=11.1 -c pytorch -c conda-forge
conda install -c conda-forge jupyterlab
conda install -c conda-forge matplotlib
pip install .
```
### Docker (CPU)
```bash
docker build . -t recommender
docker run recommender sh -c "python3.8 -m pytest"
```
