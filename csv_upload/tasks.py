from celery import shared_task
import pandas as pd

@shared_task
def process_csv_file(file_path):
    df = pd.read_csv(file_path)

    numeric_cols = df.select_dtypes(include=['number'])
    results = {
        'sum': numeric_cols.sum().to_dict(),
        'average': numeric_cols.mean().to_dict(),
        'count': len(df)
    }
    
    return results

@shared_task
def test_celery():
    return "Celery is working!"
