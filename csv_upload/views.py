from django.shortcuts import render, redirect
import pandas as pd
from .forms import FileUploadForm
from .models import UploadedFile
from .tasks import process_csv_file

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save()
            process_csv_file.delay(file_instance.file.path)  # Call Celery Task
            return redirect('file_list') 
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})





def file_list(request):
    # Retrieve last uploaded file
    latest_file = UploadedFile.objects.last()
    
    if latest_file:
        df = pd.read_csv(latest_file.file.path)
        data = df.to_dict(orient='records')  
    else:
        data = None
    
    return render(request, 'file_list.html', {'data': data})


def search_products(request):
    query = request.GET.get('q', '')
    latest_file = UploadedFile.objects.last()

    if latest_file and query:
        df = pd.read_csv(latest_file.file.path)
        filtered_data = df[df['Product Name'].str.contains(query, case=False, na=False)]
        data = filtered_data.to_dict(orient='records')
    else:
        data = None

    return render(request, 'search.html', {'data': data, 'query': query})

