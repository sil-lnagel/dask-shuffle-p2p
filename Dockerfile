FROM ghcr.io/dask/dask:2024.2.0

# pyarrow==15.0.0
RUN pip install prometheus-client==0.19.0