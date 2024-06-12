from django.contrib import admin, messages
from django.urls.resolvers import URLPattern
from django.urls import path
from django.shortcuts import render
from django import forms
from . models import Record
from django.http import HttpResponseRedirect
from django.urls import reverse
from import_export.admin import ImportExportModelAdmin

# Register your models here.



class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class RecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Record.objects.update_or_create(
                    first_name = fields[0],
                    
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)
                

        form = CsvImportForm()
        data = {"form":form}

        return render(request, "admin/csv_upload.html", data) 
        

admin.site.register(Record, RecordAdmin)