from dask.distributed import Client
import dask.dataframe as dd
import dask


SCHEDULER_ADDRESS = 'tcp://localhost:8786'
SHUFFLE_METHOD = 'p2p'
dask.config.set({'dataframe.shuffle.method': SHUFFLE_METHOD})

def main():
    client = Client(SCHEDULER_ADDRESS)

    df_1 = dd.demo.make_timeseries(
            start='2000-01-01', end='2000-12-31', dtypes={'name': str, 'value': float, 'id': int}, freq='1d', partition_freq='1M')
    df_2 = dd.demo.make_timeseries(
            start='2000-01-01', end='2000-12-31', dtypes={'name': str, 'value': float, 'id': int}, freq='1d', partition_freq='1M')
 
    df_1 = df_1.repartition(partition_size='2MB')
    df_2 = df_2.repartition(partition_size='2MB')
    df_1 = df_1.set_index("id")
    df_2 = df_2.set_index("id")
    merged = dd.merge(df_1, df_2, on='name', how='inner')
    result = dask.compute(merged)

if __name__ == "__main__":
    main()